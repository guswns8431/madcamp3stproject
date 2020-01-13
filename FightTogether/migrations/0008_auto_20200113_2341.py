# Generated by Django 3.0.2 on 2020-01-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FightTogether', '0007_auto_20200113_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='like_posts1',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='FightTogether.Incident'),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_posts2',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='FightTogether.Love'),
        ),
        migrations.AddField(
            model_name='profile',
            name='like_posts3',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='FightTogether.Politics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='FightTogether.Blog'),
        ),
    ]
