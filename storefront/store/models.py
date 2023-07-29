from typing import Any
from datetime import datetime
from django.db import models
from security.models import SecurityBaseModel


class Collection(SecurityBaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    featured_product = models.ForeignKey(
        "Product",
        null=True,
        on_delete=models.SET_NULL,
        related_name="collection_product",
    )

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.name


# Create your models here.
class Product(SecurityBaseModel):
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(default="-")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, blank=False, null=False
    )
    promotions = models.ManyToManyField(
        "Promotion",
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title


class Order(SecurityBaseModel):
    PAYMENT_STATUS_PENDING = "PENDING"
    PAYMENT_STATUS_COMPLETE = "COMPLETE"
    PAYMENT_STATUS_FAILED = "FAILED"
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
        (PAYMENT_STATUS_PENDING, "Pending"),
    ]
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey(
        "Customer", on_delete=models.PROTECT, related_name="order_customer"
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"{self.customer.pk} {self.customer.first_name} {self.payment_status}"


class Customer(SecurityBaseModel):
    MEMBERSHIP_SILVER = "SILVER"
    MEMBERSHIP_GOLD = "GOLD"
    MEMBERSHIP_PLATINUM = "PLATINUM"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
        (MEMBERSHIP_PLATINUM, "Platinum"),
    ]
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, max_length=254, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=20, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_GOLD
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        indexes = [models.Index(fields=["last_name", "first_name", "email"])]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(SecurityBaseModel):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="address_customer",
    )
    zip = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.city}"


class OrderItem(SecurityBaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="order_item_product"
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"


class Cart(SecurityBaseModel):
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(SecurityBaseModel):
    """
    Products added to a Cart
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_item_product"
    )

    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"


class Promotion(SecurityBaseModel):
    """
    Discount to be offered
    """

    description = models.CharField(max_length=255)
    discount = models.FloatField()

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"
