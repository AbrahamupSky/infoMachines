# Generated by Django 4.2.2 on 2023-09-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0004_alter_machines_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]