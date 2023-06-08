import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Random Forest Model Prediction")

# create labels and entry fields for each feature
total_items_label = tk.Label(root, text="Total Items:")
total_items_label.grid(row=0, column=0)
total_items_entry = tk.Entry(root)
total_items_entry.grid(row=0, column=1)

time_spent_label = tk.Label(root, text="Time Spent in Course:")
time_spent_label.grid(row=1, column=0)
time_spent_entry = tk.Entry(root)
time_spent_entry.grid(row=1, column=1)

total_logins_label = tk.Label(root, text="Total Logins:")
total_logins_label.grid(row=2, column=0)
total_logins_entry = tk.Entry(root)
total_logins_entry.grid(row=2, column=1)

activity_label = tk.Label(root, text="Activity inside Content Area:")
activity_label.grid(row=3, column=0)
activity_entry = tk.Entry(root)
activity_entry.grid(row=3, column=1)

user_activity_label = tk.Label(root, text="User Activity in Group:")
user_activity_label.grid(row=4, column=0)
user_activity_entry = tk.Entry(root)
user_activity_entry.grid(row=4, column=1)

clicks_label = tk.Label(root, text="Number of Clicks:")
clicks_label.grid(row=5, column=0)
clicks_entry = tk.Entry(root)
clicks_entry.grid(row=5, column=1)

message_label = tk.Label(root, text="Number of Message Participations:")
message_label.grid(row=6, column=0)
message_entry = tk.Entry(root)
message_entry.grid(row=6, column=1)

session_label = tk.Label(root, text="Join Session:")
session_label.grid(row=7, column=0)
session_entry = tk.Entry(root)
session_entry.grid(row=7, column=1)

time_spent_session_label = tk.Label(root, text="Time Spent on Session Attendance:")
time_spent_session_label.grid(row=8, column=0)
time_spent_session_entry = tk.Entry(root)
time_spent_session_entry.grid(row=8, column=1)

level_label = tk.Label(root, text="Level:")
level_label.grid(row=9, column=0)
level_entry = tk.Entry(root)
level_entry.grid(row=9, column=1)

# function to get the values entered by the user and make a prediction
def make_prediction():
    # get the values entered by the