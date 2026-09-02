"""Canonical enterprise-operations definitions shared by data-facing components."""

from __future__ import annotations

BUSINESS_DEFINITIONS: dict[str, str] = {
    "effective_sales": (
        "Valid sales orders have status confirmed, shipped, or completed; cancelled is excluded. "
        "Sales revenue is sales_order_items.quantity * unit_price."
    ),
    "effective_purchase_amount": (
        "Valid purchase orders have status ordered, partially_delivered, or delivered; cancelled is excluded. "
        "Procurement spend is quantity * unit_cost."
    ),
    "current_inventory": (
        "Current inventory is selected per product by the maximum snapshot_date in inventory_snapshots; "
        "inventory risk occurs only when on_hand_quantity < safety_stock."
    ),
    "on_time_delivery_rate": (
        "On-time delivery rate only includes purchase orders with status delivered and non-null actual_delivery_date; "
        "actual_delivery_date <= promised_delivery_date is considered on time; zero delivered sample yields NULL, not 0%."
    ),
    "not_delivered": (
        "Undelivered purchase means status in ordered or partially_delivered and actual_delivery_date is NULL."
    ),
    "natural_month": (
        "A natural month interval includes the start date and excludes the next month's start date, using Asia/Shanghai calendar dates."
    ),
}
