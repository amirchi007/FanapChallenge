# Optional: Create the CSV file for testing
def create_sample_csv():
    data = [
        ["date", "amount", "product"],
        ["2025-08-01", "1200", "Book"],
        ["2025-08-01", "800", "Pen"],
        ["2025-08-02", "1500", "Notebook"],
        ["2025-08-02", "500", "Book"],
        ["2025-08-03", "3000", "Laptop"],
        ["2025-08-03", "700", "Mouse"],
    ]

    with open("sales.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Create CSV then analyze
create_sample_csv()
analyze_sales('sales.csv')
