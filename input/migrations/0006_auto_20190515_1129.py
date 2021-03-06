# Generated by Django 2.1.1 on 2019-05-15 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_auto_20190515_1104'),
    ]

    operations = [
    
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='task',
        ),
        migrations.AddField(
            model_name='post',
            name='wms_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
