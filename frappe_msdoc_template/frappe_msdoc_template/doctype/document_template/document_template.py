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

    