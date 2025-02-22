# Generated by Django 5.0.7 on 2024-08-02 12:51

import django.db.models.deletion
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')
                ),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                (
                    'creator',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='person_clients',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')
                ),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                (
                    'creator',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='group_clients',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                ('people', models.ManyToManyField(related_name='groups', to='clients.person')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created',
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')
                ),
                (
                    'modified',
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')
                ),
                (
                    'group',
                    models.OneToOneField(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.group'
                    )
                ),
                (
                    'person',
                    models.OneToOneField(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.person'
                    )
                ),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
