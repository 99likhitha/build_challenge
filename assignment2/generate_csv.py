import csv, random
from datetime import datetime, timedelta

# Optional: makes results reproducible
random.seed(42)

products = [
    ("Laptop", "Electronics", 1000, 800),
    ("Mouse", "Electronics", 25, 10),
    ("TV", "Electronics", 500, 450),
    ("Shirt", "Apparel", 30, 12),
    ("Jeans", "Apparel", 55, 25),
    ("Headphones", "Electronics", 150, 75),
    ("Shoes", "Footwear", 90, 40),
    ("Keyboard", "Electronics", 45, 20),
    ("Watch", "Accessories", 100, 40),
    ("Bag", "Accessories", 60, 25),
]

regions = ["North", "South", "East", "West"]
payment_methods = ["Credit Card", "Debit Card", "Cash", "UPI"]

def random_date(start, end):
    """Generate random date between start and end"""
    return start + timedelta(days=random.randint(0, (end - start).days))

output_file = "sales_data_large.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "order_id","customer_id","product","category","price","cost","quantity",
        "discount","region","payment_method","date"
    ])

    for i in range(1, 1001):  # <-- CHANGED FROM 500 TO 1000
        prod, cat, price, cost = random.choice(products)
        quantity = random.randint(1, 5)
        discount = random.choice([0.0, 0.05, 0.10, 0.15, 0.20])
        region = random.choice(regions)
        payment = random.choice(payment_methods)
        date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31)).strftime("%Y-%m-%d")
        cust = f"C{random.randint(1, 200):04d}"

        writer.writerow([
            i, cust, prod, cat, price, cost, quantity,
            discount, region, payment, date
        ])

print("Generated:", output_file)
