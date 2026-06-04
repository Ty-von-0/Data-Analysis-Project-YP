from setup import pd, random, timedelta, datetime

def generate_attendance():
    members_df = pd.read_csv("data/members.csv")
    sessions_df = pd.read_csv("data/program_session.csv")

    rows = []
    attendance_id = 1

    # Assign each member a commitment level
    # High: 70–90% attendance
    # Medium: 40–60%
    # Low: 10–30%
    commitment_map = {}
    for _, member in members_df.iterrows():
        if member["status"] == "Inactive":
            commitment_map[member["member_id"]] = 0  # never attends
        else:
            commitment_map[member["member_id"]] = random.choice([
                random.uniform(0.70, 0.90),  # high commitment
                random.uniform(0.40, 0.60),  # medium
                random.uniform(0.10, 0.30)   # low
            ])

    # Generate attendance records
    for _, session in sessions_df.iterrows():
        for _, member in members_df.iterrows():

            commit_rate = commitment_map[member["member_id"]]

            # Skip inactive members
            if commit_rate == 0:
                continue

            # Decide if member attends this session
            if random.random() <= commit_rate:

                # Check-in time slightly before or after start
                check_in_variation = random.randint(-10, 15)
                check_in_time = (
                    datetime.combine(
                        datetime.strptime(str(session["session_date"]), "%Y-%m-%d").date(),
                        datetime.strptime(session["start_time"], "%H:%M").time()
                    ) + timedelta(minutes=check_in_variation)
                ).strftime("%H:%M")

                rows.append({
                    "attendance_id": attendance_id,
                    "session_id": session["session_id"],
                    "member_id": member["member_id"],
                    "present": True,
                    "check_in_time": check_in_time,
                    "notes": ""
                })

                attendance_id += 1

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = generate_attendance()
    df.to_csv("data/attendance.csv", index=False)
    print("Attendance generated.")

