# Generated by Django 4.1.4 on 2023-02-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_skills', models.CharField(max_length=200)),
                ('min_cgpa', models.CharField(max_length=5)),
                ('exp_required', models.CharField(max_length=5)),
                ('required_cand_count', models.CharField(max_length=5)),
            ],
        ),
    ]
