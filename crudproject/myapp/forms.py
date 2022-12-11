from django import forms
from .models import Accounts,Contact

class Account_Register(forms.ModelForm):
    client_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name'}))
    account_owner=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Created By'}))
    class Meta:
        model=Accounts
        fields=['client_name','account_status','industry','account_owner']

        labels ={
            'client_name':'Client Name',
            'account_status':'Account Status',
            'industry':'Industry',
            'account_owner':'Account Owner',
        }


    def __init__(self,*args,**kwargs):
        super(Account_Register,self).__init__(*args,**kwargs)
        self.fields['account_status'].empty_label='select'
        self.fields['industry'].empty_label='select'



class Contact_Register(forms.ModelForm):
    contact_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name'}))
    contact_cidn=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter CIDN'}))
    contact_price=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Price'}))
    contact_phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Phone Number'}))
    contact_email=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
    class Meta:
        model =Contact
        fields =['contact_name','contact_cidn','contact_price','contact_phone','contact_email','account']
        labels ={
            'contact_name':'Name',
            'contact_cidn':'CIDN',
            'contact_price':'Price',
            'contact_phone':' Phone',
            'contact_email':' Email',
            'account':'Account',
        }

    def __init__(self,*args,**kwargs):
        super(Contact_Register,self).__init__(*args,**kwargs)
        self.fields['account'].empty_label='select'
        
