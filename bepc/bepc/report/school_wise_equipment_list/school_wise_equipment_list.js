// Copyright (c) 2023, SOUL and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["School Wise Equipment list"] = {
	"filters": [
		{
			"fieldname": "district",
			"label": __("District"),
			"fieldtype": "Link",
			"options": "Districts",
			"width": 150,
			"reqd": 1,
	
		},
	]
};