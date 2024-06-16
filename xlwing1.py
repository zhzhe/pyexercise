import xlwings as xw
app=xw.App(visible=True,add_book=False)
# wb=app.books.add()
# wb.sheets['sheet1'].range('A1').value='人生'
# wb.sheets['sheet1'].range('B2').value='人生苦短'
# wb.save(r'd:\test.xlsx')
# wb.close()
# app.quit()

wb=app.books.open(r'd:\test.xlsx')
txt = wb.sheets('sheet1').range('A1').raw_value
print("A1= ",txt)
wb.sheets('sheet1').range('A1').raw_value = '人生苦短啊！'
print(wb.sheets('sheet1').range('A1').raw_value)
wb.sheets('sheet1').range('b1').formula = '=a2+a3'
wb.save()
wb.close()
app.quit()
