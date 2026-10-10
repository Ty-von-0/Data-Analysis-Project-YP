import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

# -----------------------------------------
# 1. Load members and sessions
# -----------------------------------------
members = pd.read_csv("data/members.csv")
sessions = pd.read_csv("data/program_session.csv")

# Filter only sessions for Men's Open Circle (program_id = 9)
sessions = sessions[sessions["program_id"] == 9]

# Use only active members
active_members = members[members["status"] == "Active"]["member_id"].tolist()

# -----------------------------------------
# 2. Function to generate a random check-in time
# -----------------------------------------
def random_checkin(start_time_str):
    base = datetime.strptime(start_time_str, "%H:%M")
    offset = random.randint(-10, 15)  # between 17:50 and 18:15
    return (base + timedelta(minutes=offset)).strftime("%H:%M")

# -----------------------------------------
# 3. Generate attendance rows
# -----------------------------------------
attendance_rows = []

for _, session in sessions.iterrows():

    session_id = session["session_id"]
    start_time = session["start_time"]

    # Randomly pick 15 attendees
    attendees = random.sample(active_members, 15)

    for member_id in attendees:
        attendance_rows.append({
            "session_id": session_id,
            "member_id": member_id,
            "present": True,
            "check_in_time": random_checkin(start_time),
            "notes": ""
        })

attendance_df = pd.DataFrame(attendance_rows)

# -----------------------------------------
# 4. Save to CSV
# -----------------------------------------
attendance_df.to_csv("data/attendance_mens_open_circle.csv", index=False)

print("Men's Open Circle attendance generated.")
