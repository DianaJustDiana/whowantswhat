# Generated by Django 2.0.5 on 2018-05-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dibcomment',
            name='comment',
            field=models.CharField(default="Here's a comment.", max_length=255),
            preserve_default=False,
        ),
    ]
