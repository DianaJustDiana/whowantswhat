# Generated by Django 2.0.5 on 2018-05-12 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_groups', '0002_auto_20180512_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]