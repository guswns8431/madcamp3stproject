# Generated by Django 3.0.2 on 2020-01-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FightTogether', '0003_incident_love_politics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('password', models.CharField(max_length=50, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
