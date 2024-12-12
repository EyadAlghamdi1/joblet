# Generated by Django 5.1.2 on 2024-12-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_organization_linkedin_organization_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='skills',
            field=models.ManyToManyField(null=True, to='organization.skill'),
        ),
    ]
