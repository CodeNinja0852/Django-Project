# Generated by Django 5.0.4 on 2024-04-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_customer_username_orderdetail_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='stripe_payment_intent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
