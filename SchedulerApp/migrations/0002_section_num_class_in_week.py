from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchedulerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='num_class_in_week',
            field=models.IntegerField(default=0),
        ),
    ]
