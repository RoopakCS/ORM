# Generated by Django 5.1.1 on 2024-09-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('Loanid', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Accountno', models.IntegerField()),
                ('Salary', models.IntegerField()),
                ('Loanamt', models.IntegerField()),
            ],
        ),
    ]
