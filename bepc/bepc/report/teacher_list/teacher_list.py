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
        "label": "Teacher Full Name",
        "fieldtype": "Data",
        "fieldname": "full_name",
        'width':150
    },
    {
        "label": "Email",
        "fieldtype": "Data",
        "fieldname": "email",
        'width':150
    },
    {
        "label": "Gender",
        "fieldtype": "Data",
        "fieldname": "gender",
        'width':150
    },
    {
        "label": "Status",
        "fieldtype": "Data",
        "fieldname": "status",
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

    data=frappe.get_all("Teacher",filters=filter,
                                fields=['site','school_name','udise_code','block','district','full_name','email','gender','status'])

    return data