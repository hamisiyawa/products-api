# Generated by Django 3.2.23 on 2023-11-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='profile.png', upload_to='media/'),
        ),
    ]