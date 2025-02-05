// Copyright (c) 2025, Maxim S and contributors
// For license information, please see license.txt

frappe.ui.form.on("Document Template", {
    refresh(frm) {
        frm.add_custom_button(__('Згенерувати документ'), function () {
            window.open("/api/method/frappe_msdoc_template.frappe_msdoc_template.doctype.document_template.document_template.generate_document?template_name=57e3ega40o&doctype=" + frm.doctype + "&docname=" + frm.docname, '_blank');
        });
    },
});

frappe.ui.form.on("*", {
    refresh(frm) {
        frappe.msgprint("Hello");
    }
});