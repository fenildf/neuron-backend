# Generated by Django 2.0.6 on 2018-06-26 17:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('word', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('rank', models.SmallIntegerField(default=None, null=True)),
                ('definitions', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('pronounce', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='new repo', max_length=50, unique=True)),
                ('entries', models.ManyToManyField(related_name='repos', to='bank.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.TextField()),
                ('chinese', models.TextField()),
                ('reference', models.TextField(default='')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='bank.Entry')),
            ],
        ),
    ]
