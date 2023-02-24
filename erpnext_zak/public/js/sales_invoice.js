
frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        if(frm.is_new()===0){
            frm.trigger("toggle_discount");
        }
    },
    customer: function(frm) {
        frm.trigger("toggle_discount");
		// frm.set_value("additional_discount_percentage", 0);
		// frm.set_value("discount_amount", 0);
		//
		// frm.set_df_property('additional_discount_percentage', 'read_only', 1);
		// frm.set_df_property('discount_amount', 'read_only', 1);
		// const values = frappe.db.get_value("User", frappe.session.user, "first_name");
		// const values = frappe.db.get_single_value("System Settings", "default_currency");
		// alert(values);
		// console.log(values);
		// if(frm.doc.customer){
		// }
		// else {
		// 	alert('zak22222222222');
		// }
    },
    toggle_discount: function(frm) {
        if(frm.doc.customer){
            frappe.db.get_value("Customer", frm.doc.customer, "allow_discount").then(r => {
                const allow_discount = r && r.message && r.message.allow_discount || 0
                frm.events.handle_toggle_discount(frm, allow_discount);
            })
        }else{
            frm.events.handle_toggle_discount(frm, 0);
        }
    },
    handle_toggle_discount(frm, allow_discount){
        [
            'is_cash_or_non_trade_discount',
            'additional_discount_percentage',
            'discount_amount',
            'apply_discount_on',
        ].forEach(field => {
            frm.toggle_enable(field, allow_discount);
            if(field === 'apply_discount_on'){
                return
            }
            frm.set_value(field, 0);
            frm.refresh_field(field);
        });
    }
})