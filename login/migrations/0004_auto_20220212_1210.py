# Generated by Django 3.2.12 on 2022-02-12 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20220211_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prof_signup_form',
            old_name='Course_Offered_1',
            new_name='Offering_Courses',
        ),
        migrations.RenameField(
            model_name='student_signup_form',
            old_name='Subject_1',
            new_name='Subjects',
        ),
    ]
