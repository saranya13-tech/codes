crone tab

crontab -e

0-59 0-23 1-31 * * curl -X  POST https://tgbooksapi.techgebra.com/api/sales/invoice-scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST https://tgbooksapi.techgebra.com/api/purchases/bill_scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST https://tgbooksapi.techgebra.com/api/journals/journal-scheduled/recurring_to_journal/
0-59 0-23 1-31 * * curl -x  POST https://tgbooksapi.techgebra.com/api/reports/schedule/send_reports/
0-59 0-23 1-31 * * curl -X  POST https://tgbooksapi.techgebra.com/api/purchases/expense_scheduled/expense_to_invoice/

0-59 0-23 1-31 * * curl -X  POST https://demo.tgbooks.techgebra.com/api/sales/invoice-scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST https://demo.tgbooks.techgebra.com/api/purchases/bill_scheduled/recurring_to_invoice/
0-59 0-23 1-31 * * curl -X  POST https://demo.tgbooks.techgebra.com/api/journals/journal-scheduled/recurring_to_journal/
0-59 0-23 1-31 * * curl -x  POST https://demo.tgbooks.techgebra.com/api/reports/schedule/send_reports/
0-59 0-23 1-31 * * curl -X  POST https://demo.tgbooks.techgebra.com/api/purchases/expense_scheduled/expense_to_invoice/
