# Generated by Django 4.0.2 on 2022-03-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.URLField(max_length=100)),
                ('foundation', models.PositiveIntegerField()),
            ],
        ),
    ]
