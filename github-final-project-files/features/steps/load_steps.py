from behave import given
from tests.factories import ProductFactory

@given("the system has sample products loaded")
def step_impl(context):
    context.products = [
        ProductFactory.create(name="A"),
        ProductFactory.create(name="B", category="Electronics"),
        ProductFactory.create(name="C", available=False)
    ]
