from django.db import models


class Job(models.Model):
    JOB_STATUS_CHOICES = [
        ("idle", "Idle"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("stopped", "Stopped"),
        ("error", "Error"),
    ]

    weight_type = models.CharField(max_length=20, default="00")
    random_seed = models.IntegerField(default=0)
    num_of_tries = models.IntegerField(default=1000000)
    best_distance = models.CharField(max_length=255, default="NA")
    job_status = models.CharField(
        max_length=20, choices=JOB_STATUS_CHOICES, default="idle"
    )
    job_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.id} - {self.job_status}"
