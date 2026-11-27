from django.db import models
from django.conf import settings


class Sprint(models.Model):

    #TODO some fields are missing

    # name and description fields
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # start and end date for a sprint, fields
    start_date = models.DateField()
    end_date = models.DateField()

    # which user created this sprint, foreign key
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_sprints",
    )

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name