# Generated for Django 5.2
from django.db import models, migrations
import django_encrypted_json.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('json', django_encrypted_json.fields.EncryptedValueJsonField(default={})),
                ('optional_json', django_encrypted_json.fields.EncryptedValueJsonField(null=True, blank=True)),
            ],
        ),
    ]
