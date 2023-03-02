from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

from openpyxl.chart import BarChart,Reference,LineChart
# bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
# bar_chart = BarChart() # 차트의 종류를 설정 (Bar,Line,Pie, ..)
# bar_chart.add_data(bar_value)
# ws.add_chart(bar_chart, "E1") # 차트 넣을 위치 정의

#B11:C11 까지의 데이터
line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3)
line_chart = LineChart()
line_chart.add_data(line_value, titles_from_data = True) # 계열 -> 수학,영어처엄 제목에서 가지고 오게됨
line_chart.title = "성적표" # 제목
line_chart.style = 20 # 미래 정의 된 스타일을 적용, 사용자가 개별 지정도 가능
line_chart.y_axis.title = "점수" #y축의 제목
line_chart.x_axis.title = "점수" #x축의 제목
ws.add_chart(line_chart, "E1")

wb.save("sample_chart.xlsx")