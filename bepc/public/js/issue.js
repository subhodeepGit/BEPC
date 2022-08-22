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
    }
});
