# Generated by Django 2.2.1 on 2019-06-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0022_task_whs_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('IB', 'Inbound'), ('OB', 'Outbound'), ('INV', 'Inventory'), ('UN', 'Unspecified'), ('BK', 'Break')], default='UN', max_length=3),
        ),
    ]
