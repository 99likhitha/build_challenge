import pandas as pd


class SalesAnalysis:
    def __init__(self, csv_file):
        # Reading CSV
        self.df = pd.read_csv(csv_file, parse_dates=["date"])

        # Functional transformation
        self.df = (
            self.df
            .assign(
                revenue=lambda x: x.price * x.quantity * (1 - x.discount),
                cost_total=lambda x: x.cost * x.quantity,
                profit=lambda x: x.revenue - x.cost_total,
                month=lambda x: x.date.dt.to_period("M").astype(str),
                year=lambda x: x.date.dt.year,
                weekday=lambda x: x.date.dt.day_name()
            )
        )

    # Total revenue
    def total_revenue(self):
        return float(self.df["revenue"].sum())

    # Revenue grouped by category
    def revenue_by_category(self):
        return (
            self.df.groupby("category")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .to_dict()
        )

   
    # Revenue grouped by region
    def revenue_by_region(self):
        return (
            self.df.groupby("region")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .to_dict()
        )

    # Top N products by revenue

    def top_n_products(self, n=5):
        return (
            self.df.groupby("product")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .head(n)
                   .index
                   .tolist()
        )

    # Monthly performance metrics 

    def monthly_summary(self):
        return (
            self.df.groupby("month")
                   .agg(
                       total_revenue=("revenue", "sum"),
                       total_profit=("profit", "sum"),
                       total_units=("quantity", "sum"),
                       avg_discount=("discount", "mean"),
                       avg_order_value=("revenue", "mean")
                   )
                   .sort_index()
                   .to_dict("index")
        )

    # Category revenue contribution (%) 

    def category_contribution_percent(self):
        total = self.df["revenue"].sum()
        return (
            self.df.groupby("category")["revenue"]
               .sum()
               .apply(lambda r: round((r / total) * 100, 2))
               .sort_values(ascending=False)
               .to_dict()
        )

    # Customer lifetime revenue (CLV proxy)

    def customer_lifetime_revenue(self):
        return (
            self.df.groupby("customer_id")["revenue"]
                   .sum()
                   .sort_values(ascending=False)
                   .to_dict()
        )

    # Payment method usage count

    def payment_method_distribution(self):
        return (
            self.df["payment_method"]
                   .value_counts()
                   .to_dict()
        )

    # Average profit by category

    def avg_profit_by_category(self):
        return (
            self.df.groupby("category")["profit"]
                   .mean()
                   .sort_values(ascending=False)
                   .to_dict()
        )
