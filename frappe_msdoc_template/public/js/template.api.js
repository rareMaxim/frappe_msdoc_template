

frappe.router.on("change", page_changed);

function page_changed(event) {
    frappe.after_ajax(function () {
        var route = frappe.get_route();
        if (route[0] == "Form") {
            frappe.ui.form.on(route[1], {
                refresh: function (frm) {
                    build_template_buttons(frm);
                }
            })
        }
    })
};


/**
 * Builds template buttons on the form.
 * 
 * @param {Object} frm - The form object.
 * @returns {void} - This function does not return anything.
 */
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

    /**
     * Adds a custom button to the form based on the provided template.
     *
     * @param {Object} frm - The form object.
     * @param {string} title - The title of the button.
     * @param {string} name - The name of the template.
     * @param {string} group - The group to which the button belongs.
     */

    function add_button_by_template(frm, title, name, group) {
        frm.add_custom_button(__(title), function () {
            frappe.call({
                method: "frappe_msdoc_template.tmpl_gen.get_link",
                args: {
                    template_name: name, // selected template
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
    }
};
