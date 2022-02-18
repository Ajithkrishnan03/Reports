from odoo import api, models


class ReportPurchaseCustomerWise(models.AbstractModel):
    _name = 'report.purchase_report.purchase_report_view'
    _decription ='purchase_report_view'

    @api.model
    
    def _get_report_values(self, docids, data=None):
        return {
           
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'data':data['form'],
        }
