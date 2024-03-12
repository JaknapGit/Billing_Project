# Generated by Django 5.0.3 on 2024-03-12 14:26

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('order_product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_product', models.CharField(max_length=30)),
                ('order_product_quantity', models.PositiveIntegerField()),
                ('order_product_cost_per_quantity', models.FloatField(blank=True)),
                ('order_product_total_cost', models.FloatField(blank=True)),
                ('order_product_total_cost_with_gst', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(blank=True, max_length=30)),
                ('vendor_information', models.TextField()),
                ('vendor_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('vendor_email', models.EmailField(blank=True, max_length=254)),
                ('vendor_gst_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('order_total_cost_without_gst', models.FloatField(default=0.0)),
                ('order_total_cost_with_gst', models.FloatField(default=0.0)),
                ('order_status', models.CharField(default='pending', max_length=20)),
                ('order_delivery_date', models.DateField(blank=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.vendor')),
            ],
        ),
    ]
