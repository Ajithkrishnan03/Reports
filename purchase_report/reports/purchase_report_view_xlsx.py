from odoo import models

class PurchaseReportViewXlsx(models.AbstractModel):
	_name = 'report.purchase_report.purchase_report_view_xlsx'
	_inherit = 'report.report_xlsx.abstract'

	def generate_xlsx_report(self, workbook, data, customer):
		print("success", data['orders'])
		sheet = workbook.add_worksheet('Orders')
		bold = workbook.add_format({'bold': True})
		sheet.set_column('A:A',20)
		sheet.set_column('B:B',30)
		sheet.set_column('C:C',20)
		sheet.set_column('D:D',20)
		sheet.set_column('E:E',20)
		sheet.set_column('F:F',10)
		sheet.set_column('G:G',10)

		row = 0
		col = 0
		total = 0
		total1 = 0
		total2 = 0
		counter = 0
		sheet.write(row, col,'Customer_Name', bold)
		sheet.write(row, col + 1, 'Company',bold)
		sheet.write(row, col + 2,'Order_Date', bold)
		sheet.write(row, col + 3, 'Order_Number',bold)
		sheet.write(row, col + 4,'Untaxed_Amount', bold)
		sheet.write(row, col + 5,'Total', bold)
		sheet.write(row, col + 6,'Tax', bold)
		#sheet.write(row, col + 7,'demo', bold)
		#sheet.write(row + 25, col + 2,'example')
		
		for order in data['orders']:
			row = row + 1
			
			#total= order['amount_untaxed']
			sheet.write(row, col, order['partner_id'][1])
			sheet.write(row, col + 1, order['company_id'][1])
			sheet.write(row, col + 2, order['date_order'])
			sheet.write(row, col + 3, order['name'])
			sheet.write(row, col + 4, order['amount_untaxed'])
			sheet.write(row, col + 5, order['amount_total'])
			#sheet.write(row, col + 6, order[('amount_total - amount_untaxed')])
			sheet.write(row, col + 6, order['amount_total'] - order['amount_untaxed'])
			#sheet.write(row +25, col + 4, order['amount_untaxed'] + total)
			#sheet.write(row, col + 7, order['name'] + total)

		for order in data['orders']:

			col = 2
			demo = order['amount_total'] - order['amount_untaxed']
			#total=0
			total= total + order['amount_untaxed']
			total1= total1 + order['amount_total']
			total2 = total2 + demo
			counter = counter + 1
			#total2= total2 + order['amount_total'] - order['amount_untaxed']
			#counter=0
			sheet.write(row + 1, col, 'Total',bold)
			#sheet.write(row + 1, col + 2, order['amount_untaxed'] + total)
			#sheet.write(row + 1, col + 1, order['name'] + counter+1)
			sheet.write(row + 1, col + 1,  counter,bold)
			sheet.write(row + 1, col + 2,  total,bold)
			sheet.write(row + 1, col + 3,  total1,bold)
			sheet.write(row + 1, col + 4,  total2,bold)
			

			
			
			
			
