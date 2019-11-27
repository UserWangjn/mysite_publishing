# Generated by Django 2.2.7 on 2019-11-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('publishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publishing')),
            ],
        ),
    ]
