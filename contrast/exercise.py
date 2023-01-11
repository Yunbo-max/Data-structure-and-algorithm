import os
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用


def getfilelist(filepath):
    filelist = os.listdir(filepath)  # 获取filepath文件夹下的所有的文件
    print(filelist)
    print(len(filelist))
    files = []
    for i in range(len(filelist)):
        child = os.path.join('%s\\%s' % (filepath, filelist[i]))
        # child=filelist[i]
        if os.path.isdir(child):
            file_list = [i.split('\\')[-1].split('.')[0] for i in getfilelist(child)]
            files.extend(file_list)

        else:
            files.append(child)
    return files


# filepath = "D:\\Documents\\Desktop\\书籍\\2020论文分类下载\\2020论文分类下载"
# print(getfilelist(filepath))

def write2excel(filelist):
    for i, element in enumerate(filelist):
        ws.append([i, element, '', '', '', ''])


if __name__ == "__main__":
    #  创建Excel表并写入数据
    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 获取当前正在操作的表对象
    # 往表中写入标题行,以列表形式写入！
    ws.append(['序号', '论文标题（英文）', '论文标题（中文）', '所属分类', '年份', '备注'])
    filepath = "E:\\desk\\Uob\\semester 2\\BIA"
    filelist = getfilelist(filepath)
    write2excel(filelist)
    wb.save('paper.xlsx')
