# Generated by Django 3.1.1 on 2020-12-01 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_category_invoice_listing_review_thumbsup_watch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='highestBidder',
        ),
    ]
