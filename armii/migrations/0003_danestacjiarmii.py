# Generated by Django 3.2.9 on 2023-03-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armii', '0002_dostawaarmii_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaneStacjiArmii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skr_nazwa', models.CharField(max_length=100)),
                ('nazwa', models.CharField(max_length=250)),
                ('adrres', models.CharField(max_length=250)),
                ('adress_email', models.EmailField(default='slawomirwitek@watkem.pl', max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
