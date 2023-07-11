# Generated by Django 4.2.2 on 2023-06-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0002_auto_20230620_1745"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="teacher",
        ),
        migrations.AddField(
            model_name="student",
            name="teachers",
            field=models.ManyToManyField(related_name="students", to="school.teacher"),
        ),
        migrations.AlterField(
            model_name="student",
            name="group",
            field=models.CharField(max_length=10, verbose_name="Класс"),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.CharField(max_length=10, verbose_name="Предмет"),
        ),
    ]