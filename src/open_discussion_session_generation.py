import pandas as pd
from datetime import datetime, timedelta

# -----------------------------------------
# Load existing program_session.csv
# -----------------------------------------
sessions = pd.read_csv("data/program_session.csv")

# -----------------------------------------
# Create 52 weekly sessions for program_id = 9
# -----------------------------------------
program_id = 9
start_date = datetime(2024, 1, 5)  # first Friday of 2024
num_sessions = 52

new_sessions = []

for i in range(num_sessions):
    session_date = start_date + timedelta(weeks=i)

    new_sessions.append({
        "session_id": sessions["session_id"].max() + 1 + i,
        "program_id": program_id,
        "session_date": session_date.strftime("%Y-%m-%d"),
        "start_time": "18:00",
        "end_time": "21:00"
    })

new_sessions_df = pd.DataFrame(new_sessions)

# -----------------------------------------
# Append to existing sessions
# -----------------------------------------
updated_sessions = pd.concat([sessions, new_sessions_df], ignore_index=True)

# -----------------------------------------
# Save updated file
# -----------------------------------------
updated_sessions.to_csv("data/program_session.csv", index=False)

print("Program sessions for Men's Open Circle added.")
