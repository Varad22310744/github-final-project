Feature: Product Service

  Scenario: Reading a Product
    Given the system has sample products loaded
    When I GET the product with id 1
    Then the response status should be 200

  Scenario: Updating a Product
    Given the system has sample products loaded
    When I PUT to /products/1 with {"name": "UpdatedName"}
    Then the response status should be 200

  Scenario: Deleting a Product
    Given the system has sample products loaded
    When I DELETE /products/1
    Then the response status should be 204

  Scenario: Listing all Products
    Given the system has sample products loaded
    When I GET /products
    Then the response status should be 200

  Scenario: Searching by category
    Given the system has sample products loaded
    When I GET /products?category=Electronics
    Then the response status should be 200

  Scenario: Searching by availability
    Given the system has sample products loaded
    When I GET /products?available=true
    Then the response status should be 200

  Scenario: Searching by name
    Given the system has sample products loaded
    When I GET /products?name=A
    Then the response status should be 200
