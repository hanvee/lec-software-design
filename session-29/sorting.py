from datetime import datetime
from typing import List, Literal

# Product class
class Product:
    def __init__(self, name: str, quantity: int, created_date: str):
        self.name = name
        self.quantity = quantity
        self.created_date = datetime.strptime(created_date, '%Y-%m-%d')

    def __repr__(self):
        return f"{self.name} | Qty: {self.quantity} | Date: {self.created_date.date()}"

SortField = Literal["name", "quantity", "created_date"]
SortOrder = Literal["asc", "desc"]

def compare(a: Product, b: Product, field: SortField, order: SortOrder) -> bool:
    if field == "name":
        val_a = a.name.lower()
        val_b = b.name.lower()
    elif field == "quantity":
        val_a = a.quantity
        val_b = b.quantity
    elif field == "created_date":
        val_a = a.created_date
        val_b = b.created_date
    else:
        raise ValueError("Unsupported field")

    if order == "asc":
        return val_a > val_b
    else:
        return val_a < val_b


def sort_products(products: List[Product], field: SortField, order: SortOrder = "asc") -> List[Product]:
    sorted_list = products.copy()
    n = len(sorted_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(sorted_list[j], sorted_list[j + 1], field, order):
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list


def print_products(title: str, products: List[Product]):
    print(f"\n{title}")
    for p in products:
        print(f"- {p}")

# Sample product list
products: List[Product] = [
    Product("Keyboard", 12, "2025-01-10"),
    Product("Mouse", 10, "2025-05-22"),
    Product("Laptop", 5, "2025-12-01"),
    Product("Speaker", 6, "2025-07-15"),
]

# Example Usage
print_products("Sorted by Name (A-Z):", sort_products(products, "name", "asc"))
print_products("Sorted by Quantity (High to Low):", sort_products(products, "quantity", "desc"))
print_products("Sorted by Created Date (Newest First):", sort_products(products, "created_date", "desc"))
