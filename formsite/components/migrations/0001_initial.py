# Generated by Django 5.0.6 on 2024-06-10 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='null', max_length='300', null=True, upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('fps1080', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('fps1440', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('fps4k', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('AvgPower', models.IntegerField(default=0)),
                ('itemDescription', models.CharField(max_length=4000000)),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('cores', models.IntegerField()),
                ('clock_speed', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('threads', models.IntegerField(default=0)),
                ('avgTemp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('socket', models.CharField(max_length=80)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('avgTemp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('memory_size', models.IntegerField(default=0)),
                ('core_clock', models.IntegerField(default=0)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('formFactor', models.CharField(max_length=20)),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='PSU',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.component')),
                ('wattage', models.IntegerField(default=0)),
                ('modular', models.CharField(max_length=200)),
                ('efficiency_rating', models.CharField(max_length=280)),
                ('pstier', models.CharField(max_length=200)),
            ],
            bases=('components.component',),
        ),
    ]
