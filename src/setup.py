from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker("en_CA")

Faker.seed(42)
random.seed(42)

# Global date range for program sessions
PROGRAM_START = datetime(2024, 1, 1)
PROGRAM_END = datetime(2024, 12, 31)

print("Setup Complete.")