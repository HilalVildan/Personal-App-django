# Generated by Django 4.1.5 on 2023-01-16 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='department',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='personnel.department'),
        ),
    ]
