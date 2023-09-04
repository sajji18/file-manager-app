# Generated by Django 4.2.3 on 2023-09-03 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iitr_drive', '0010_remove_folder_parent_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_folders', to='iitr_drive.folder'),
        ),
    ]
