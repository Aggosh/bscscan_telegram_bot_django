# Generated by Django 4.2.5 on 2023-09-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bscscan", "0003_alter_transaction_block_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="block_number",
            field=models.BigIntegerField(unique=True),
        ),
    ]