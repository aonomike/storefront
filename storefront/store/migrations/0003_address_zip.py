# Generated by Django 4.2.3 on 2023-07-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_add_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
