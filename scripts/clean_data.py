import pandas as pd
from pathlib import Path

# File paths
RAW = Path("data/raw/gym_members_exercise_tracking.csv")
OUT = Path("data/processed/gym_members_cleaned.csv")

# Read raw data
df = pd.read_csv(RAW)

# Add unique member ID
df["member_id"] = range(1, len(df) + 1)

# Clean column names for easier use
df.columns = (
    df.columns.str.strip()
    .str.replace(" ", "_")
    .str.replace("(", "")
    .str.replace(")", "")
    .str.replace("/", "_")
)

# Create retention status (1 = active, 0 = inactive)
df["retention_status"] = (
    (df["Workout_Frequency_days_week"] >= 3)
    & (df["Session_Duration_hours"] >= 1.0)
).astype(int)

# Save cleaned dataset
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

# Print quick summary
print("✅ Cleaning complete!")
print(df["retention_status"].value_counts(normalize=True) * 100)
