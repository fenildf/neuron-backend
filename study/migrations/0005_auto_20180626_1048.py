# Generated by Django 2.0.6 on 2018-06-26 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20180621_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryrecord',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_records', to='bank.Entry'),
        ),
        migrations.AlterField(
            model_name='entryrecord',
            name='proficiency',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='entryrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
