# Generated by Django 4.2.2 on 2023-06-27 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sales.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sales.status'),
            preserve_default=False,
        ),
    ]
