from django.db import models
from django.contrib.auth.models import User

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
  completed = models.BooleanField(default = False, blank = True)
  updated = models.DateTimeField(auto_now = True, blank = True)
  user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

  def __str__(self):
        return self.firstname