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
    sub="Complaint Lodged for {0} on {1}".format(doc["item"],doc["opening_date"])
    cc=doc["district_collector"],doc["project_manager"]
    msg="""<b>---------------------Issue Details---------------------</b><br>"""
    msg+="""<b>State:</b>  {0}<br>""".format(doc["state"])
    msg+="""<b>District:</b>  {0}<br>""".format(doc["district"])
    msg+="""<b>Block:</b>  {0}<br>""".format(doc["block"])
    msg+="""<b>School Id:</b>  {0}<br>""".format(doc["school"])
    msg+="""<b>School Name:</b>  {0}<br>""".format(doc["school_name"])
    msg+="""<b>School Address:</b>  {0}<br>""".format(doc["school_address"])
    msg+="""<b>School Contact:</b>  {0}<br>""".format(doc["school_contact_no"])
    msg+="""<b>Item Name:</b>  {0}<br>""".format(doc['item'])
    msg+="""<b>Manufacturer:</b>  {0}<br>""".format(doc['manufactrurer'])
    msg+="""<b>Serial No:</b>  {0}<br>""".format(doc['serial_no'])
    msg+="""<b>Description:</b>  {0}<br>""".format(doc['description'])
    msg+="""<b>Issue Type:</b>  {0}<br>""".format(doc['issue_type'])
    msg+="""<b>Priority:</b>  {0}<br>""".format(doc['priority'])
    send_mail([doc['oem_email_address']],cc,sub,msg)

def internal_mail(doc):
    # {'item': '08b50badef', 'manufactrurer': 'HP Company', 'serial_no': 'SL-HP-01', 'description': 'sadsfa', 'oem_email_address': 'tousiff.taj@soulunileaders.com', 'disabled': 0}
    sub = "New Issue"
    # recipients="helpdesk@gmail.com"
    cc="tousiff.taj@soulunileaders.com"
    msg="""<p>--------Issue Details----------</p>"""
    msg+="""<p>State : {0}</p>""".format(doc.state_)
    msg+="""<p>District:{0}</p>""".format(doc.district_)
    msg+="""<p>Block:{0}</p>""".format(doc.block)
    msg+="""<p>School Id: {0}</p>""".format(doc.school)
    msg+="""<p>School Address:{0}</p>""".format(doc.school_name)
    msg+="""<p>School Contact:{0}</p>""".format(doc.school_contact_no)
    msg += """</u></b></p><table class='table table-bordered'><tr>
            <th>Item</th><th>Serial No</th><th>Description</th><th>Manufacturer</th>"""
       
    for d in doc.get("items_detail"):
        msg += "<tr><td>" + """{0}""".format(str(d.get('item'))) + "</td><td>" + str(d.get('serial_no') or '') + "</td><td>" + str(d.get('description')) + "</td><td>" + str(d.get('manufactrurer'))  + "</td></tr>"
        msg += "</table>"
    
    send_mail(frappe.db.get_value("Issue",doc.get('name'),"helpdesk_email"),cc,'Issue',msg)
    

    
