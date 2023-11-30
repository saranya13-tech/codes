crone tab

crontab -e

0-59 0-23 1-31 * * curl -X  POST sales/invoice-scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST purchases/bill_scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST journals/journal-scheduled/recurring_to_journal/
0-59 0-23 1-31 * * curl -x  POST reports/schedule/send_reports/
0-59 0-23 1-31 * * curl -X  POST purchases/expense_scheduled/expense_to_invoice/

