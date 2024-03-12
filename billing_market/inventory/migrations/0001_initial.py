# Generated by Django 5.0.3 on 2024-03-12 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GST',
            fields=[
                ('gst_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hsn_code', models.CharField(blank=True, max_length=20)),
                ('cgst', models.FloatField(blank=True)),
                ('sgst', models.FloatField(blank=True)),
                ('igst', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('offer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(blank=True, max_length=30)),
                ('offer_description', models.TextField(blank=True)),
                ('offer_in_percentile', models.FloatField(blank=True)),
                ('offer_in_rupees', models.FloatField(blank=True)),
                ('offer_start_date', models.DateField(blank=True)),
                ('offer_end_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('product_cost_per_quantity', models.FloatField(default=0.0)),
                ('product_cost_with_gst', models.FloatField(default=0.0)),
                ('product_quantity', models.PositiveIntegerField(default=0)),
                ('product_total_cost', models.FloatField(default=0.0)),
                ('product_gst', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='gst_products', to='inventory.gst')),
                ('product_offers', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offer_products', to='inventory.offers')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.productcategory')),
            ],
        ),
    ]
