import re
from lxml import html
import requests
from openpyxl import load_workbook

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
}


def data():
    urls = 'http://tools.2345.com/m/reliang/'
    responses = requests.get(url=urls, headers=headers)
    responses.encoding = 'gbk'
    result_html = html.etree.HTML(
        responses.content, parser=html.etree.HTMLParser(encoding='gbk'))
    print(result_html)
    tree = result_html
    li_list = tree.xpath('/html/body/div[1]/section[2]/div/ul/li')
    for li in li_list:
        url = li.xpath('./a/@href')[0]
        excel_name = li.xpath('./a/text()')[0]
        workbook = load_workbook(filename="01.xlsx")  # 加载excel文件
        sheet = workbook['Sheet1']  # 获取工作表对象
        pattern = re.compile(r'(?<=list)\d+\.?\d*')
        group_id = str(pattern.findall(url)[0])
        last = 100
        print(excel_name)
        print(group_id)
        for page_num in range(1, last + 1):
            url = 'http://tools.2345.com/frame/sundry/heatSearchAjax?groupId=' + group_id + '&page=' + str(page_num)
            # print(url)
            response = requests.get(url=url, headers=headers)
            response.encoding = 'utf-8'
            page_text = response.json()
            if page_text['status'] == 'max':
                break
            for dic in page_text['data']:
                tmp_list = [dic['name'], dic['reliang']]
                sheet.append(tmp_list)
        workbook.save(excel_name + '.xlsx')


if __name__ == '__main__':
    data()
