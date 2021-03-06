# Generated by Django 3.2 on 2021-04-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210414_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='middle_name',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.role'),
        ),
    ]
