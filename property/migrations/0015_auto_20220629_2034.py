# Generated by Django 2.2.24 on 2022-06-29 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220629_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complained_flat', to='property.Flat', verbose_name='Квартира, на которую жаловаилсь'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaining_user', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]