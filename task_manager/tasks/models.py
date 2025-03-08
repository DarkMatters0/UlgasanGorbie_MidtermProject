from django.db import models
from datetime import date

class Task(models.Model):
    title = models.CharField(max_length=100)  # Required
    description = models.TextField(blank=True, null=True)  # Optional
    due_date = models.DateField()  # Required
    status = models.CharField(max_length=20, editable=False)  # Auto-set based on due_date

    def save(self):
        # Set status based on due_date
        if self.due_date < date.today():
            self.status = "Overdue"
        else:
            self.status = "Pending"
        
        models.Model.save(self)  # Save the object to the database

    def __str__(self):
        return self.title
