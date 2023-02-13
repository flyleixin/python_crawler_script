from openpyxl import load_workbook

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'

}


def data():
    workbook = load_workbook(filename="01.xlsx")  # 加载excel文件
    sheet = workbook['Sheet1']  # 获取工作表对象

    tmp_list = [0, 0, 1]
    print(tmp_list)
    sheet.append(tmp_list)
    workbook.save("01.xlsx")


if __name__ == '__main__':
    data()
