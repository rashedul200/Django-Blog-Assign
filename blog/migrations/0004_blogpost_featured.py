# Generated by Django 4.1.7 on 2023-03-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]