# Generated by Django 5.0.6 on 2024-10-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('history', models.TextField()),
                ('details', models.TextField()),
                ('certificate', models.TextField()),
            ],
        ),
    ]