

frappe.ui.form.on('Purchase Order', {
	refresh: function(frm) {
        // alert('Zaaaaaaaaaak');

        frm.set_query("supplier_2", function () {
            return {"filters": {'supplier_type': 'Company'}};
        });


    }

});

