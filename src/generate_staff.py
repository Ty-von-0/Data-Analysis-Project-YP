from setup import fake, random, pd

def generate_staff(n=12):
    rows = []
    for staff_id in range(1, n+1):
        rows.append({
            "staff_id": staff_id,
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name(),
            "role": random.choice(["Facilitator", "Coach", "Tutor", "Support Worker"]),
            "hire_date": fake.date_between(start_date="-3y", end_date="today"),
            "status": "Active"
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_staff()
    df.to_csv("data/staff.csv", index=False)
    print("Staff generated.")
