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
        "label": "Status",
        "fieldtype": "Select",
        "fieldname": "status",
        'width':180
    },
	{
		"label": "No. of Cases",
        "fieldtype": "Data",
        "fieldname": "count(status)",
        'width':180
	}
]

def get_data(filters):
	data= []
	fltr, flt2 = {},[]
	if filters.get("district"):
		fltr.update({"district":filters.get("district")})
	data=frappe.db.sql(''' select
    status,
    count(status)
	from `tabTheft Case record`
	WHERE district= %s Group By status;''',(filters.get("district")),as_dict=1)

	print("\n\n\n\n",data)
	return data