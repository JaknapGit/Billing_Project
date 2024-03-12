from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from auth_app.models import User
from inventory.models import Product

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_contact = PhoneNumberField(region='IN', unique=True)
    customer_address = models.TextField()
    customer_email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.customer_name}'
    
class Invoice(models.Model):
    invoice_id = models.BigAutoField(primary_key=True)
    invoice_number = models.PositiveIntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    total_cost_without_gst = models.FloatField(default=0.0)
    total_cost_with_offers_and_gst = models.FloatField(default=0.0)
    total_cost_with_gst = models.FloatField(default=0.0)
    invoice_created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'user_invoices')

    def __str__(self) -> str:
        return f'{self.invoice_number}'
    
class InvoiceProduct(models.Model):
    invoice_product_id = models.BigAutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, related_name='product_in_invoice', blank=True)
    product_invoice = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='invoice_products', blank=True)
    invoice_product_quantity = models.PositiveIntegerField()
    invoice_product_cost_per_quantity = models.FloatField(default=0.0)
    invoice_product_total_cost = models.FloatField(default=0.0)
    invoice_product_cost_per_quantity_with_offer = models.FloatField(default=0.0)
    invoice_product_total_cost_with_gst = models.FloatField(default=0.0)
    invoice_product_total_cost_with_offer = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f'{self.invoice_product}'

class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    transaction_number = models.IntegerField()
    transaction_mode = models.CharField(max_length=30)
    transaction_amount = models.FloatField(default=0.0)
    transaction_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='transaction_by')
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, related_name='invoice_transaction')
    is_successful = models.BooleanField(blank=True)