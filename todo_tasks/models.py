from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Task(models.Model):
    user= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    task= models.CharField(default="", max_length=100)
    details= models.TextField(blank= True, null=True, default="")
    date= models.DateTimeField(blank= True, null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{self.task}, {self.user}"

# class Job(models.Model):
#     user= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     task= models.CharField(default="", max_length=100)
#     details= models.TextField(blank= True, null=True, default="")
#     date= models.DateTimeField(blank= True, null=True, auto_now=False, auto_now_add=False)

#     def __str__(self):
#         return self.task