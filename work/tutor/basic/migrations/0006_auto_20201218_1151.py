# Generated by Django 3.1.4 on 2020-12-18 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20201218_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_details',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basic.user'),
        ),
    ]