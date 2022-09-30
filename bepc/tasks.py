# from msilib.schema import tables
from bepcsupport.support.doctype.issue.issue import Issue
import frappe
import string
import random
from frappe.utils.data import getdate
from frappe.utils import nowdate, now_datetime
from datetime import datetime
def all():
    pass

def cron():
    for data in frappe.db.get_all("Items Detail",{"disabled":0},['name','oem_email_address']):
        oem_email_address=data["oem_email_address"]
        items_detail_info=frappe.get_all("Items Detail",{'parenttype':"Issue",'oem_email_address':oem_email_address,'disabled':0},
                                                        ['item','manufactrurer','serial_no','oem_email_address','parenttype','parent'])
        issue_parent_name=[]
        for t in items_detail_info:
            issue_parent_name.append(t['parent'])
        if len(issue_parent_name)==1:    
            issue_info=frappe.get_all("Issue",filters=[["name","=",issue_parent_name[0]]],fields=['name','school','school_name','district','block','resolution_by','sla_status','project_manager','district_collector'])
            
        else:
            issue_info=frappe.get_all("Issue",filters=[["name","in",tuple(issue_parent_name)]],fields=['name','school','school_name','district','block','resolution_by','sla_status','project_manager','district_collector'])
           
           

        for t in issue_info:
            print(type(t["resolution_by"]))
            print(t["resolution_by"]) 
            print(type(nowdate()))
            if t["resolution_by"] >= datetime.strptime(nowdate(),'%Y-%m-%d').date():

                t["sla_status"]="Within SLA"
              

                sub="""Issue Reminder"""
                msg="""<b>---------------------Issue Details---------------------</b><br>"""

                msg+= """</u></b></p><table class='table table-bordered'><tr>
                    <th>Issue</th><th>District</th><th>Block</th><th>School</th><th>School Name</th><th>Item</th><th>Manufactrurer</th><th>Serial No</th><th>Due Date</th><th>Status</th>"""    
                for res1 in items_detail_info:
                    for t in issue_info:
                        if t["name"]==res1["parent"]:
                            msg += "<tr><td>" + """{0}""".format(str(t.get('name'))) + "</td><td>" + str(t.get('district')) + "</td><td>" + str(t.get('block'))  + "</td><td>" + str(t.get('school')) + "</td><td>" + str(t.get('school_name')) + "</td><td>" + str(res1.get('item'))  + "</td><td>" + str(res1.get('manufactrurer')) + "</td><td>" + str(res1.get('serial_no')) + "</td><td>" + str(t.get('resolution_by'))  + "</td><td>" + str(t.get('sla_status'))  + "</td></tr>"
                msg += "</table>"
                send_mail([oem_email_address],sub,msg)  
            else:
                t["sla_status"]="Over SLA"
                cc=t["project_manager"]
                print(cc)
                sub="""Issue Reminder"""
                # cc="tousiff.taj@soulunileaders.com"
                


                msg="""<b>---------------------Issue Details---------------------</b><br>"""

                msg+= """</u></b></p><table class='table table-bordered'><tr>
                    <th>Issue</th><th>District</th><th>Block</th><th>School</th><th>School Name</th><th>Item</th><th>Manufactrurer</th><th>Serial No</th><th>Due Date</th><th>Status</th>"""    
                for res1 in items_detail_info:
                    for t in issue_info:
                        if t["name"]==res1["parent"]:

                            msg += "<tr><td>" + """{0}""".format(str(t.get('name'))) + "</td><td>" + str(t.get('district')) + "</td><td>" + str(t.get('block'))  + "</td><td>" + str(t.get('school')) + "</td><td>" + str(t.get('school_name')) + "</td><td>" + str(res1.get('item'))  + "</td><td>" + str(res1.get('manufactrurer')) + "</td><td>" + str(res1.get('serial_no')) + "</td><td>" + str(t.get('resolution_by'))  + "</td><td>" + str(t.get('sla_status'))  + "</td></tr>"
                msg += "</table>"

                send_mail_cc([oem_email_address],[cc],sub,msg)    
# <td>" + str(res1.get('sla_status')) + "</td>
def send_mail(recipients,subject,message):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients,subject=subject,message=message,with_container=True)
def send_mail_cc(recipients=None,cc=None,subject=None,message=None):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients or [],cc=cc or [],expose_recipients="header",subject=subject,message = message,with_container=True)
def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
       return "true"
    return ""

