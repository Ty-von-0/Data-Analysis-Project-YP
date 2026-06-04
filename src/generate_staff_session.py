from setup import pd, random

def generate_staff_sessions():
    staff_df = pd.read_csv("data/staff.csv")
    sessions_df = pd.read_csv("data/program_session.csv")

    rows = []
    staff_session_id = 1

    for _, session in sessions_df.iterrows():
        assigned_staff = random.sample(
            staff_df["staff_id"].tolist(),
            k=random.randint(1, 2)
        )

        for staff_id in assigned_staff:
            rows.append({
                "staff_session_id": staff_session_id,
                "staff_id": staff_id,
                "session_id": session["session_id"],
                "role_during_session": "Facilitator"
            })
            staff_session_id += 1

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_staff_sessions()
    df.to_csv("data/staff_session.csv", index=False)
    print("Staff sessions generated.")
