# Generated by Django 5.1 on 2024-08-09 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='tipo'),
        ),
    ]
