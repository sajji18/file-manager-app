# Generated by Django 4.2.3 on 2023-09-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iitr_drive', '0004_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='iitr_drive.folder'),
            preserve_default=False,
        ),
    ]
