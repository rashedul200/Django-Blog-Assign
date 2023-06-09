# Generated by Django 4.1.7 on 2023-04-03 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_author_category_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['created'], 'verbose_name_plural': 'All Posts'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='catagory',
            new_name='category',
        ),
    ]
