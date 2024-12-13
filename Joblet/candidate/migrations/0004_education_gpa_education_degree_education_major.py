# Generated by Django 5.1.2 on 2024-12-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_alter_project_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='GPA',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('HIGH_SCHOOL', 'High School'), ('ASSOCIATE', 'Associate Degree'), ('BACHELOR', "Bachelor's Degree"), ('MASTER', "Master's Degree"), ('PHD', 'Doctorate/PhD'), ('DIPLOMA', 'Diploma'), ('CERTIFICATION', 'Certification'), ('OTHER', 'Other')], default='Other', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.CharField(default='none', max_length=100),
        ),
    ]