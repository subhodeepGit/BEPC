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
    # {
    #     "label": "Trainer name",
    #     "fieldtype": "Data",
    #     "fieldname": "trainer_number",
    #     'width':150
    # },
    # {
    #     "label": "Email",
    #     "fieldtype": "Data",
    #     "fieldname": "email_id",
    #     'width':150
    # },
    {
        "label": "Total teacher to be trained",
        "fieldtype": "Data",
        "fieldname": "total_teacher_to_be_trained",
        'width':150
    },
    {
        "label": "Training days",
        "fieldtype": "Data",
        "fieldname": "training_days",
        'width':150
    },
    {
        "label": "Per session hours",
        "fieldtype": "Data",
        "fieldname": "per_session_hours",
        'width':150
    },
    {
        "label": "From Date",
        "fieldtype": "Data",
        "fieldname": "date",
        'width':150
    },
    {
        "label": "To Date",
        "fieldtype": "Data",
        "fieldname": "end_date",
        'width':150
    },
    {
        "label": "Training Venue",
        "fieldtype": "Data",
        "fieldname": "training_venue",
        'width':150
    },
    {
        "label": "Teachers group",
        "fieldtype": "Data",
        "fieldname": "teachers_group",
        'width':150
    },
    {
        "label": "School consent",
        "fieldtype": "Data",
        "fieldname": "school_consent",
        'width':150
    },
    {
        "label": "Teacher group name",
        "fieldtype": "Data",
        "fieldname": "teacher_group_name",
        'width':150
    },

]

def get_data(filters):
    filter=[]
    filter.append(['status',"=","Completed"])
    if filters.get("name_of_school"):
        filter.append(['site',"=",filters.get("name_of_school")])
        if filters.get("district"):
            filter.append(['district',"=",filters.get("district")])
            if filters.get("block"):
                if len(filters.get("block"))==1:
                    filter.append(['block','=',filters.get("block")[0]])
                else:
                    filter.append(['block','in',filters.get("block")[0]])

    data=frappe.get_all("Teacher Training",filters=filter,
                            fields=['name','status','total_teacher_to_be_trained','training_days','per_session_hours',
                            'date','end_date','training_venue','teachers_group','school_consent','teacher_group_name'])
    
    final_data=[]
    for t in data:
        school=frappe.get_all("School List",{"parent":t["name"]},['site','school_name','district','block'])
        for s in school:
            s['name']=t['name']
            s['status']=t['status']
            s['total_teacher_to_be_trained']=t['total_teacher_to_be_trained']
            s['training_days']=t['training_days']
            s['per_session_hours']=t['per_session_hours']
            s['date']=t['date']
            s['end_date']=t['end_date']
            s['training_venue']=t['training_venue']
            s['teachers_group']=t['teachers_group']
            s['school_consent']=t['school_consent']
            s['teacher_group_name']=t['teacher_group_name']
            final_data.append(s)
        name=frappe.get_all("Trainer Name",{"parent":t["name"]},['trainer_number','email_id'])
        # for s in name:
        #     s['name']=t['name']
        #     s['status']=t['status']
        #     s['total_teacher_to_be_trained']=t['total_teacher_to_be_trained']
        #     s['training_days']=t['training_days']
        #     s['per_session_hours']=t['per_session_hours']
        #     s['date']=t['date']
        #     s['end_date']=t['end_date']
        #     s['training_venue']=t['training_venue']
        #     s['teachers_group']=t['teachers_group']
        #     s['school_consent']=t['school_consent']
        #     s['teacher_group_name']=t['teacher_group_name']
        #     final_data.append(s)

    return final_data