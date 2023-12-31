# Generated by Django 4.1.7 on 2023-10-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0012_participant_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bdm_one',
        ),
        migrations.RemoveField(
            model_name='group',
            name='bdm_two',
        ),
        migrations.AddField(
            model_name='group',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='winner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='finished_after',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='number_in_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='reward_in_after',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='wins_in_after',
            field=models.IntegerField(default=0),
        ),
    ]
