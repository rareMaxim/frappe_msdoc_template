# Copyright (c) 2025, Maxim S and contributors
# For license information, please see license.txt

import frappe
import os
from frappe.model.document import Document
from frappe.twofactor import BytesIO
from frappe.utils.file_manager import get_file_path, save_file
from docx import Document as DocxDocument
from openpyxl import load_workbook


class DocumentTemplate(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from frappe_msdoc_template.frappe_msdoc_template.doctype.document_template_table.document_template_table import DocumentTemplateTable

        doc_type: DF.Link | None
        templates: DF.Table[DocumentTemplateTable]
    # end: auto-generated types

    def generate_and_attach(self, doctype, docname):
        """Генерує документ і додає його у вкладення."""
        file_path = generate_document(self.name, doctype, docname)
        with open(file_path, "rb") as file:
            file_content = file.read()
        file_name = os.path.basename(file_path)
        attached_file = save_file(
            file_name, file_content, doctype, docname, is_private=1)
        return attached_file.file_url


def replace_placeholders(text, context):
    """Замінює плейсхолдери у тексті."""
    for key, value in context.items():
        text = text.replace(f'{{{{ {key} }}}}', str(value))
        print(f'{{{{ {key} }}}}', str(value))
    return text


@frappe.whitelist()
def generate_document(template_name, doctype, docname):
    """Генерує документ на основі шаблону та DocType."""
    # Отримуємо шаблон
    template = frappe.get_doc("Document Template", template_name)
    file_path = get_file_path(template.file)
    if not file_path:
        frappe.throw("Файл шаблону не знайдено")

    # Отримуємо дані з DocType
    doc = frappe.get_doc(doctype, docname)
    context = doc.as_dict()
    _, ext = os.path.splitext(file_path)

    if ext == ".docx":
        return generate_word_document(file_path, context)
    elif ext == ".xlsx":
        return generate_excel_document(file_path, context)
    else:
        frappe.throw("Непідтримуваний формат файлу")


def generate_word_document(file_path, context):
    from frappe.desk.utils import provide_binary_file
    """Заповнює шаблон Word"""
    frappe.msgprint(file_path)
    doc = DocxDocument(file_path)
    for para in doc.paragraphs:
        para.text = replace_placeholders(para.text, context)
    output_stream = BytesIO()  
    doc.save(output_stream)
    # frappe.msgprint(len(output_stream))
    frappe.response["type"] = "binary"
    frappe.response["filecontent"] = output_stream.getvalue()
    frappe.response["filename"] = "document.docx"
    frappe.response["type"] = "download"
    frappe.response["display_content_as"] = "attachment"
    return frappe.response
    # return f"{file_path}.docx"


def generate_excel_document(file_path, context):
    """Заповнює шаблон Excel"""
    wb = load_workbook(file_path)
    ws = wb.active
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, str):
                cell.value = replace_placeholders(cell.value, context)
    temp_path = "/tmp/generated.xlsx"
    wb.save(temp_path)
    return temp_path
