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
        "fieldname": "item",
        'width':180
    },
    {
        "label": "Status",
        "fieldtype": "Data",
        "fieldname": "status",
        'width':150
    },
    {
        "label": "Udise Code",
        "fieldtype": "Data",
        "fieldname": "udise_code",
        'width':110
    },
	{
        "label": "School Name",
        "fieldtype": "Data",
        "fieldname": "apple",
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
        "label": "Euipment lost",
        "fieldtype": "Data",
        "fieldname": "euipment_lost",
        'width':150
    },
    {
        "label": "Equipment name",
        "fieldtype": "Data",
        "fieldname": "equipment_name",
        'width':150
    },
    {
        "label": "Reason",
        "fieldtype": "Data",
        "fieldname": "reason",
        'width':150
    },
]

def get_data(filters):
    filter=[]
    
    if filters.get("name_of_school"):
        filter.append(['item',"=",filters.get("name_of_school")])
        if filters.get("district"):
            filter.append(['district',"=",filters.get("district")])
            if filters.get("block"):
                if len(filters.get("block"))==1:
                    filter.append(['block','=',filters.get("block")[0]])
                else:
                    filter.append(['block','in',filters.get("block")[0]])
    data=frappe.get_all("Theft Case record",filters=filter,
                                fields=['item','status','udise_code','apple','district','block','euipment_lost','equipment_name','reason'])
 
    return data