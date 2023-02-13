import requests
from openpyxl import load_workbook

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'

}


def data():
    workbook = load_workbook(filename="01.xlsx")  # 加载excel文件
    sheet = workbook['Sheet1']  # 获取工作表对象
    # print(sheet)
    group_id = '94'
    last = 91
    for page_num in range(1, last):
        url = 'http://tools.2345.com/frame/sundry/heatSearchAjax?groupId=' + group_id + '&page=' + str(last)
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        page_text = response.text
        print(page_text)
    # time.sleep(10000)
    # for page_num in range(1, 11):
    #     if page_num == 1:
    #         url = 'https://www.boohee.com/food/view_menu'
    #     else:
    #         url = 'https://www.boohee.com/food/view_menu?page=' + str(page_num)
    #     time.sleep(0.5)
    #     response = requests.get(url=url, headers=headers)
    #     response.encoding = 'utf-8'
    #     page_text = response.text
    #     # print(page_text)
    #     tree = etree.HTML(page_text)
    #     # 每一个li
    #     li_list = tree.xpath('//*[@id="main"]/div/div[2]/ul/li')
    #     for li in li_list:
    #         # 局部解析
    #         url = li.xpath('./div[1]/a/img/@src')[0]
    #         title = li.xpath('./div[2]/h4/a/@title')[0]
    #         heat = li.xpath('./div[2]/p/text()')[0]
    #         pattern = re.compile(r'(?<=热量：)\d+\.?\d*')
    #         heat_num = pattern.findall(heat)[0]
    #         tmp_list = [title, heat_num, url]
    #         print(tmp_list)
    #         sheet.append(tmp_list)
    # workbook.save('菜肴.xlsx')


if __name__ == '__main__':
    data()
