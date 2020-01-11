# Generated by Django 3.0.2 on 2020-01-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FightTogether', '0002_blog_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('password', models.CharField(max_length=50, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('password', models.CharField(max_length=50, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('password', models.CharField(max_length=50, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
