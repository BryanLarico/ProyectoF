# Generated by Django 5.0.6 on 2024-07-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='year',
            new_name='semester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='idTeacher',
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisite',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='hoursPractice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='hoursTeory',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='laboratory',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='nameCourse',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
