# Generated by Django 2.0.5 on 2020-04-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20180516_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='hosting',
            field=models.CharField(choices=[('local', 'Local'), ('spaces', 'Spaces')], default='local', max_length=8),
        ),
    ]
