// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Teacher Group', {
	
	onload:function(frm)
	{
		frm.set_query('teacher','teacher_list',function() {
			return {
				filters: {
					"site":frm.doc.school,
					"district":frm.doc.district,
					"block":frm.doc.block
				}
			};
		});
	}	
});