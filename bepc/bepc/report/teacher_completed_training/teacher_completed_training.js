// Copyright (c) 2023, SOUL and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Teacher Completed Training"] = {
	"filters": [
		{
			"fieldname": "district",
			"label": __("District"),
			"fieldtype": "Link",
			"options": "Districts",
			"width": 150,
			"reqd": 1,
		},
		{
			"fieldname": "block",
			"label": __("Block"),
			"fieldtype": "MultiSelectList",
			"options": "Block",
			"width": 150,
			"reqd": 0,
			get_data: function(txt) {
				return frappe.db.get_link_options('Block', txt, {
					district: frappe.query_report.get_filter_value("district")
				});
			}
		},
		{
			"fieldname": "name_of_school",
			"label": __("Name of School"),
			"fieldtype": "Link",
			"options": "School",
			"width": 150,
		},
	]
};