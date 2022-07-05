// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt
frappe.ui.form.on('Survey Form', {
	kra_template: function(frm) {
		if(frm.doc.kra_template){
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Survey Questionnaire Template",
					filters: {name: frm.doc.kra_template}
				},
				callback: function(r) {
					if(r.message){
						if(!r.message.electricity_consumption_reading){
							frm.set_df_property('electricity_consumption_reading', 'hidden', 1);
						}
						if(!r.message.internet_use){
							frm.set_df_property('internet_use', 'hidden', 1);
						}
					}
				}
			});
		}
	},
});

frappe.ui.form.on("Survey Form", {	
    onload:function(frm){		     
    if(frappe.session.user_fullname == "Data Entry Operator"  ){
		alert("Hi Data Entry Operator ")
        frm.set_df_property("title_of_the_document","read_only",0);	
		frm.set_df_property("kra_template","read_only",0);	
		frm.set_df_property("full_name","read_only",0);	
		frm.set_df_property("email_id","read_only",0);	
		frm.set_df_property("date_of_upload","read_only",0);
    };
	// if(frappe.session.user_fullname == "Data Entry Operator"  ){
	// 	alert("Hi Data Entry Operator ")
    //     frm.set_df_property("title_of_the_document","read_only",1);	
	// 	frm.set_df_property("kra_template","read_only",1);	
	// 	frm.set_df_property("full_name","read_only",1);	
	// 	frm.set_df_property("email_id","read_only",1);	
	// 	frm.set_df_property("date_of_upload","read_only",1);
    // };
	

	if(frappe.session.user_fullname == "Approver 1" ){
		alert("Hi Approver 1 ")
        frm.set_df_property("title_of_the_document","read_only",1);	
		frm.set_df_property("kra_template","read_only",0);	
		frm.set_df_property("full_name","read_only",0);	
		frm.set_df_property("email_id","read_only",0);	
		frm.set_df_property("date_of_upload","read_only",0);
    };
	// if(frappe.session.user_fullname == "Approver 1" ){

	// 	alert("Hi Approver 1 ")
    //     frm.set_df_property("title_of_the_document","read_only",1);	
	// 	frm.set_df_property("kra_template","read_only",1);	
	// 	frm.set_df_property("full_name","read_only",1);	
	// 	frm.set_df_property("email_id","read_only",1);	
	// 	frm.set_df_property("date_of_upload","read_only",1);
    // };
	
	if(frappe.session.user_fullname == "Approver 2" ){
	
        frm.set_df_property("title_of_the_document","read_only",1);	
		frm.set_df_property("kra_template","read_only",0);	
		frm.set_df_property("full_name","read_only",0);	
		frm.set_df_property("email_id","read_only",0);	
		frm.set_df_property("date_of_upload","read_only",0);
    };
	// if(frappe.session.user_fullname == "Approver 2" ){
	// 	alert("Hi Approver 2 ")
    //     frm.set_df_property("title_of_the_document","read_only",1);	
	// 	frm.set_df_property("kra_template","read_only",1);	
	// 	frm.set_df_property("full_name","read_only",1);	
	// 	frm.set_df_property("email_id","read_only",1);	
	// 	frm.set_df_property("date_of_upload","read_only",1);
    // };
	
	// if(frappe.session.user == "Administrator"){
	// 	alert("hi Administrator")
    //     frm.set_df_property("title_of_the_document","read_only",0);	
	// 	frm.set_df_property("kra_template","read_only",0);	
	// 	frm.set_df_property("full_name","read_only",0);	
	// 	frm.set_df_property("email_id","read_only",0);	
	// 	frm.set_df_property("date_of_upload","read_only",0);
    // };

}
		
});
