# Generated by Django 3.2.12 on 2022-08-19 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='book-images/84279_1646620000.webp', upload_to='book-images/'),
        ),
    ]
