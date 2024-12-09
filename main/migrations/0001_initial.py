# Generated by Django 5.1.3 on 2024-12-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_type', models.CharField(default='00', max_length=2)),
                ('random_seed', models.IntegerField(default=0)),
                ('num_of_trys', models.IntegerField(default=1000000)),
                ('num_of_batch_jobs', models.IntegerField(default=1)),
                ('best_distance', models.CharField(default='NA', max_length=20)),
                ('job_status', models.CharField(default='none submitted', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]