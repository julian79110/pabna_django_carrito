# Generated by Django 5.0.1 on 2024-02-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEcommerce', '0008_alter_itemcarrito_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrito',
            name='cantidad',
            field=models.IntegerField(max_length=99),
        ),
    ]