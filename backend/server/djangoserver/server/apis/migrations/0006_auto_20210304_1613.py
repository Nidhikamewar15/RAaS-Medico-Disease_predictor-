# Generated by Django 3.1.7 on 2021-03-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_files_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartdisease',
            name='prediction',
            field=models.IntegerField(null=True),
        ),
    ]
