import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# List of IPL teams
teams = [
    'Chennai Super Kings',
    'Delhi Daredevils',
    'Kings XI Punjab',
    'Kolkata Knight Riders',
    'Mumbai Indians',
    'Rajasthan Royals',
    'Royal Challengers Bangalore',
    'Sunrisers Hyderabad'
]

# Streamlit app configuration
st.set_page_config(page_title="IPL Score Predictor", page_icon="🏏", layout="centered")

# Title and description
st.title("🏏 IPL Score Predictor")
st.markdown("Predict the final score of an IPL match using Machine Learning")
st.markdown("---")

# Create two columns for team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting Team", teams, index=0)

with col2:
    bowling_team = st.selectbox("Select Bowling Team", teams, index=1)

# Validate that batting and bowling teams are different
if batting_team == bowling_team:
    st.error("Batting and Bowling teams must be different!")

# Match situation inputs
st.markdown("### Current Match Situation")

col3, col4, col5 = st.columns(3)

with col3:
    overs = st.number_input("Overs Completed", min_value=5.1, max_value=19.5, value=10.0, step=0.1, 
                            help="Enter overs in format: 10.2 means 10 overs and 2 balls")

with col4:
    runs = st.number_input("Current Runs", min_value=0, max_value=300, value=80, step=1)

with col5:
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=2, step=1)

# Last 5 overs statistics
st.markdown("### Last 5 Overs Statistics")

col6, col7 = st.columns(2)

with col6:
    runs_last_5 = st.number_input("Runs in Last 5 Overs", min_value=0, max_value=100, value=40, step=1)

with col7:
    wickets_last_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=5, value=1, step=1)

# Prediction function
def predict_score(batting_team, bowling_team, overs, runs, wickets, runs_last_5, wickets_last_5):
    """
    Predict the final score of an IPL match
    """
    # Create input features array matching the training data structure
    # The exact number of features depends on how your model was trained
    # Assuming: numeric features + one-hot encoded teams
    
    input_features = []
    
    # Add numeric features
    input_features.append(runs)
    input_features.append(wickets)
    input_features.append(overs)
    input_features.append(runs_last_5)
    input_features.append(wickets_last_5)
    
    # Add batting team one-hot encoding
    for team in teams:
        input_features.append(1 if team == batting_team else 0)
    
    # Add bowling team one-hot encoding
    for team in teams:
        input_features.append(1 if team == bowling_team else 0)
    
    # Convert to numpy array and reshape
    input_features = np.array(input_features).reshape(1, -1)
    
    # Make prediction
    predicted_score = model.predict(input_features)[0]
    
    # Ensure prediction is not less than current runs
    predicted_score = max(predicted_score, runs)
    
    return round(predicted_score)

# Predict button
st.markdown("---")
if st.button("Predict Final Score", type="primary", use_container_width=True):
    if batting_team != bowling_team:
        # Make prediction
        predicted_score = predict_score(batting_team, bowling_team, overs, runs, wickets, runs_last_5, wickets_last_5)
        
        # Display result
        st.markdown("### Prediction Result")
        
        # Create a nice display box
        col_result1, col_result2, col_result3 = st.columns([1, 2, 1])
        
        with col_result2:
            st.markdown(f"""
            <div style='background-color: #1e3a8a; padding: 30px; border-radius: 10px; text-align: center;'>
                <h2 style='color: white; margin: 0;'>Predicted Final Score</h2>
                <h1 style='color: #fbbf24; font-size: 60px; margin: 10px 0;'>{predicted_score}</h1>
                <p style='color: #d1d5db; margin: 0;'>Expected runs at end of innings</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Display match details
        st.markdown("### Match Summary")
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
            st.metric("Current Score", f"{runs}/{wickets}")
            st.metric("Overs Completed", f"{overs}")
            st.metric("Run Rate (Last 5)", f"{runs_last_5/5:.2f}")
        
        with summary_col2:
            st.metric("Predicted Final", predicted_score)
            st.metric("Runs Needed", max(0, predicted_score - runs))
            st.metric("Projected Total", f"{predicted_score}/{wickets if wickets < 10 else 10}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 20px;'>
    <p>Built with Machine Learning | Linear Regression Model</p>
    <p>Model Accuracy: RMSE ≈ 15.84 runs</p>
</div>
""", unsafe_allow_html=True)