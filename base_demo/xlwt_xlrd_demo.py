# coding=utf-8
import xlwt


xlwt_data = [
    ('有', '人', '云', '淡', '风', '轻'),
    ('有', '人', '负', '重', '前', '行'),
    ('p', 'y', 't', 'h', 'o', 'n')
]
output_file_name = 'xlwt_file.xls'


def save_excel(target_list, output_file_name):
    """
    将数据写入xls文件
    """
    if not output_file_name.endswith('.xls'):
        output_file_name += '.xls'
    workbook = xlwt.Workbook(encoding='utf-8')
    ws = workbook.add_sheet("sheet1")
    title_data = ('a', 'b', 'c', 'd', 'e', 'f')
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            ws.write(i, j, target_list[i][j])
    workbook.save(output_file_name)


# save_excel(xlwt_data, output_file_name)


import xlrd


input_file_name = 'xlwt_file.xls'


def read_excel(input_file_name):
    """
    从xls文件中读取数据
    """
    workbook = xlrd.open_workbook(input_file_name)
    print(workbook)
    # 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
    print(workbook.sheet_names())
    # 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
    # table = workbook.sheet_by_index(0)
    # print(table)
    table = workbook.sheet_by_name('sheet1')
    print(table)
    # 通过nrows和ncols获取到表格中数据的行数和列数
    rows = table.nrows
    cols = table.ncols
    # 可以通过row.values()按行获取数据，返回一个列表，也可以按列
    for row in range(rows):
        row_data = table.row_values(row)
        print(''.join(row_data))
    # for col in range(cols):
    #     col_data = table.col_values(col)
    #     print(''.join(col_data))
    # 也可以根据单元格获取每一个单元格的数据
    for row in range(rows):
        for col in range(cols):
            data = table.cell(row, col).value
            print(data, end=' ')


read_excel(input_file_name)
