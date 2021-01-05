# coding=utf-8
import csv


csv_data = (
    (1, 2, 3, 4, 5, 6),
    ('a', 'b', 'c', 'd', 'e', 'f'),
    ('p', 'y', 't', 'h', 'o', 'n')
)
output_file_name = 'csv_file.csv'


def save_csv(target_list, output_file_name):
    """
    将数据写入csv文件
    """
    if not output_file_name.endswith('.csv'):
        output_file_name += '.csv'
    csv_file = open(output_file_name, "w", newline="")
    key_data = target_list[0]
    value_data = [target for target in target_list]
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(key_data)
    csv_writer.writerows(value_data)
    csv_file.close()


# save_csv(csv_data, output_file_name)


# coding=utf-8
import csv


input_file_name = 'csv_file.csv'


def read_csv(input_file_name):
    """
    读取csv文件数据
    """
    with open(input_file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        # csv_reader对象，是一个列表的格式
        print(csv_reader)
        # csv_reader对象的一个迭代器，可以通过next()取出其中的元素
        print(next(csv_reader))
        # 也可以通过for循环取出所有元素
        for line in csv_reader:
            print(''.join(line))


read_csv(output_file_name)
