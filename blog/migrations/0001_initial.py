# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postear',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Texto', models.TextField()),
                ('Fecha_de_Creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('Fecha_de_Publicacion', models.DateTimeField(null=True, blank=True)),
                ('Autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
