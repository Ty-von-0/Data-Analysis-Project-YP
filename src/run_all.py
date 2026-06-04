from generate_program_types import generate_program_types
from generate_programs import generate_programs
from generate_members import generate_members
from generate_staff import generate_staff
from generate_program_session import generate_program_sessions
from generate_staff_session import generate_staff_sessions
from generate_attendance import generate_attendance
import pandas as pd

# 1. Program Types
df_program_types = generate_program_types()
df_program_types.to_csv("data/program_type.csv", index=False)
print("Program types generated.")

# 2. Programs
df_programs = generate_programs()
df_programs.to_csv("data/programs.csv", index=False)
print("Programs generated.")

# 3. Members
df_members = generate_members()
df_members.to_csv("data/members.csv", index=False)
print("Members generated.")

# 4. Staff
df_staff = generate_staff()
df_staff.to_csv("data/staff.csv", index=False)
print("Staff generated.")

# 5. Program Sessions
df_program_session = generate_program_sessions(df_programs)
df_program_session.to_csv("data/program_session.csv", index=False)
print("Program sessions generated.")

# 6. Staff Sessions
df_staff_session = generate_staff_sessions()
df_staff_session.to_csv("data/staff_session.csv", index=False)
print("Staff sessions generated.")

# 7. Attendance
df_attendance = generate_attendance()
df_attendance.to_csv("data/attendance.csv", index=False)
print("Attendance generated.")

print("All synthetic data generated successfully.")

