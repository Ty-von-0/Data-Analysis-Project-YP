from setup import pd, random

def generate_programs():
    program_types = pd.read_csv("data/program_type.csv")

    program_names = [
        "Painting Workshop",
        "Basketball Night",
        "Homework Club",
        "Soccer Club"
        "Men's Open Circle",
        "Fitness Training",
        "Creative Writing",
        "Study Skills Lab",
        "Music Jam Session"
    ]

    rows = []
    program_id = 1

    for name in program_names:
        rows.append({
            "program_id": program_id,
            "program_name": name,
            "program_type_id": random.choice(program_types["program_type_id"].tolist()),
            "is_active": True
        })
        program_id += 1

    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_programs()
    df.to_csv("data/programs.csv", index=False)
    print("Programs generated.")

