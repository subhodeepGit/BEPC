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
from bepc.bepc.notification.custom_notification import issue_notification_mail, issue_notification


def validate(self,method):
    data=frappe.get_all("Items Detail",{"parent":self.name},["item","manufactrurer","serial_no","description","oem_email_address","disabled"])
    for t in data:
        t["subject"]=self.subject
        t["state_"]=self.state_
        t["district_"]=self.district_
        t["block"]=self.block
        t["school"]=self.school
        t["district_collector"]=self.district_collector
        t["project_manager"]=self.project_manager
        t["school_name"]=self.school_name
        t["priority"]=self.priority
        t["issue_type"]=self.issue_type
        issue_notification_mail(t)
        # cron(self)
# def cron(self):
#     print("\n\n\nfirst data")
#     data=frappe.get_all("Items Detail",{"parent":self.name,"disabled":0},["item","manufactrurer","serial_no","description","oem_email_address","disabled"])
#     print(data)
#     for t in data:
#         t["subject"]=self.subject
#         t["state_"]=self.state_
#         t["district_"]=self.district_
#         t["block"]=self.block
#         t["school"]=self.school
#         t["customer_email"]=self.customer_email
#         t["project_manager"]=self.project_manager
#         t["school_name"]=self.school_name
#         t["priority"]=self.priority
#         t["issue_type"]=self.issue_type
#         issue_notification(t)
        