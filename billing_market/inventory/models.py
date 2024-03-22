from django.db import models

class Offers(models.Model):
    offer_id = models.BigAutoField(primary_key=True)
    offer_name = models.CharField(max_length=30, blank=True)
    offer_description = models.TextField(blank=True)
    offer_in_percentile = models.FloatField(blank=True)
    offer_in_rupees = models.FloatField(blank=True)
    offer_start_date = models.DateField(blank=True)
    offer_end_date = models.DateField(blank=True)


class GST(models.Model):
    gst_id = models.BigAutoField(primary_key=True)
    hsn_code = models.CharField(max_length=20, blank=True)
    cgst = models.FloatField(blank=True)
    sgst = models.FloatField(blank=True)
    igst = models.FloatField(blank=True)

    def __str__(self) -> str:
        return f'{self.hsn_code}'
    
class ProductCategory(models.Model):
    product_category_id = models.BigAutoField(primary_key=True)
    product_category_name = models.CharField(max_length=30, blank=True)

    def __str__(self) -> str:
        return f'{self.product_category_name}'
    
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(unique=True, max_length=30)
    product_cost_per_quantity = models.FloatField(default= 0.0)
    product_cost_with_gst = models.FloatField(default=0.0)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    product_offers = models.ForeignKey(Offers, on_delete=models.DO_NOTHING, related_name='offer_products', blank=True)
    product_quantity = models.PositiveIntegerField(default=0)
    product_total_cost = models.FloatField(default=0.0)
    product_gst = models.ForeignKey(GST, on_delete=models.CASCADE, related_name='gst_products', blank=True)    

    def __str__(self) -> str:
        return f'{self.product_name}'
