from datetime import datetime, date
from uuid import UUID

import pytest

from .types import (
    Address,
    ProductVariant,
    Product,
    ProductCategory,
    Customer,
    CustomerTier,
    OrderItem,
    PaymentDetails,
    OrderRequest,
    OrderResponse,
    PaginatedResponse,
    OrderStatus,
    PaymentMethod,
)


@pytest.fixture
def example_address() -> Address:
    return Address(street="123 Main St", city="Anytown", state="CA", postal_code="12345", country="US", is_primary=True)


@pytest.fixture
def example_product_variant() -> ProductVariant:
    return ProductVariant(
        sku="EP-001-BLK", color="Black", stock_count=10, size=None, weight=None, dimensions=None, in_stock=True
    )


@pytest.fixture
def example_product(example_product_variant) -> Product:
    return Product(
        id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        name="Example Product",
        description="This is an example product",
        category=ProductCategory.ELECTRONICS,
        price=199.99,
        discount_percent=None,
        tax_rate=None,
        rating=None,
        review_count=0,
        tags=["example", "new"],
        image_urls=["https://example.com/image.jpg"],
        created_at=datetime.now(),
        variants=[example_product_variant],
    )


@pytest.fixture
def example_customer(example_address) -> Customer:
    return Customer(
        id=UUID("770f9511-f39c-42d5-a860-557654551222"),
        email="customer@example.com",
        full_name="John Doe",
        phone="1234567890",
        tier=CustomerTier.STANDARD,
        addresses=[example_address],
        created_at=datetime.now(),
        preferences={"theme": "dark", "notifications": True},
        consent={"marketing": True, "analytics": True},
    )


@pytest.fixture
def example_order_item() -> OrderItem:
    return OrderItem(
        product_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        variant_sku="EP-001-BLK",
        quantity=2,
        unit_price=199.99,
        discount_amount=10.00,
        total=389.98,
    )


@pytest.fixture
def example_payment_details() -> PaymentDetails:
    return PaymentDetails(
        method=PaymentMethod.CREDIT_CARD,
        transaction_id="txn_12345",
        status="completed",
        amount=389.98,
        currency="USD",
        paid_at=datetime.now(),
    )


@pytest.fixture
def example_order_request(example_order_item) -> OrderRequest:
    return OrderRequest(
        customer_id=UUID("770f9511-f39c-42d5-a860-557654551222"),
        items=[example_order_item],
        shipping_address_id=UUID("880f9511-f39c-42d5-a860-557654551333"),
        billing_address_id=None,
        payment_method=PaymentMethod.CREDIT_CARD,
        notes="Please deliver before 6pm",
        use_loyalty_points=False,
    )


@pytest.fixture
def example_order_response(example_order_item, example_address, example_payment_details) -> OrderResponse:
    return OrderResponse(
        id=UUID("660f9511-f39c-42d5-a860-557654551111"),
        customer_id=UUID("770f9511-f39c-42d5-a860-557654551222"),
        status=OrderStatus.PENDING,
        items=[example_order_item],
        shipping_address=example_address,
        billing_address=example_address,
        payment=example_payment_details,
        subtotal=389.98,
        shipping_cost=10.0,
        tax_amount=20.0,
        discount_amount=10.0,
        total_amount=409.98,
        tracking_number="TRK123456789",
        estimated_delivery=date.today(),
        created_at=datetime.now(),
        notes="Please deliver before 6pm",
        metadata={},
    )


@pytest.fixture
def example_paginated_products(example_product) -> PaginatedResponse:
    return PaginatedResponse(items=[example_product], total=1, page=1, size=20, pages=1)
