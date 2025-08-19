import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. CREATE A DUMMY DATASET
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"],
    "Age": [20, 22, 21, 24, 23, 21, 25, 22],
    "Hours_Studied": [10, 12, 9, 15, 13, 8, 14, 10],
    "Test_Score": [80, 83, 78, 90, 87, 75, 88, 82]
}

df = pd.DataFrame(data)

# 2. EXPLORATORY DATA ANALYSIS
print("Dummy Dataset:")
print(df)

print("\nDescriptive Statistics:")
print(df.describe())

# Calculate correlation on numeric columns only
numeric_df = df.select_dtypes(include=[np.number])
print("\nCorrelation Matrix:")
print(numeric_df.corr())

# 3. PLOTTING
plt.scatter(df["Hours_Studied"], df["Test_Score"])
plt.title("Study Hours vs Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.show()

# 4. SIMPLE LINEAR REGRESSION
X = df[["Hours_Studied"]]  # Independent variable (2D)
y = df["Test_Score"]       # Dependent variable

model = LinearRegression()
model.fit(X, y)

# Predict the test score for 10 hours of study (example)
pred_hours = [[10]]
predicted_score = model.predict(pred_hours)[0]

print(f"\nPredicted Test Score for {pred_hours[0][0]} Hours of Study: {predicted_score:.2f}")
