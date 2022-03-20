# Generated by Django 4.0.3 on 2022-03-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_doctor_degree_alter_doctor_job_alter_doctor_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Nonbinary'), ('O', 'Other')], default='M', max_length=1, null=True),
        ),
    ]