from setup import pd, random, PROGRAM_START, PROGRAM_END, timedelta

def generate_program_sessions(programs_df, session_count=300):
    rows = []
    session_id = 1

    current = PROGRAM_START
    while current <= PROGRAM_END:
        weekday = current.weekday()

        # Friday evening sessions
        if weekday == 4:
            rows.append({
                "session_id": session_id,
                "program_id": random.choice(programs_df["program_id"].tolist()),
                "session_date": current.date(),
                "start_time": "18:00",
                "end_time": "21:00"
            })
            session_id += 1

        # Occasional Saturday sessions
        if weekday == 5 and random.random() < 0.25:
            rows.append({
                "session_id": session_id,
                "program_id": random.choice(programs_df["program_id"].tolist()),
                "session_date": current.date(),
                "start_time": "18:00",
                "end_time": "21:00"
            })
            session_id += 1

        current += timedelta(days=1)

    return pd.DataFrame(rows)

if __name__ == "__main__":
    programs_df = pd.read_csv("data/programs.csv")
    df = generate_program_sessions(programs_df)
    df.to_csv("data/program_session.csv", index=False)
    print("Program sessions generated.")

