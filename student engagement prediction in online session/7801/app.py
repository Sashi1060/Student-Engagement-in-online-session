import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("7801.csv")

# Preprocess data
le = LabelEncoder()
df["Level"] = le.fit_transform(df["Level"])
X = df.drop("Level", axis=1)
y = df["Level"]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Streamlit app
st.title("Level Prediction")

# Sidebar inputs
st.sidebar.header("Input Parameters")
total_items = st.sidebar.slider("Total Items", 0.0, 1.0)
time_spent = st.sidebar.slider("Time Spent in Course", 0.0, 1.0)
total_logins = st.sidebar.slider("Total Logins", 0.0, 1.0)
activity_inside_content_area = st.sidebar.slider("Activity inside Content Area", 0.0, 1.0, 0.5)
user_activity_in_group = st.sidebar.slider("User Activity in Group", 0.0, 1.0, 0.5)
nbre_of_clics = st.sidebar.slider("Number of Clicks", 0.0, 1.0)
nbre_of_message_participation = st.sidebar.slider("Number of Message Participation", 0.0, 1.0)
join_session = st.sidebar.slider("Join Session", 0.0, 1.0, 0.5)
time_spent_on_session_attendence = st.sidebar.slider("Time Spent on Session Attendence", 0.0, 1.0, 0.5)

# Make prediction
input_data = [[total_items, time_spent, total_logins, activity_inside_content_area, user_activity_in_group, nbre_of_clics, nbre_of_message_participation, join_session, time_spent_on_session_attendence]]
input_data_scaled = scaler.transform(input_data)
prediction = le.inverse_transform(clf.predict(input_data_scaled))[0]

# Display prediction
st.subheader("Prediction")
st.write("The predicted level is", prediction)
