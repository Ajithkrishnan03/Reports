from odoo import models, fields, api, _

class PurchaseReportByCustomer(models.TransientModel):
    _name = 'purchase.customer.report'

    partner_id = fields.Many2one('res.partner', string="Customer")
    start_date = fields.Datetime(string="Start Date",required=True)
    end_date = fields.Datetime(string="End Date",required=True)


    def print_excel_report(self):

        domain = []
        partner_id = self.partner_id

        if partner_id:
            domain += [('partner_id', '=', partner_id.id)]
        start_date = self.start_date
        if start_date:
            domain += [('date_order', '>=', start_date)]
        end_date = self.end_date
        if end_date:
            domain += [('date_order', '<=', end_date)]

        orders = self.env['purchase.order'].search_read(domain)
        datas = {
        'orders': orders,
        'form_data' : self.read()[0]
        }
        return self.env.ref('purchase_report.action_report_by_customer_excel').report_action(self, data=datas)


    def print_report(self):
        purchase_order = self.env['purchase.order'].search([])
        purchase_order_groupby_dict = {}
        for customer in self.partner_id:
            filtered_purchase_order = list(filter(lambda x: x.partner_id == customer, purchase_order))
            print('filtered_purchase_order ===',filtered_purchase_order)
            filtered_by_date = list(filter(lambda x: x.date_order >= self.start_date and x.date_order <= self.end_date, filtered_purchase_order))
            purchase_order_groupby_dict[customer.name] = filtered_by_date

        final_dist = {}
        for customer in purchase_order_groupby_dict.keys():
            purchase_data = []
            for order in purchase_order_groupby_dict[customer]:
                temp_data = []
                
                temp_data.append(order.company_id.name)
                temp_data.append(order.date_order)
                temp_data.append(order.name)
                temp_data.append(order.amount_untaxed)
                temp_data.append(order.amount_total)
                temp_data.append(order.amount_total-order.amount_untaxed)
                purchase_data.append(temp_data)
            final_dist[customer] = purchase_data

        datas = {
            'ids': self,
            'model': 'purchase.customer.report',
            'form': final_dist,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
    
        return self.env.ref('purchase_report.action_report_by_customer').report_action(self, data=datas)
