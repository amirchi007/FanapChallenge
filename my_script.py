import csv
from collections import defaultdict

# Open and read the CSV file
def analyze_sales(filename):
    total_sales = 0
    sales_count = 0
    sales_by_date = defaultdict(int)

    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = int(row['amount'])
            date = row['date']
            total_sales += amount
            sales_count += 1
            sales_by_date[date] += amount

    # Calculate average
    average_sale = total_sales / sales_count if sales_count > 0 else 0

    # Find the day with the highest sales
    max_day = max(sales_by_date.items(), key=lambda item: item[1])

    # Print results
    print("Total Sales:", total_sales)
    print("Average Sale Amount:", average_sale)
    print("Highest Sales Day:", max_day[0], "with", max_day[1], "units")

# Example usage
analyze_sales('sales.csv')
