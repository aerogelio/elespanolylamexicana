# Generated by Django 3.0.2 on 2020-01-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elespanolylamexicanaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]