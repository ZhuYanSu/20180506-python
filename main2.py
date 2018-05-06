from urllib.request import urlopen
import json

year = input('Choose a year: ')
for month in range(1, 13):
    url = 'https://www.google.com/doodles/json/'+year+'/'+ str(month)+'?hl=zh_TW'
    response = urlopen(url)
    doodles = json.load(response)
    for doodle in doodles:
        img_url = 'https:' + doodle['url']
        print(img_url)
        response = urlopen(img_url)
        img_data = response.read()

        #     list[-1] = list[list.len-1]
        file_name = 'result_2017/' + img_url.split('/')[-1]
        f = open(file_name, 'wb')
        f.write(img_data)
        f.close()



