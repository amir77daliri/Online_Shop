# Generated by Django 4.0 on 2024-06-15 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_sub_category_alter_category_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='parent_category',
        ),
    ]
