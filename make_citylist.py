import re, json

with open('city.txt','r',encoding='utf-8') as f:
    all_list = f.readlines()

mdcg = {'北京市', '上海市', '天津市', '重庆市'}
province, city, county = '', '', ''
province2city, city2county, county2city, city2province = {}, {}, {}, {}
for i in all_list:
    i = i.lstrip(' ').rstrip('\n').rstrip(' ')

    if i in mdcg:
        province, city = i, i
        province2city[i] = i
        city2province[i] = i
        continue

    elif '—' in i:
        province, city = i.split('—')
        try:
            province2city[province].extend([city])
        except KeyError:
            province2city[province] = [city]
        city2province[city] = province
        continue

    else:
        county = i.split(' ')
        try:
            city2county[city].extend(county)
        except KeyError:
            city2county[city] = county

        for j in county:
            county2city[j] = city

with open('province2city.json','w', encoding='utf-8') as fpc:
    json.dump(province2city, fpc, ensure_ascii=False)
with open('city2county.json', 'w', encoding='utf-8') as fco:
    json.dump(city2county, fco, ensure_ascii=False)
with open('county2city.json', 'w', encoding='utf-8') as foc:
    json.dump(county2city, foc, ensure_ascii=False)
with open('city2province.json', 'w', encoding='utf-8') as fcp:
    json.dump(city2province, fcp, ensure_ascii=False)

