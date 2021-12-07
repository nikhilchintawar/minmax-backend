# Generated by Django 3.2.8 on 2021-12-07 02:35

import ckeditor.fields
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', django_mysql.models.EnumField(choices=[('expense', 'expense'), ('income', 'income')])),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('summary', ckeditor.fields.RichTextField()),
                ('is_custom', models.BooleanField(db_index=True, default=True)),
            ],
            options={
                'verbose_name_plural': 'Generic Categories',
                'db_table': 'generic_categories',
            },
        ),
        migrations.AddIndex(
            model_name='genericcategory',
            index=models.Index(fields=['type'], name='generic_cat_type_e61b2a_idx'),
        ),
        migrations.AddConstraint(
            model_name='genericcategory',
            constraint=models.UniqueConstraint(fields=('name', 'type'), name='GenericCategory type-name unique together constraint'),
        ),
    ]
