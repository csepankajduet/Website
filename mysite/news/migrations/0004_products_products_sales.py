# Generated by Django 3.0.2 on 2020-02-04 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200128_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('sales_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('total_sales', models.IntegerField()),
                ('app_user_id', models.CharField(max_length=200, null=True)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products_Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('total_quantity', models.IntegerField()),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=22)),
                ('app_user_id', models.CharField(max_length=200, null=True)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.Products')),
            ],
        ),
    ]
