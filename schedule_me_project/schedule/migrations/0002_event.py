# Generated by Django 3.2.2 on 2021-05-22 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(choices=[('0', '12 AM'), ('1', '1 AM'), ('2', '2 AM'), ('3', '3 AM'), ('4', '4 AM'), ('5', '5 AM'), ('6', '6 AM'), ('7', '7 AM'), ('8', '8 AM'), ('9', '9 AM'), ('10', '10 AM'), ('11', '11 AM'), ('12', '12 PM'), ('13', '1 PM'), ('14', '2 PM'), ('15', '3 PM'), ('16', '4 PM'), ('17', '5 PM'), ('18', '6 PM'), ('19', '7 PM'), ('20', '8 PM'), ('21', '9 PM'), ('22', '10 PM'), ('23', '11 PM'), ('24', '12 AM')], max_length=5)),
                ('day', models.CharField(choices=[('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], max_length=9)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]