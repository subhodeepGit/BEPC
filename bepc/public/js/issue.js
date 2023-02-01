frappe.ui.form.on('Issue', {
    
	setup:function(frm)
    {
        frm.set_query("district_", function() {
            return {
                filters: {
                    "state":frm.doc.state_
                }
            };
        });
        frm.set_query("block", function() {
            return {
                filters: {
                    "district":frm.doc.district_
                }
            };
        });
        frm.set_query("school", function() {
            return {
                filters: {
                    "state":frm.doc.state_,
                    "district":frm.doc.district_
                }
            };
        });
        frm.set_query('item', 'items_detail', function() {
            return {
                filters: {
                    "tcil_code":frm.doc.tcil
                }
            };
        });
    
    },
//     refresh:function(frm){
//         if (!frm.is_new()){
//             frm.add_custom_button(__('Submit'), function() {
//                 frappe.call({
//                     method: "bepc.bepc.doctype.issue.mail",
//                     doc:frm.doc,
//                     args:{
//                         name:frm.doc.name,
//                     },
//                     callback: function() {
//                         frm.refresh();
//                     }
//                 });
//             }).addClass('btn-primary');;
//         }
        
//     }
});

