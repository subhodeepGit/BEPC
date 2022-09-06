from bepc.support.doctype.issue.issue import Issue
import frappe
import string
import random

def all():
    pass

def cron():

    msg="""<b>Reminder,</b><br>"""
    msg+="""<p>Issue Pending </p><br>"""
    data=frappe.get_all("Items Detail",{"parenttype":"Issue","disabled":0},["oem_email_address","parent"])
    recipient=[]
    for t in data:
        recipient.append(t.oem_email_address)
        if len(recipient)!=0:
                    send_mail(recipient,'Reminder',msg)


def send_mail(recipients,subject,message):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients,subject=subject,message=message,with_container=True)

def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
       return "true"
    return ""