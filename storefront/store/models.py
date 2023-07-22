from typing import Any
from datetime import datetime
from django.db import models
from security.models import UpdateLog


class Collection(UpdateLog):
    name = models.CharField(max_length=255, blank=False, null=False)
    featured_product = models.ForeignKey("Product", on_delete=models.SET_NULL, related_name="+")


# Create your models here.
class Product(UpdateLog):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, blank=False, null=False
    )
    promotions = models.ManyToManyField(
        "Promotion",
    )

    def __str__(self) -> str:
        return self.title


class Order(UpdateLog):
    PAYMENT_STATUS_PENDING = "PENDING"
    PAYMENT_STATUS_COMPLETE = "COMPLETE"
    PAYMENT_STATUS_FAILED = "FAILED"
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
        (PAYMENT_STATUS_PENDING, "Pending"),
    ]
    payment_status = models.CharField(
        max_length=5, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING
    )
    customer = models.ForeignKey("Customer", on_delete=models.PROTECT)


class Customer(UpdateLog):
    MEMBERSHIP_SILVER = 1
    MEMBERSHIP_GOLD = 2
    MEMBERSHIP_PLATINUM = 3
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
        max_length=5, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_GOLD
    )


class Address(UpdateLog):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )


class OrderItem(UpdateLog):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(UpdateLog):
    pass


class CartItem(UpdateLog):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Promotion(UpdateLog):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
