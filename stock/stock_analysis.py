import urllib, json
import sys
import urllib.request
import pandas as pd
import datetime as dt


#'http://quotes.money.163.com/service/chddata.html?code=0601857&start=20180101&end=20180818&fields=TCLOSE;PCHG;TCAP;MCAP', encoding='gbk')
data = pd.read_csv('C:\\Users\\Stella\\OneDrive\\PythonProject\\hws\\stock\\stock_names.csv', encoding='gbk')
data_sz = pd.read_csv('C:\\Users\\Stella\\OneDrive\\PythonProject\\hws\\stock\\sz_stock_names.csv', converters={'公司代码': lambda x: str(x)})
stock_names_sz = data_sz["公司代码"].values.tolist()
#print(type(data[['公司代码 ']]))
print(data_sz["公司代码"].values.tolist()[0])
stock_names = data["公司代码 "].values.tolist()

new_issue_stock_name = []
print(len(data_sz))
for i in range(len(data_sz)):
    if dt.datetime.strptime(data_sz['A股上市日期'].values[i],'%Y-%m-%d') > dt.datetime.strptime('2017-01-01','%Y-%m-%d'):
        new_issue_stock_name.append(data_sz['公司代码'].values[i])


print(dt.datetime.strptime(data['A股上市日期'].values[0].strip(),'%Y-%m-%d').date() )
print( dt.datetime.strptime('2017-01-01','%Y-%m-%d').date())

for i in range(len(data)):
    if(len(data['A股上市日期'].values[i].strip())) < 2:
        continue;

    if dt.datetime.strptime(data['A股上市日期'].values[i].strip(),'%Y-%m-%d') > dt.datetime.strptime('2017-01-01','%Y-%m-%d'):
        new_issue_stock_name.append(data['公司代码 '].values[i])


print(len(new_issue_stock_name))


stock_name_with_mcap_match = []
count = 0
for stock in stock_names[:2]:
    stock_data_url = 'http://quotes.money.163.com/service/chddata.html?code='+'0' + str(stock)+'&start=20180821&end=20180821&fields=MCAP'
    #print(stock_data_url)
    stock_data_val = pd.read_csv(stock_data_url, encoding='gbk')
    stock_cur_mcap = stock_data_val["流通市值"].values[0]
    #print(stock_cur_mcap)
    count = count + 1
    #print(count)
    if stock_cur_mcap <= 5000000000:
        stock_name_with_mcap_match.append(stock)

print('list of stock names with mcap < 5 billion')
print(stock_name_with_mcap_match)
