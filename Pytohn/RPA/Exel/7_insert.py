from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8 번재 줄이 추가됨
# ws.insert_rows(8,5) # 8줄 위치에 5줄이 추가됨
# ws.insert_cols(2) # B번째 열이 추가됨
ws.insert_cols(2,3) # B번째 열로부터 3열추가됨

wb.save("sample_insert_rows.xlsx")
wb.save("sample_insert_cols.xlsx")