# Generated by Django 5.0.7 on 2024-07-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='ends_at',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='starts_at',
            new_name='start',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
    ]
