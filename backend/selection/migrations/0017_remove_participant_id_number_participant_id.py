# Generated by Django 4.1.7 on 2023-11-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0016_alter_participant_id_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='id_number',
        ),
        migrations.AddField(
            model_name='participant',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
