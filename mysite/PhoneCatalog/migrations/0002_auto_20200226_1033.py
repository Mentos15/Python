# Generated by Django 3.0.3 on 2020-02-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneCatalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecatalog',
            name='RegDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]