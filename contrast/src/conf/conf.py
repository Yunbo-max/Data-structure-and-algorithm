# -*- coding: utf-8 -*-  

conf = {
	
	# 要对比的表格 不能超过2个
	'class_sheet' : {
		'class1' : './src/conf/labeldata07091821-源文件.xls',
		'class2' : './src/conf/labeldata07091821汇总.xls'
	},

	# 工作表名称
	#'sheet_name': 'Sheet1',
	'sheet_name': 'data',

	# 对比表的前缀
	'contrast_profix':'对比结果',

	# 保存路径
	'save_path' : './src/conf/{}_contrast.xls'
	
}