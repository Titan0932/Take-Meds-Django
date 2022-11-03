
from django.db import models





class EnterMeds(models.Model):
    """ Medication name
    how many times a day => the time for each
    amount 
    how much much instore
    active or not   ?
        """
    uid=models.CharField(max_length=100, primary_key=True)
    medName=models.CharField(max_length=50, name='Medication')
    amount=models.IntegerField(name='Dosage')
    inStore=models.IntegerField(name='Number in Store')
    remarks=models.CharField(max_length=200, name='remarks')
    times=models.CharField(name='timings', max_length=400)

    active=models.BooleanField()

    def __str__(self):
        return self.medName

class EnterInfo(models.Model):

    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    fullname=models.CharField(max_length=100, name='fullname')
    username=models.CharField(max_length=20, name='username')
    password1=models.CharField(max_length=50, name='password1')
    email=models.EmailField(name='E-mail')
    Age=models.IntegerField(name='Age')
    Address=models.CharField(max_length=100, name='Address')
    Nationality= models.CharField(max_length=100,name='Nationality')
    phone=models.CharField(max_length=100, name='Phone Number')
    Gender=models.CharField(max_length=50, name='Gender')


    def __str__(self):
        return self.username