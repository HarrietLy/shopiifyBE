# Generated by Django 4.0.3 on 2022-03-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_price_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]