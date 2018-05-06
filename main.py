from facebook import GraphAPI
from urllib.request import urlopen
import json

# MAC OS + python 3.6 之 bug
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

token = "EAACEdEose0cBAHLgrL4Oo42rysHnHSim9LadAAm5UzBka8NfI4LfTJeuZA9TjwytXacLq1AcD2ZA1fup14pmfOpf2kYZBMmiFZC6wOZC6RTKZBFmyu8CoYpCjHCZB77rCZAIUPPwAC29PA9FA4oA7rZA0uUXbeT8byosv97PYD8KuZCMSBLW0tWPfWowo0qL5pRmVq4uFG4FEh8gZDZD"

g = GraphAPI(access_token= token)

# 4. COUNTER
index = 0
# print(g.get_connections("me", "likes"))
page = g.get_connections("me", "likes")

# 2. 無窮迴圈 不知怎麼寫先Run 試試看
while True:
    for fan_page in page['data']:
        index = index + 1
        print(index, fan_page['name'])
    # 3. 出事了再處理 此時也等於讀完了
    try:
        url = page['paging']['next']
        print(url)
        response = urlopen(url)
        print(response)
        #  1. 把現在頁面改成下一頁
        page = json.load(response)
    except KeyError:
        print("ENNNNNNNND")
        break





