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
        "fieldtype": "Link",
        "fieldname": "site",
        "options":"School",
        'width':180
    },
    {
        "label": "UDISE code",
        "fieldtype": "Data",
        "fieldname": "udise_code",
        'width':150
    },
    {
        "label": "Name of School",
        "fieldtype": "Data",
        "fieldname": "site_name",
        'width':110
    },
    {
        "label": "School Contact Number",
        "fieldtype": "Data",
        "fieldname": "school_contact_number",
        'width':150
    },
    {
        "label": "School Address",
        "fieldtype": "Data",
        "fieldname": "school_address",
        'width':150
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
        "label": "Pin code",
        "fieldtype": "Data",
        "fieldname": "pin_code",
        'width':150
    },
	{
        "label": "Date",
        "fieldtype": "Date",
        "fieldname": "date",
        'width':150
    },
	{
        "label": "Internet service provider",
        "fieldtype": "Data",
        "fieldname": "internet_service_provider",
        'width':150
    },
	{
        "label": "Data Usage (Gb)",
        "fieldtype": "Float",
        "fieldname": "data_usage",
        'width':150
    },
	{
        "label": "Monthly Bill Amount",
        "fieldtype": "Float",
        "fieldname": "monthly_bill_amount",
        'width':150
    },
	{
        "label": "Payment Date",
        "fieldtype": "Date",
        "fieldname": "payment_date",
        'width':150
    },
	{
        "label": "Transaction ID",
        "fieldtype": "Data",
        "fieldname": "payment_details",
        'width':150
    },
	{
        "label": "Quarter for Payment",
        "fieldtype": "Data",
        "fieldname": "quarter",
        'width':150
    },
]

def get_data(filters):
	data= []
	fltr, flt2 = {},[]
	if filters.get("district"):
		fltr.update({"district":filters.get("district")})
	data=frappe.db.sql(''' select
    site,
    udise_code,
    siteschool_name,
    district,
    block,
    pin_code,
    school_contact_number,
    school_address,
    date,
    internet_service_provider,
	data_usage,
	monthly_bill_amount,
	quarter,
	payment_date,
	payment_details
	from `tabInternet consumption Record`
	WHERE district= %s ;''',(filters.get("district")),as_dict=1)
	return data