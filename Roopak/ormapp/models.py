from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Loanid=models.IntegerField(primary_key=True);
    Name=models.CharField(max_length=100);
    Age=models.IntegerField(default=18);
    Gender=models.CharField(max_length=1, default='M');
    City=models.CharField(max_length=20, default='Chennai');
    Accountno=models.IntegerField();
    Salary=models.IntegerField();
    Loanamt=models.IntegerField();

class BankloanAdmin(admin.ModelAdmin):
    list_display=('Loanid','Name','Age','Gender','City','Accountno','Salary','Loanamt')