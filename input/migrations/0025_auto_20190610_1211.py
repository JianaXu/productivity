# Generated by Django 2.2.1 on 2019-06-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0024_auto_20190610_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='whs_id',
            field=models.CharField(choices=[('MYL', 'MYL'), ('THA', 'THA'), ('VNN', 'VNN'), ('VNW', 'VNW'), ('IDG', 'IDG'), ('PHL', 'PHL')], default='UN', max_length=3),
        ),
    ]