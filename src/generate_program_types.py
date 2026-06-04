from setup import pd

def generate_program_types():
    program_types = [
        {"program_type_id": 1, "program_type_name": "Arts"},
        {"program_type_id": 2, "program_type_name": "Sports"},
        {"program_type_id": 3, "program_type_name": "Academic Support"},
        {"program_type_id": 4, "program_type_name": "Open Circle Discussions"},
    ]
    return pd.DataFrame(program_types)

if __name__ == "__main__":
    df = generate_program_types()
    df.to_csv("data/program_type.csv", index=False)
    print("Program types generated.")
