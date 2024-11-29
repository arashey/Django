from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class Customuser(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=200)
    dateetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username
        
    def checkpassword(self, password):
        return check_password(password, self.password)

    def setpassword(self, plaintext_pass):
        self.password = make_password(plaintext_pass)