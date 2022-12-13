with open(
            f"{os.getcwd()}/apps/companies/seed_data/tax/"+instance.tax_code+".json",
            "wb+",
        ) as f:
            #f.name or f.filename (dont know which one)will get filename.So you can replace it name.txt
            for chunk in f.read():
                f.write(chunk)
        handle=open(f"{os.getcwd()}/apps/companies/seed_data/tax/"+instance.tax_code+".json",'r+')
        handle.write('[{"name":"GST","total_percentage":"10","splits":[{"name":"CGST","percentage":"9"},{"name":"IGST","percentage":"9"},{"name":"SGST","percentage":"9"}]},{"name":"VAT","total_percentage":"20","splits":[{"name":"VAT","percentage":"10"}]}]')
  
        handle.close()
