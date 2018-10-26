# Generated by Django 2.0 on 2018-10-25 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20181025_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundId',
            fields=[
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='webapp.Found')),
                ('person_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostId',
            fields=[
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='webapp.Lost')),
                ('person_id', models.CharField(max_length=200)),
            ],
        ),
    ]
