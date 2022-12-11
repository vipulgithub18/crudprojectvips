from django.db import models

# Create your models here.
class Account_status(models.Model):
    account_name=models.CharField(max_length=100)
    def __str__(self):
        return self.account_name
    
class Industry(models.Model):
    industry_name=models.CharField(max_length=100)
    def __str__(self):
        return self.industry_name

class Accounts(models.Model):
    client_name=models.CharField(max_length=100)
    account_status=models.ForeignKey(Account_status,on_delete=models.CASCADE)
    industry=models.ForeignKey(Industry,on_delete=models.CASCADE)
    account_owner=models.CharField(max_length=90)

    def __str__(self):
        return self.client_name
        
class Contact(models.Model):
    contact_name=models.CharField(max_length=99)
    contact_cidn=models.IntegerField()
    contact_price=models.FloatField()
    contact_phone=models.IntegerField()
    contact_email=models.EmailField(max_length=99)
    account=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    