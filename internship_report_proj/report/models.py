from django.db import models


class Intern(models.Model):
    name = models.CharField(max_length=100)
    joined_date = models.DateField()

    def __str__(self):
        return self.name


class WorkSubmission(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    date = models.DateField()
    worked_on = models.TextField()
    screenshot = models.ImageField(upload_to='screenshots/')

    def __str__(self):
        return f"Submission by {self.intern.name} on {self.date}"


from django.db import models

# Create your models here.
