def test_read_route(client):
    resp = client.get("/products/1")
    assert resp.status_code in [200, 404]

def test_update_route(client):
    resp = client.put("/products/1", json={"name": "NewProduct"})
    assert resp.status_code in [200, 404]

def test_delete_route(client):
    resp = client.delete("/products/1")
    assert resp.status_code in [200, 404, 204]

def test_list_all_route(client):
    resp = client.get("/products")
    assert resp.status_code == 200

def test_list_by_name_route(client):
    resp = client.get("/products?name=Test")
    assert resp.status_code == 200

def test_list_by_category_route(client):
    resp = client.get("/products?category=Electronics")
    assert resp.status_code == 200

def test_list_by_availability_route(client):
    resp = client.get("/products?available=true")
    assert resp.status_code == 200
