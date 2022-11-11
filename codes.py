//to add dat  with same key value pair

[{'sales':100,'amount':1000},{'sales':200,'amount':100},{'sales':100,'amount':100}]



for item in instance.data["items"]:
            item_data = item["item"]
            item["sales_account"] = item_data["account_code"]
            account_group.append(
                {
                    "credit_account_code": item["sales_account"],
                    "amount": 0,
                    "voucher_code": "SI",
                    "voucher_number": instance.data["sales_invoice_no"],
                    "debit_account_code": debit_account_code,
                    "voucher_ref_id": voucher_ref_id,
                    "date": instance.data["created_at"],
                }
            )
            data = []
            for obj in account_group:
                if obj not in data:
                    data.append(obj)
        for item in instance.data["items"]:
            for obj in data:
                if item["sales_account"] == obj["credit_account_code"]:
                    obj["amount"] = float(obj["amount"]) + float(
                        item["qty"]
                    ) * float(item["item_rate"])
                    
 //simple code
 
 d = defaultdict(float)
        for item in instance.data["items"]:
            d[(item['sales_account'])] += float(item['total_price'])
            
            
 // key value separation 
for key, value in account_group_sum.items():
            account_group.append(
                    {
                        "credit_account_code": key,
                        "amount": value,
