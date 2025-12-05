import pandas as pd
from assignment2.sales_analysis import SalesAnalysis

CSV_FILE = "assignment2/sales_data_large.csv"


def test_total_revenue():
    sa = SalesAnalysis(CSV_FILE)
    assert sa.total_revenue() > 0


def test_revenue_by_category():
    sa = SalesAnalysis(CSV_FILE)
    result = sa.revenue_by_category()

    assert isinstance(result, dict)
    assert len(result) >= 3
    assert all(v > 0 for v in result.values())


def test_revenue_by_region():
    sa = SalesAnalysis(CSV_FILE)
    result = sa.revenue_by_region()

    assert set(result.keys()).issubset({"North", "South", "East", "West"})
    assert all(v > 0 for v in result.values())


def test_top_n_products():
    sa = SalesAnalysis(CSV_FILE)
    top = sa.top_n_products(3)

    assert len(top) == 3
    assert all(isinstance(p, str) for p in top)


def test_monthly_summary():
    sa = SalesAnalysis(CSV_FILE)
    summary = sa.monthly_summary()

    # At least some months must exist
    assert len(summary) >= 6

    # Check structure
    for metrics in summary.values():
        assert "total_revenue" in metrics
        assert "total_profit" in metrics
        assert "total_units" in metrics


def test_category_contribution():
    sa = SalesAnalysis(CSV_FILE)
    contrib = sa.category_contribution_percent()

    total_percent = sum(contrib.values())
    assert 98 <= total_percent <= 102  # Allow rounding tolerance


def test_customer_lifetime_revenue():
    sa = SalesAnalysis(CSV_FILE)
    clv = sa.customer_lifetime_revenue()

    assert len(clv) > 0
    assert all(v > 0 for v in clv.values())


def test_payment_method_distribution():
    sa = SalesAnalysis(CSV_FILE)
    dist = sa.payment_method_distribution()

    assert set(dist.keys()).issubset(
        {"Credit Card", "Debit Card", "Cash", "UPI"}
    )
    assert sum(dist.values()) == 1000


def test_avg_profit_by_category():
    sa = SalesAnalysis(CSV_FILE)
    result = sa.avg_profit_by_category()

    assert isinstance(result, dict)
    assert len(result) >= 3
