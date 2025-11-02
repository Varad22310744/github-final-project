from dataclasses import dataclass
import random

@dataclass
class ProductFactory:
    id: int = None
    name: str = "SampleProduct"
    category: str = "General"
    price: float = 99.99
    available: bool = True

    @classmethod
    def create(cls, **kwargs):
        data = {
            "id": kwargs.get("id", random.randint(1000, 9999)),
            "name": kwargs.get("name", f"Product-{random.randint(1,999)}"),
            "category": kwargs.get("category", "General"),
            "price": kwargs.get("price", 99.99),
            "available": kwargs.get("available", True)
        }
        return cls(**data)
