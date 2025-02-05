function build_template_buttons(frm) {
    frappe.call({
        method: "frappe_msdoc_template.tmpl_gen.get_templates",
        args: {
            doctype: frm.doctype
        },
        callback: function (r) {
            if (r.message) {
                for (let i = 0; i < r.message.length; i++) {
                    add_button_by_template(frm, r.message[i].title, r.message[i].name, r.message[i].group);
                }
            }
        }
    });
}

function add_button_by_template(frm, title, name, group) {
    frm.add_custom_button(__(title), function () {
        frappe.call({
            method: "frappe_msdoc_template.tmpl_gen.get_link",
            args: {
                template_name: name, // обраний шаблон
                doctype: frm.doctype,
                docname: frm.doc.name
            },
            callback: function (r) {
                if (r.message) {
                    window.open(r.message);
                }
            }
        });
    }, __(group));
};