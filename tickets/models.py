from django.db import models
from django.conf import settings


class Ticket(models.Model):

    class Priority(models.TextChoices):
        LOW = "LOW", "Low" # first is database value, second is display value
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    # title and description fileds
    title = models.CharField(max_length=200)
    description = models.TextField()

    # user assignee foreign key
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="assigned_tickets",
    )

    # user creator foreign key
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_tickets",
    )

    # time estimate field
    estimation = models.PositiveIntegerField()

    # ticket priority field
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
    )

    # which sprint does this ticket belong to, forein key
    sprint = models.ForeignKey(
        "sprints.Sprint",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tickets",
    )

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    priority__in=["LOW", "MEDIUM", "HIGH"] # ticket priority constraints
                ),
                name="valid_ticket_priority",
            ),
        ]

    def __str__(self):
        return self.title