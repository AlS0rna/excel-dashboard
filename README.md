# excel-dashboard

This script assumes that the CSV file has the following structure:
Date	Category	Amount
2021-01-01	Groceries	50.00
2021-01-02	Entertainment	100.00
2021-01-03	Groceries	75.00
You can customize the script to fit your specific needs. For example, you can add more columns to the CSV file, or you can use a different type of chart to visualize the data.

This script generates a pie chart showing the percentage of total spending in each category. The pie chart is generated using the pie function from the matplotlib library. The autopct parameter is used to display the percentage value for each slice of the pie.
You can customize the appearance of the pie chart by setting additional parameters of the pie function. For example, you can use the colors parameter to specify the colors of the slices, or the explode parameter to pull out a slice from the pie. You can find more information about these parameters in the documentation for the pie function: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
