# Generated by Django 5.0.6 on 2024-10-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_companyinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='certificate',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='logo',
            field=models.ImageField(upload_to='logo/'),
        ),
    ]