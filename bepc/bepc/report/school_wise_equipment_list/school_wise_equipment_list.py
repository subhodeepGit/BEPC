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
        "label": "TCIL Code",
        "fieldtype": "Data",
        "fieldname": "site",
        'width':180
    },
    {
        "label": "School Name",
        "fieldtype": "Data",
        "fieldname": "school_name",
        'width':150
    },
    {
        "label": "Udise Code",
        "fieldtype": "Data",
        "fieldname": "udise_code",
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
        "label": "Lab",
        "fieldtype": "Data",
        "fieldname": "lab",
        'width':150
    },
    {
        "label": "Item Name",
        "fieldtype": "Data",
        "fieldname": "item_name",
        'width':150
    },
    {
        "label": "Manufacturer",
        "fieldtype": "Data",
        "fieldname": "vendor",
        'width':150
    },
    {
        "label": "Serial number",
        "fieldtype": "Data",
        "fieldname": "serial_number",
        'width':150
    },
    {
        "label": "OEM Email",
        "fieldtype": "Data",
        "fieldname": "mac_id",
        'width':150
    },
]

def get_data(filters):
    filter=[]
    
    if filters.get("name_of_school"):
        filter.append(['site',"=",filters.get("name_of_school")])
        if filters.get("district"):
            filter.append(['district',"=",filters.get("district")])
            if filters.get("block"):
                if len(filters.get("block"))==1:
                    filter.append(['block','=',filters.get("block")[0]])
                else:
                    filter.append(['block','in',filters.get("block")[0]])
    data=frappe.get_all("School wise Equipment List",filters=filter,
                                fields=['name','site','school_name','udise_code','block','district'])

    final_data=[]
    for t in data:
        child = frappe.get_all("Schoolwise Equipment List childtable",{"parent":t["name"]},['lab','item_name','vendor','serial_number','mac_id'])
        for i in child:
            i['name']=t['name']
            i['site']=t['site']
            i['school_name']=t['school_name']
            i['udise_code']=t['udise_code']
            i['block']=t['block']
            i['district']=t['district']
            final_data.append(i)    
    return final_data