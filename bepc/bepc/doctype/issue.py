import json
from datetime import datetime, timedelta
# from bepc.tasks import has_default_email_acc
# from bepc.tasks import has_default_email_acc
import frappe
from re import L
from frappe.utils.data import format_date
from frappe.utils import get_url_to_form
from frappe.utils import cint, cstr, parse_addr
from frappe import _
from frappe.core.utils import get_parent_doc
from frappe.email.inbox import link_communication_to_document
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from bepc.bepc.notification.custom_notification import issue_notification_mail, internal_mail
from frappe.utils.data import getdate
from frappe.utils import nowdate, now_datetime

def validate(self,method):
    print("\n\n")
    print(self.name)
    if self.issue_type=="External":
        external_mail(self)
    elif self.issue_type=="Internal":
        internal_mail(self)
            

def before_save(self,method):
    pass
    # print("\n\n\n\n\n")
    # print(self.get("items_detail"))
    # for t in self.get("items_detail"):
    #     print(t.disabled) 
    #     print(t.modified)
    #     print(t.creation)
        
def external_mail(self):
    for t in self.get("items_detail"):
        data={}
        if t.disabled==0:
            data["item"]=t.item
            data["manufactrurer"]=t.manufactrurer
            data["serial_no"]=t.serial_no
            data["description"]=t.description
            data["disabled"]=t.disabled
            data["oem_email_address"]=t.oem_email_address
            data["subject"]=self.subject
            data["state_"]=self.state_
            data["district_"]=self.district_
            data["block"]=self.block
            data["school"]=self.school
            data["school_address"]=self.school_address
            data["school_contact_no"]=self.school_contact_no
            data["district_collector"]=self.district_collector
            data["project_manager"]=self.project_manager
            data["school_name"]=self.school_name
            data["priority"]=self.priority
            data["issue_type"]=self.issue_type
            data["helpdesk_email"]=self.helpdesk_email
            issue_notification_mail(data)



    # data=frappe.get_all("Items Detail",filters=[["parent","=",self.name],["disabled","=",0]],fields=["item","manufactrurer","serial_no","description","oem_email_address","disabled"])
    # print("\n\n\n\n\n")
    # print(data)
    # for t in data:
    #     t["subject"]=self.subject
    #     t["state_"]=self.state_
    #     t["district_"]=self.district_
    #     t["block"]=self.block
    #     t["school"]=self.school
    #     t["school_address"]=self.school_address
    #     t["school_contact_no"]=self.school_contact_no
    #     t["district_collector"]=self.district_collector
    #     t["project_manager"]=self.project_manager
    #     t["school_name"]=self.school_name
    #     t["priority"]=self.priority
    #     t["issue_type"]=self.issue_type
    #     issue_notification_mail(t)


# @frappe.whitelist()
# def mail(doc,name=None):
#     print("\n\n\n\nTaking Data")
#     data=frappe.get_all("Items Detail",{"parent":name},["item","manufactrurer","serial_no","description","oem_email_address","disabled"])
#     print("\n\n\ndata")
#     print(data)
#     for t in data:

#         t["subject"]=doc.subject
#         t["state_"]=doc.state_
#         t["district_"]=doc.district_
#         t["block"]=doc.block
#         t["school"]=doc.school
#         t["school_address"]=doc.school_address
#         t["school_contact_no"]=doc.school_contact_no
#         t["district_collector"]=doc.district_collector
#         t["project_manager"]=doc.project_manager
#         t["school_name"]=doc.school_name
#         t["priority"]=doc.priority
#         t["issue_type"]=doc.issue_type
#         issue_notification_mail(t)


               