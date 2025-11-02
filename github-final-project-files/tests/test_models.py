import pytest
from tests.factories import ProductFactory

class FakeRepo:
    def __init__(self):
        self._data = {}

    def create(self, product):
        self._data[product.id] = product
        return product

    def get(self, product_id):
        return self._data.get(product_id)

    def update(self, product_id, **kwargs):
        product = self._data.get(product_id)
        if not product:
            return None
        for key, value in kwargs.items():
            setattr(product, key, value)
        return product

    def delete(self, product_id):
        return self._data.pop(product_id, None)

    def list_all(self):
        return list(self._data.values())

    def find_by_name(self, name):
        return [p for p in self._data.values() if name.lower() in p.name.lower()]

    def find_by_category(self, category):
        return [p for p in self._data.values() if p.category == category]

    def find_by_availability(self, available):
        return [p for p in self._data.values() if p.available == available]

@pytest.fixture
def repo():
    return FakeRepo()

def test_read_product(repo):
    p = ProductFactory.create()
    repo.create(p)
    result = repo.get(p.id)
    assert result.id == p.id

def test_update_product(repo):
    p = ProductFactory.create()
    repo.create(p)
    repo.update(p.id, name="UpdatedProduct")
    result = repo.get(p.id)
    assert result.name == "UpdatedProduct"

def test_delete_product(repo):
    p = ProductFactory.create()
    repo.create(p)
    repo.delete(p.id)
    assert repo.get(p.id) is None

def test_list_all_products(repo):
    p1 = ProductFactory.create()
    p2 = ProductFactory.create()
    repo.create(p1); repo.create(p2)
    assert len(repo.list_all()) >= 2

def test_find_by_name(repo):
    p = ProductFactory.create(name="SpecialProduct")
    repo.create(p)
    result = repo.find_by_name("Special")
    assert any("Special" in r.name for r in result)

def test_find_by_category(repo):
    p = ProductFactory.create(category="Toys")
    repo.create(p)
    result = repo.find_by_category("Toys")
    assert len(result) >= 1

def test_find_by_availability(repo):
    p = ProductFactory.create(available=False)
    repo.create(p)
    result = repo.find_by_availability(False)
    assert all(r.available == False for r in result)
