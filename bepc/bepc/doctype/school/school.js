// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('School', 'onload', function(frm) {

    {
        frm.set_query("district", function() {
            return {
                filters: {
                    "state":frm.doc.state
                }
            };
        });
        frm.set_query("block", function() {
            return {
                filters: {
                    "district":frm.doc.district
                }
            };
        });
    }

    frappe.call({
        method:"bepc.bepc.doctype.school.school.get_user_role",
        args: {
            doc: frm.doc
        },
        callback: function(r){
            var result = r.message;

            if(result == "Level-I"  )
            {
                frm.set_df_property("data_33" ,"read_only",0);
                frm.set_df_property("site_name" ,"read_only",0);
                frm.set_df_property("udise" ,"read_only",0);
                frm.set_df_property("zone" ,"read_only",0);
                frm.set_df_property("state" ,"read_only",0);
                frm.set_df_property("district" ,"read_only",0);
                frm.set_df_property("block" ,"read_only",0);
                frm.set_df_property("cluster_name" ,"read_only",0);
                frm.set_df_property("post_office" ,"read_only",0);
                frm.set_df_property("pin_code" ,"read_only",0);
                frm.set_df_property("panchayat" ,"read_only",0);
                frm.set_df_property("near_landmark" ,"read_only",0);
                frm.set_df_property("school_mail_id" ,"read_only",0);
                frm.set_df_property("school_contact_no" ,"read_only",0);
                frm.set_df_property("name_of_president" ,"read_only",0);
                frm.set_df_property("president_contact_no" ,"read_only",0);
                frm.set_df_property("principal_name" ,"read_only",0);
                frm.set_df_property("principle_mobile_number" ,"read_only",0);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",0);
                frm.set_df_property("asst_contact_number" ,"read_only",0);
                frm.set_df_property("latitude" ,"read_only",0);
                frm.set_df_property("longitude" ,"read_only",0);
                
            }
            if(result == "Level-I" && frm.doc.workflow_state == "Pending Approval by Level-II" )
            {
                frm.set_df_property("data_33" ,"read_only",1);
                frm.set_df_property("site_name" ,"read_only",1);
                frm.set_df_property("udise" ,"read_only",1);
                frm.set_df_property("zone" ,"read_only",1);
                frm.set_df_property("state" ,"read_only",1);
                frm.set_df_property("district" ,"read_only",1);
                frm.set_df_property("block" ,"read_only",1);
                frm.set_df_property("cluster_name" ,"read_only",1);
                frm.set_df_property("post_office" ,"read_only",1);
                frm.set_df_property("pin_code" ,"read_only",1);
                frm.set_df_property("panchayat" ,"read_only",1);
                frm.set_df_property("near_landmark" ,"read_only",1);
                frm.set_df_property("school_mail_id" ,"read_only",1);
                frm.set_df_property("school_contact_no" ,"read_only",1);
                frm.set_df_property("name_of_president" ,"read_only",1);
                frm.set_df_property("president_contact_no" ,"read_only",1);
                frm.set_df_property("principal_name" ,"read_only",1);
                frm.set_df_property("principle_mobile_number" ,"read_only",1);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",1);
                frm.set_df_property("asst_contact_number" ,"read_only",1);
                frm.set_df_property("latitude" ,"read_only",1);
                frm.set_df_property("longitude" ,"read_only",1);
                
            }
	
            if(result == "Level-II" && frm.doc.workflow_state == "Pending Approval by Level-II")
            {
                frm.set_df_property("data_33" ,"read_only",0);
                frm.set_df_property("site_name" ,"read_only",0);
                frm.set_df_property("udise" ,"read_only",0);
                frm.set_df_property("zone" ,"read_only",0);
                frm.set_df_property("state" ,"read_only",0);
                frm.set_df_property("district" ,"read_only",0);
                frm.set_df_property("block" ,"read_only",0);
                frm.set_df_property("cluster_name" ,"read_only",0);
                frm.set_df_property("post_office" ,"read_only",0);
                frm.set_df_property("pin_code" ,"read_only",0);
                frm.set_df_property("panchayat" ,"read_only",0);
                frm.set_df_property("near_landmark" ,"read_only",0);
                frm.set_df_property("school_mail_id" ,"read_only",0);
                frm.set_df_property("school_contact_no" ,"read_only",0);
                frm.set_df_property("name_of_president" ,"read_only",0);
                frm.set_df_property("president_contact_no" ,"read_only",0);
                frm.set_df_property("principal_name" ,"read_only",0);
                frm.set_df_property("principle_mobile_number" ,"read_only",0);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",0);
                frm.set_df_property("asst_contact_number" ,"read_only",0);
                frm.set_df_property("latitude" ,"read_only",0);
                frm.set_df_property("longitude" ,"read_only",0);
                
            }

            if(result == "Level-II" && frm.doc.workflow_state == "Pending Approval by Level-III")
            {
                frm.set_df_property("data_33" ,"read_only",1);
                frm.set_df_property("site_name" ,"read_only",1);
                frm.set_df_property("udise" ,"read_only",1);
                frm.set_df_property("zone" ,"read_only",1);
                frm.set_df_property("state" ,"read_only",1);
                frm.set_df_property("district" ,"read_only",1);
                frm.set_df_property("block" ,"read_only",1);
                frm.set_df_property("cluster_name" ,"read_only",1);
                frm.set_df_property("post_office" ,"read_only",1);
                frm.set_df_property("pin_code" ,"read_only",1);
                frm.set_df_property("panchayat" ,"read_only",1);
                frm.set_df_property("near_landmark" ,"read_only",1);
                frm.set_df_property("school_mail_id" ,"read_only",1);
                frm.set_df_property("school_contact_no" ,"read_only",1);
                frm.set_df_property("name_of_president" ,"read_only",1);
                frm.set_df_property("president_contact_no" ,"read_only",1);
                frm.set_df_property("principal_name" ,"read_only",1);
                frm.set_df_property("principle_mobile_number" ,"read_only",1);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",1);
                frm.set_df_property("asst_contact_number" ,"read_only",1);
                frm.set_df_property("latitude" ,"read_only",1);
                frm.set_df_property("longitude" ,"read_only",1);
                
            }
	
            if(result == "Level-III" && frm.doc.workflow_state == "Pending Approval by Level-III" )
            {
                frm.set_df_property("data_33" ,"read_only",0);
                frm.set_df_property("site_name" ,"read_only",0);
                frm.set_df_property("udise" ,"read_only",0);
                frm.set_df_property("zone" ,"read_only",0);
                frm.set_df_property("state" ,"read_only",0);
                frm.set_df_property("district" ,"read_only",0);
                frm.set_df_property("block" ,"read_only",0);
                frm.set_df_property("cluster_name" ,"read_only",0);
                frm.set_df_property("post_office" ,"read_only",0);
                frm.set_df_property("pin_code" ,"read_only",0);
                frm.set_df_property("panchayat" ,"read_only",0);
                frm.set_df_property("near_landmark" ,"read_only",0);
                frm.set_df_property("school_mail_id" ,"read_only",0);
                frm.set_df_property("school_contact_no" ,"read_only",0);
                frm.set_df_property("name_of_president" ,"read_only",0);
                frm.set_df_property("president_contact_no" ,"read_only",0);
                frm.set_df_property("principal_name" ,"read_only",0);
                frm.set_df_property("principle_mobile_number" ,"read_only",0);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",0);
                frm.set_df_property("asst_contact_number" ,"read_only",0);
                frm.set_df_property("latitude" ,"read_only",0);
                frm.set_df_property("longitude" ,"read_only",0);

            }
            
            if(result == "Level-III" && frm.doc.workflow_state == "Approved by Level-III" )
            {
                frm.set_df_property("data_33" ,"read_only",1);
                frm.set_df_property("site_name" ,"read_only",1);
                frm.set_df_property("udise" ,"read_only",1);
                frm.set_df_property("zone" ,"read_only",1);
                frm.set_df_property("state" ,"read_only",1);
                frm.set_df_property("district" ,"read_only",1);
                frm.set_df_property("block" ,"read_only",1);
                frm.set_df_property("cluster_name" ,"read_only",1);
                frm.set_df_property("post_office" ,"read_only",1);
                frm.set_df_property("pin_code" ,"read_only",1);
                frm.set_df_property("panchayat" ,"read_only",1);
                frm.set_df_property("near_landmark" ,"read_only",1);
                frm.set_df_property("school_mail_id" ,"read_only",1);
                frm.set_df_property("school_contact_no" ,"read_only",1);
                frm.set_df_property("name_of_president" ,"read_only",1);
                frm.set_df_property("president_contact_no" ,"read_only",1);
                frm.set_df_property("principal_name" ,"read_only",1);
                frm.set_df_property("principle_mobile_number" ,"read_only",1);
                frm.set_df_property("name_of_asst_hmhms" ,"read_only",1);
                frm.set_df_property("asst_contact_number" ,"read_only",1);
                frm.set_df_property("latitude" ,"read_only",1);
                frm.set_df_property("longitude" ,"read_only",1); 
            }
        }
    })
});