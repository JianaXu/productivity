# Generated by Django 2.2.1 on 2019-06-10 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0023_auto_20190604_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='curr_grp',
            new_name='grp_name',
        ),
    ]