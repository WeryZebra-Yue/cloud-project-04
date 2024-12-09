# Generated by Django 5.0.6 on 2024-12-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_job_delete_jobstatus"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="num_of_batch_jobs",
        ),
        migrations.AlterField(
            model_name="job",
            name="job_status",
            field=models.CharField(
                choices=[
                    ("idle", "Idle"),
                    ("running", "Running"),
                    ("completed", "Completed"),
                    ("stopped", "Stopped"),
                    ("error", "Error"),
                ],
                default="idle",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="weight_type",
            field=models.CharField(default="00", max_length=20),
        ),
    ]
