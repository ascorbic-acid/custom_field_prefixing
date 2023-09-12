from frappe.custom.doctype.custom_field.custom_field import CustomField

class CustomCustomField(CustomField):
    def set_fieldname(self):
        super(CustomCustomField, self).set_fieldname()
        
        prefix = "custom_"

        if self.fieldname.startswith(prefix):
            self.fieldname = self.fieldname[len(prefix):]
