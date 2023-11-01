import openpyxl

# Takes Date, and Time worked from gui.
# Loads workbook and appends this data to 2 columns in excel
# If file does not already exist it will create it.

excel_file = ""
if not os.path.exists(excel_file):
    pass
else:
    wb = load_workbook()
    sheet = wb.active