# Generated by Django 5.1 on 2025-02-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manageoffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offershopname', models.CharField(max_length=100)),
                ('offershoplocation', models.CharField(max_length=100)),
                ('offercategory', models.CharField(max_length=50)),
                ('offertitle', models.CharField(max_length=50)),
                ('offerdescription', models.TextField(max_length=200)),
                ('offerstartdate', models.DateField()),
                ('offerenddate', models.DateField()),
            ],
        ),
    ]
