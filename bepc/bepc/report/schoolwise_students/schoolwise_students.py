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
        "label": "PIMPL/TCIL code",
        "fieldtype": "Link",
        "fieldname": "school_code",
        "options":"School",
        'width':180
    },
    {
        "label": "UDISE",
        "fieldtype": "Data",
        "fieldname": "udise",
        'width':150
    },
    {
        "label": "Name of School",
        "fieldtype": "Data",
        "fieldname": "name_of_school",
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
        "label": "Class V(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_vbg",
        'width':150
    },
    {
        "label": "Class VI(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_vibg",
        'width':150
    },
    {
        "label": "Class VII(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_viibg",
        'width':150
    },
    {
        "label": "Class VIII(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_viiibg",
        'width':150
    },
    {
        "label": "Class IX(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_ixbg",
        'width':150
    },
    {
        "label": "Class X(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_xbg",
        'width':150
    },
    {
        "label": "Class XI(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_xibg",
        'width':150
    },
    {
        "label": "Class XII(B/G)",
        "fieldtype": "Int",
        "fieldname": "class_xiibg",
        'width':150
    },
    {
        "label": "Total Students",
        "fieldtype": "Int",
        "fieldname": "total_students",
        'width':150
    },
]

def get_data(filters):
    filter=[]
    # if filters.get("name_of_school"):
    #     filter.append(['school_code',"=",filters.get("name_of_school")])
    if filters.get("district"):
        filter.append(['district',"=",filters.get("district")])
        if filters.get("block"):
            if len(filters.get("block"))==1:
                filter.append(['block','=',filters.get("block")[0]])
            else:
                filter.append(['block','in',filters.get("block")[0]])

    # data=frappe.db.sql(''' select
    # school_code,
    # udise,
    # name_of_school,
    # district,
    # block,
    # class_vbg,
    # class_vibg,
    # class_viibg,
    # class_viiibg,
    # class_ixbg,
    # class_xbg,[[]]
    # class_xibg,
    # class_xiibg,
    # sum(class_vbg + class_vibg + class_viibg + class_viiibg) as "total_students"
    # from
    # `tabSchool Survey Form`
    # WHERE district = %s or block = %s
    # # GROUP BY school_code; ''',(filters.get("district"),filters.get("block")),as_dict=1)

    data=frappe.get_all("School Survey Form",filters=filter,
                                fields=['school_code','udise','name_of_school','district',
                                'block','class_vbg','class_vibg','class_viibg','class_viiibg',
                                'class_ixbg','class_xbg','class_xibg','class_xiibg'], group_by ="school_code")        
    for t in data:
        total_students = 0
        total_students = t["class_vbg"] + t["class_vibg"] + t["class_viibg"]+ t["class_viiibg"] + t["class_ixbg"] + t["class_xbg"] + t["class_xibg"] + t["class_xiibg"]
        t['total_students']=total_students

    return data