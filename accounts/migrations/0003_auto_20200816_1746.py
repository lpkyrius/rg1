# Generated by Django 3.1 on 2020-08-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pending'), ('Saiu para entrega', 'Saiu para entrega'), ('Entregue', 'Entregue')], max_length=200, null=True),
        ),
    ]
