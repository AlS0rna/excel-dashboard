import csv
import matplotlib.pyplot as plt

# Read the CSV file containing bank statements
with open('statements.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get the headers
    data = [row for row in reader]

# Sort the data by category
data.sort(key=lambda x: x[1])

# Group the data by category
categories = {}
for row in data:
    category = row[1]
    amount = float(row[2])
    if category not in categories:
        categories[category] = 0
    categories[category] += amount

# Extract the categories and amounts
labels = list(categories.keys())
amounts = list(categories.values())

# Plot the data
plt.pie(amounts, labels=labels, autopct='%1.1f%%')
plt.show()