# Generated by Django 4.2.4 on 2023-08-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='area',
            field=models.CharField(choices=[('Rural', 'Rural'), ('SemiUrban', 'Semiurban'), ('Urban', 'Urban')], max_length=15),
        ),
        migrations.AlterField(
            model_name='approval',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15),
        ),
        migrations.AlterField(
            model_name='approval',
            name='graduateeducation',
            field=models.CharField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_graduate')], max_length=15),
        ),
        migrations.AlterField(
            model_name='approval',
            name='married',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15),
        ),
        migrations.AlterField(
            model_name='approval',
            name='selfemployed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15),
        ),
    ]
