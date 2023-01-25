from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .forms import Account_Register,Contact_Register
from .models import Accounts,Contact
from django.contrib import messages

# Create your views here.

# home page 
def home(request):
    return render(request,'myapp/base.html')



# show aacount data
def account_list(request):
        context = Accounts.objects.all()
        return render(request,'myapp/accountlist.html',{'con':context})

# create and insert account data 
def add_show(request):
    if request.method=='POST':
        ad=Account_Register(request.POST)
        if ad.is_valid():
            cnm=ad.cleaned_data['client_name']
            accs=ad.cleaned_data['account_status']
            ind=ad.cleaned_data['industry']
            acco=ad.cleaned_data['account_owner']
            result=Accounts(client_name=cnm,account_status=accs,industry=ind,account_owner=acco)
            result.save()
            ad=Account_Register()
            messages.success(request, 'Record Successfully inserted ')
            # return redirect('/list/')
    else:
        ad=Account_Register()
    return render(request,'myapp/account.html',{'AD':ad})

# delete account data
def account_delete(request,id):
     if request.method=='POST':
        pi= Accounts.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/list/')

# update account data
def update_account(request,id):
    if request.method=="POST":
        Adt=Accounts.objects.get(pk=id)
        result=Account_Register(request.POST,instance=Adt)
        if result.is_valid():
            result.save()
            result=Account_Register()
    else:
        Adt=Accounts.objects.get(pk=id)
        result=Account_Register(instance=Adt)
    return render(request,'myapp/account_update.html',{'au':result})

# show contact data
def contact_list(request):
    context1 =Contact.objects.all()
    return render(request,'myapp/contactlist.html',{'con1':context1})

#delete contact data
def contact_delete(request,id):
     if request.method=='POST':
        pi= Contact.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/Clist/')



#update contact data
def update_contact(request,id):
    if request.method=="POST":
        Adt=Contact.objects.get(pk=id)
        result=Contact_Register(request.POST,instance=Adt)
        if result.is_valid():
            result.save()
            result=Contact_Register()
    else:
        Adt=Contact.objects.get(pk=id)
        result=Contact_Register(instance=Adt)
    return render(request,'myapp/update_contact.html',{'cu':result})

# insert create contact data
def add_show_contact(request):
    if request.method=='POST':
        cd=Contact_Register(request.POST)
        if cd.is_valid():
            cn=cd.cleaned_data['contact_name']
            cc=cd.cleaned_data['contact_cidn']
            cp=cd.cleaned_data['contact_price']
            cphone=cd.cleaned_data['contact_phone']
            ce=cd.cleaned_data['contact_email']
            ca=cd.cleaned_data['account']
            result1=Contact(contact_name=cn,contact_cidn=cc,contact_price=cp,contact_phone=cphone,contact_email=ce,account=ca)
            result1.save()
            cd=Contact_Register()
            # return redirect('Clist')

        # context={'list':Accounts.object.all()}

    else: 
        cd=Contact_Register()
    return render(request,'myapp/contact.html',{"CD":cd})    
        





