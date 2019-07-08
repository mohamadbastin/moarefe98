# Generated by Django 2.2.2 on 2019-07-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crewsignup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='boolean',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
