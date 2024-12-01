import pandas as pd

data = pd.read_csv("day_1/input.csv")

# Convert columns to int
data["left_list"] = data["left_list"].astype(int)
data["right_list"] = data["right_list"].astype(int)

# Sort values
ordered_left = data.sort_values(by=["left_list"]).copy()
ordered_right = data.sort_values(by=["right_list"]).copy()

# Reset index
ordered_left.reset_index(drop=True, inplace=True)
ordered_right.reset_index(drop=True, inplace=True)

# Calculate the sum of the absolute differences between the two lists
print(sum(abs(ordered_left["left_list"] - ordered_right["right_list"])))

###### part 2
# Get uniques from left_list
unique_values = data["left_list"].unique()
value_counts_right = ordered_right["right_list"].value_counts()
value_counts_map = {}
for value in unique_values:
    value_counts_map[value] = value_counts_right.get(value, 0) * value

# Calculate the sum using the dict
data["similarity_score"] = data["left_list"].map(value_counts_map)

print(sum(data["similarity_score"]))
