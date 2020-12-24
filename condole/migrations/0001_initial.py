# Generated by Django 3.1.4 on 2020-12-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('relationship_with_deceased', models.CharField(max_length=50, null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
