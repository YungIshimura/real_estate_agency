# Generated by Django 2.2.24 on 2022-06-27 10:36

from django.db import migrations
import phonenumbers


def normalization_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber):
            normalize_phonenumber = phonenumbers.format_number(
                phonenumber, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_pure_phone = normalize_phonenumber
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20220627_1211'),
    ]

    operations = [
        migrations.RunPython(normalization_phonenumber),
    ]
