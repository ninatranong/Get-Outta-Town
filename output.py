import pandas as pd

def create_csv(results):
    countries = results.keys()
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('Get_Outta_Town.xlsx', engine="xlsxwriter")
    workbook  = writer.book
    wrap_format = workbook.add_format({'text_wrap': True})
    for country in countries:
        df = pd.DataFrame(data=results[country], index=[0]).T
        
        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name=country)
        # Create xlsxwriter worksheet object 
        worksheet = writer.sheets[country] 
           
        # set width of the B column 
        worksheet.set_column('A:C', 20, wrap_format) 
        
    # Close the Pandas Excel writer and output the Excel file.
    writer.close()
    print('File created.')