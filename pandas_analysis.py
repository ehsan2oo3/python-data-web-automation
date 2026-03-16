import pandas as pd

# Create DataFrame
data = {
    "Name": ["Ali", "Sara", "John", "Mina"],
    "Age": [22, 21, 23, 22],
    "Score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Filter
high_scores = df[df["Score"] > 80]

# Grouping
grouped = df.groupby("Age")["Score"].mean()

print("High Scores:\n", high_scores)
print("\nAverage Score by Age:\n", grouped)