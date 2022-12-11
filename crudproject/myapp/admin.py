from django.contrib import admin
from .models import Account_status,Accounts,Contact,Industry
# Register your models here.
@admin.register(Account_status)
class Account_statusAdmin(admin.ModelAdmin):
    list_display=('account_name',)

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display=('industry_name',)

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display=('client_name','account_status','industry','account_owner')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('contact_name','contact_cidn','contact_price','contact_phone','contact_email','account')

