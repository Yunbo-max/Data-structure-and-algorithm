# -*- coding: utf-8 -*- 
# author SDM
# time 2021-07-14 

import xlwt
import xlrd
from src.conf.conf import conf

# --------------------------------------------------------
# 对比两表数据 并将数据写入新excel文件
# 第一份与第二份对比  第二份中不同于第一份中的数据填充为黄色
# 以最小行列进行对比  多出的部分丢弃 小于的部分会被包括
# ---------------------------------------------------------
def contrast_write():

	# 获取两份表的行列最小值 避免下标超出
	min_rows = -1
	min_cols = -1

	excel_datas = []

	for k, v in conf['class_sheet'].items():
		data = xlrd.open_workbook(v)

		sheet = data.sheet_by_name(conf['sheet_name']) 
		excel_datas.append(sheet)

	for v in excel_datas:

		if min_rows == -1 or min_cols == -1:
			min_rows = v.nrows
			min_cols = v.ncols
		else:
			if v.nrows < min_rows :
				min_rows = v.nrows

			if v.ncols < min_cols:
				min_cols = v.ncols

	#print('min_rows{} min_cols{}'.format(min_rows, min_cols))
	if min_rows <= 0 or min_cols <= 0:
		raise Exception('表格行列数值异常')
		return
		
	workbook = xlwt.Workbook()
	worksheet = workbook.add_sheet('Sheet1')

	pattern = xlwt.Pattern()

	# pattern style is NO_PATTERN SOLID_PATTERN 0x00 through 0x12
	pattern.pattern = xlwt.Pattern.SOLID_PATTERN 
	
	# may be 8 through 63
	# 0 black 1 white 2 red 3 green 4 blue 5 yellow 6 magenta 7 cyan 
	# pattern.pattern_fore_colour = xlwt.Style.colur_map['red']
	pattern.pattern_fore_colour = 5
	style = xlwt.XFStyle()	# create style
	style.pattern = pattern # pattern to style

	# read contrast and write
	for r in range(0, min_rows):

		for c in range(0, min_cols):

			print('正在对比 {}行 {}列'.format(r, c))
			if excel_datas[0].cell(r, c).value != excel_datas[1].cell(r, c).value:
				worksheet.write(r, c, excel_datas[1].cell(r, c).value, style)
			else:
				worksheet.write(r, c, excel_datas[1].cell(r, c).value)

	workbook.save(conf['save_path'].format(conf['contrast_profix']))

def run():
	contrast_write()

if __name__ == '__main__':
	run()