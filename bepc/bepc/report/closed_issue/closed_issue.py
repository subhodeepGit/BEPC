# Copyright (c) 2023, SOUL and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    data = get_data(filters)
    columns = get_columns(filters)

    return columns,data

def get_columns(filters=None):
    return [
    {
        "label": "Subject",
        "fieldtype": "Data",
        "fieldname": "subject",
        'width':180
    },
    {
        "label": "School Name",
        "fieldtype": "Data",
        "fieldname": "school_name",
        'width':150
    },
    {
        "label": "Status",
        "fieldtype": "Data",
        "fieldname": "status",
        'width':110
    },
    {
        "label": "District",
        "fieldtype": "Link",
        "fieldname": "district",
        "options":"Districts",
        'width':150
    },
    {
        "label": "Block",
        "fieldtype": "Link",
        "options":"Block",
        "fieldname": "block",
        'width':150
    },
    {
        "label": "TCIL",
        "fieldtype": "Data",
        "fieldname": "tcil",
        'width':150
    },
    {
        "label": "Issue Type",
        "fieldtype": "Data",
        "fieldname": "issue_type",
        'width':150
    },
    {
        "label": "Helpdesk Email",
        "fieldtype": "Data",
        "fieldname": "helpdesk_email",
        'width':150
    },
    {
        "label": "Project Manager",
        "fieldtype": "Data",
        "fieldname": "project_manager",
        'width':150
    },
    {
        "label": "District Collector",
        "fieldtype": "Data",
        "fieldname": "district_collector",
        'width':150
    },
    {
        "label": "Item",
        "fieldtype": "Data",
        "fieldname": "item",
        'width':150
    },
    {
        "label": "Manufactrurer",
        "fieldtype": "Data",
        "fieldname": "manufactrurer",
        'width':150
    },
    {
        "label": "Serial no",
        "fieldtype": "Data",
        "fieldname": "serial_no",
        'width':150
    },
    {
        "label": "Description",
        "fieldtype": "Data",
        "fieldname": "description",
        'width':150
    },
	{
        "label": "OEM Email address",
        "fieldtype": "Data",
        "fieldname": "oem_email_address",
        'width':150
    },

]

def get_data(filters):
    filter=[]
    filter.append(['status',"=","Closed"])
    if filters.get("name_of_school"):
        filter.append(['tcil',"=",filters.get("name_of_school")])
        if filters.get("district"):
            filter.append(['district',"=",filters.get("district")])
            if filters.get("block"):
                if len(filters.get("block"))==1:
                    filter.append(['block','=',filters.get("block")[0]])
                else:
                    filter.append(['block','in',filters.get("block")[0]])

    data=frappe.get_all("issues",filters=filter,
                            fields=['name','status','subject','tcil','school_name',
                            'district','block','issue_type','helpdesk_email','project_manager','district_collector'])
    
    final_data=[]
    for t in data:
        school=frappe.get_all("Item Detail",{"parent":t["name"]},['item','manufactrurer','serial_no','description','oem_email_address'])
        for s in school:
            s['name']=t['name']
            s['status']=t['status']
            s['subject']=t['subject']
            s['tcil']=t['tcil']
            s['school_name']=t['school_name']
            s['district']=t['district']
            s['block']=t['block']
            s['issue_type']=t['issue_type']
            s['helpdesk_email']=t['helpdesk_email']
            s['project_manager']=t['project_manager']
            s['district_collector']=t['district_collector']
            final_data.append(s)

    return final_data