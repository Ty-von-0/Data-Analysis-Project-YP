from setup import fake, random, pd

def generate_members(n=60):
    rows = []
    for member_id in range(1, n+1):
        rows.append({
            "member_id": member_id,
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name(),
            "age": random.randint(17, 24),
            "gender": "Male",
            "join_date": fake.date_between(start_date="-2y", end_date="today"),
            "status": random.choice(["Active", "Inactive"])
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_members()
    df.to_csv("data/members.csv", index=False)
    print("Members generated.")

