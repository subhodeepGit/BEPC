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
        "label": "Main meter Previous reading",
        "fieldtype": "Float",
        "fieldname": "main_meter_previous_reading",
        'width':150
    },
		{
        "label": "Main meter Current reading",
        "fieldtype": "Float",
        "fieldname": "main_meter_current_reading",
        'width':150
    },
		{
        "label": "Sub meter previous reading",
        "fieldtype": "Float",
        "fieldname": "previous_meter_reading",
        'width':150
    },
		{
        "label": "Sub meter current reading",
        "fieldtype": "Float",
        "fieldname": "meter_reading",
        'width':150
    },
		{
        "label": "Total Billable Unit",
        "fieldtype": "Float",
        "fieldname": "total_billable_unit",
        'width':150
    },
		{
        "label": "Price per unit",
        "fieldtype": "Float",
        "fieldname": "price_per_unit",
        'width':150
    },
		{
        "label": "Bill Posting Date",
        "fieldtype": "Date",
        "fieldname": "date",
        'width':150
    },
		{
        "label": "Total Bill Amount",
        "fieldtype": "Float",
        "fieldname": "total_bill_amount",
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
        "fieldname": "transaction_id",
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
    site_name,
    district,
    block,
    pin_code,
    school_contact_number,
    school_address,
    date,
    main_meter_previous_reading,
    main_meter_current_reading,
    previous_meter_reading,
    meter_reading,
    total_billable_unit,
    price_per_unit,
    total_bill_amount,
    quarter,
    payment_date,
    transaction_id
	from `tabElectricity Consumption Record`
	WHERE district= %s ;''',(filters.get("district")),as_dict=1)

	return data
