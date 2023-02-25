# Generated by Django 3.2.9 on 2023-02-24 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DostawaArmii',
            fields=[
                ('number', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('zb_98', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('zb_95', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('zb_on', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('zb_ontir', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('zb_lpg', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('zb_adblue', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=30, null=True)),
                ('dostawca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dost_armii', to='common.dostawcy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LicznikBazowyArmii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_DYS', models.PositiveSmallIntegerField()),
                ('ID_WAZ', models.PositiveSmallIntegerField()),
                ('SYMBOL', models.CharField(max_length=20)),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=30)),
                ('ARTYKUL', models.CharField(max_length=250, null=True)),
                ('KIEDY', models.CharField(max_length=150)),
                ('KIEDY_WGR', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LicznikDostawyArmii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_DYS', models.PositiveSmallIntegerField()),
                ('ID_WAZ', models.PositiveSmallIntegerField()),
                ('SYMBOL', models.CharField(max_length=20)),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=30)),
                ('ARTYKUL', models.CharField(max_length=250, null=True)),
                ('KIEDY', models.CharField(max_length=150)),
                ('KIEDY_WGR', models.DateTimeField(auto_now=True)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dost_licz_armii', to='armii.dostawaarmii')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
