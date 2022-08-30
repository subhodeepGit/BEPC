import frappe
from re import L
from frappe.utils.data import format_date
from frappe.utils import get_url_to_form
from frappe.utils import cint, cstr, parse_addr


def send_mail(recipients=None,cc=None,subject=None,message=None):
    if has_default_email_acc():
        frappe.sendmail(recipients=recipients or [],cc=cc or [],expose_recipients="header",subject=subject,message = message,with_container=True)

def has_default_email_acc():
    for d in frappe.get_all("Email Account", {"default_outgoing":1}):
       return "true"
    return ""

def issue_notification_mail(doc):
    # {'item': '08b50badef', 'manufactrurer': 'HP Company', 'serial_no': 'SL-HP-01', 'description': 'sadsfa', 'oem_email_address': 'tousiff.taj@soulunileaders.com', 'disabled': 0}
    sub="""<p><b>Issue Ticket</b></p><br>"""
    cc=doc["district_collector"],doc["project_manager"]
    msg="""<b>---------------------Issue Details---------------------</b><br>"""
    msg+="""<b>Subject:</b>  {0}<br>""".format(doc["subject"])
    msg+="""<b>State:</b>  {0}<br>""".format(doc["state_"])
    msg+="""<b>District:</b>  {0}<br>""".format(doc["district_"])
    msg+="""<b>Block:</b>  {0}<br>""".format(doc["block"])
    msg+="""<b>School Id:</b>  {0}<br>""".format(doc["school"])
    msg+="""<b>School Name:</b>  {0}<br>""".format(doc["school_name"])
    msg+="""<b>Manufacturer:</b>  {0}<br>""".format(doc['manufactrurer'])
    msg+="""<b>Seriel No:</b>  {0}<br>""".format(doc['serial_no'])
    msg+="""<b>Description:</b>  {0}<br>""".format(doc['description'])
    msg+="""<b>Issue Type:</b>  {0}<br>""".format(doc['issue_type'])
    msg+="""<b>Priority:</b>  {0}<br>""".format(doc['priority'])
    send_mail([doc['oem_email_address']],cc,'New Issue',msg)

def issue_notification(doc):
    # {'item': '08b50badef', 'manufactrurer': 'HP Company', 'serial_no': 'SL-HP-01', 'description': 'sadsfa', 'oem_email_address': 'tousiff.taj@soulunileaders.com', 'disabled': 0}
    sub="""Issue Reminder"""
    cc=doc["district_collector"],doc["project_manager"]
    msg="""<b>---------------------Issue Details---------------------</b><br>"""
    msg+="""<b>Subject:</b>  {0}<br>""".format(doc["subject"])
    msg+="""<b>State:</b>  {0}<br>""".format(doc["state_"])
    msg+="""<b>District:</b>  {0}<br>""".format(doc["district_"])
    msg+="""<b>Block:</b>  {0}<br>""".format(doc["block"])
    msg+="""<b>School Id:</b>  {0}<br>""".format(doc["school"])
    msg+="""<b>School Name:</b>  {0}<br>""".format(doc["school_name"])
    msg+="""<b>Manufacturer:</b>  {0}<br>""".format(doc['manufactrurer'])
    msg+="""<b>Seriel No:</b>  {0}<br>""".format(doc['serial_no'])
    msg+="""<b>Description:</b>  {0}<br>""".format(doc['description'])
    msg+="""<b>Issue Type:</b>  {0}<br>""".format(doc['issue_type'])
    msg+="""<b>Priority:</b>  {0}<br>""".format(doc['priority'])
    send_mail([doc['oem_email_address']],cc,sub,msg)


# def issue_notification(doc):
#     # {'item': '08b50badef', 'manufactrurer': 'HP Company', 'serial_no': 'SL-HP-01', 'description': 'sadsfa', 'oem_email_address': 'tousiff.taj@soulunileaders.com', 'disabled': 0}
#     # cc=doc["customer_email"]
#     sub="""<p><b>Issue Ticket</b></p><br>"""
#     cc=doc["customer_email"]
#     msg="""<b>---------------------Issue Details---------------------</b><br>"""
#     msg+="""<b>Subject:</b>  {0}<br>""".format(doc["subject"])
#     msg+="""<b>State:</b>  {0}<br>""".format(doc["state_"])
#     msg+="""<b>District:</b>  {0}<br>""".format(doc["district_"])
#     msg+="""<b>Block:</b>  {0}<br>""".format(doc["block"])
#     msg+="""<b>School Name:</b>  {0}<br>""".format(doc["school"])
    # send_mail([doc['oem_customer_emailemail_address']],'New Issue',msg,cc)
    # send_mail([doc['oem_email_address'],doc["customer_email"]],'New Issue',msg)
    # msg+= """</u></b></p><table class='table table-bordered'><tr>
    #     <th>Issue</th>"""
    # for d in doc.get("items_detail"):
    #     msg += """<tr><td>{0}</td></tr>""".format(str(d.get('item'))) 
    # msg += "</table>"
    # send_mail(frappe.db.get_value("Test Item",doc.get('name'),"email_id"),sub,msg)
    # send_mail(frappe.db.get_value("Issue",doc.get('name'),"customer_email"),'Application status',msg)


