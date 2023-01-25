# Copyright (c) 2023, SOUL and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime

def execute(filters=None):
	data = get_data(filters)
	columns = get_columns(filters)

	return columns,data

def get_columns(filters=None):
    return [
    {
        "label": "School",
        "fieldtype": "Link",
        "fieldname": "tcil",
		"options":"School",
        'width':180
    },
	{
        "label": "School Name",
        "fieldtype": "Data",
        "fieldname": "school_name",
        'width':180
    },
	{
        "label": "School Address",
        "fieldtype": "Data",
        "fieldname": "school_address",
        'width':180
    },
	{
        "label": "District",
        "fieldtype": "Data",
        "fieldname": "district",
        'width':180
    },
	{
        "label": "School Contact No.",
        "fieldtype": "Data",
        "fieldname": "school_contact_no",
        'width':180
    },
	{
        "label": "Helpdesk Email",
        "fieldtype": "Data",
        "fieldname": "helpdesk_email",
        'width':180
    },
	{
		"label": "Status of Issue",
        "fieldtype": "Data",
        "fieldname": "status",
        'width':180
	},
	{
        "label": "No. of Issues(based on Status)",
        "fieldtype": "Data",
        "fieldname": "count(status)",
        'width':180
    },
	{
		"label": "SLA Status",
        "fieldtype": "Data",
        "fieldname": "agreement_status",
        'width':180
	},
	{
        "label": "No. of Issues(based on SLA)",
        "fieldtype": "Data",
        "fieldname": "count(agreement_status)",
        'width':180
    },
	# {
    #     "label": "Issue creation date and Time",
    #     "fieldtype": "Datetime",
    #     "fieldname": "resolution_date",
    #     'width':180
    # },
	# {
    #     "label": "Resolution Date",
    #     "fieldtype": "Datetime",
    #     "fieldname": "resolution_date",
    #     'width':180
    # },
]

def get_data(filters):
	print("\n\n\n\n")
	data= []
	fltr, flt2 = {},[]
	if filters.get("district"):
		fltr.update({"district":filters.get("district")})

	# if filters.get("issue_creation_date_and_time"):
	# 	fltr.update({"issue_creation_date_and_time":filters.get("issue_creation_date_and_time")})

	# if filters.get("resolution_date"):
	# 	fltr.update({"resolution_date":filters.get("resolution_date")})

	# data=frappe.db.sql(''' SELECT tcil, school_name, school_address, district, school_contact_no, helpdesk_email, status, count(status), agreement_status, count(agreement_status), issue_creation_date_and_time, resolution_date
	# from `tabIssue` 
	# WHERE district= %s and %s <= %s
	# GROUP BY school, status, agreement_status; ''',(filters.get("district"),filters.get("resolution_date"),filters.get("resolution_date")),as_dict=1)

	data=frappe.db.sql(''' SELECT tcil, school_name, school_address, district, school_contact_no, helpdesk_email, status, count(status), agreement_status, count(agreement_status) 
	from `tabIssue` WHERE district= %s Group By school, status, agreement_status;''',(filters.get("district")),as_dict=1)
	print("\n\n\n\n",data)
	return data