import pandas as pd

# ---------------------------------------------------------
# File paths — edit if your folder structure is different
# ---------------------------------------------------------
MAIN_ATTENDANCE_PATH = "data/attendance.csv"
MOC_ATTENDANCE_PATH = "data/attendance_mens_open_circle.csv"
OUTPUT_PATH = "data/attendance_merged.csv"

# ---------------------------------------------------------
# Load both attendance files
# ---------------------------------------------------------
main_df = pd.read_csv(MAIN_ATTENDANCE_PATH)
moc_df = pd.read_csv(MOC_ATTENDANCE_PATH)

# ---------------------------------------------------------
# If main attendance has attendance_id but MOC does not,
# or vice versa, we will regenerate IDs cleanly.
# ---------------------------------------------------------
# Drop attendance_id if present (we will recreate it)
if "attendance_id" in main_df.columns:
    main_df = main_df.drop(columns=["attendance_id"])

if "attendance_id" in moc_df.columns:
    moc_df = moc_df.drop(columns=["attendance_id"])

# ---------------------------------------------------------
# Merge the two datasets
# ---------------------------------------------------------
merged_df = pd.concat([main_df, moc_df], ignore_index=True)

# ---------------------------------------------------------
# Recreate attendance_id as a clean sequential integer
# ---------------------------------------------------------
merged_df.insert(0, "attendance_id", range(1, len(merged_df) + 1))

# ---------------------------------------------------------
# Save merged file
# ---------------------------------------------------------
merged_df.to_csv(OUTPUT_PATH, index=False)

print("Merged attendance saved to:", OUTPUT_PATH)
