import requests
import pprint, json

headers={'X-Access-Token': '4a13a90be2124925'}


locat = requests.get('http://freegeoip.net/json/').json()

lat = locat['latitude']
lon = locat['longitude']

url = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?latitude={}&longitude={}&method=both'.format(str(lat), str(lon))
response = requests.get(url, headers=headers).json()

# temp = response['restaurants'][81]['apiKey']

# print(str(len(temp)) + '\n ' + str(temp))
# print(temp)
file = open('Rutgers_res.txt','r+')
# for key in range(0, len(response['restaurants'])):
#     temp = response['restaurants'][key]['apiKey'] + '\n'
#     file.write(temp)
    # print(temp)

# file.close()
arr = file.readlines()

for i in range(0, len(arr)):
    arr[i] = arr[i].replace("\n", "")
    menu = 'https://api.eatstreet.com/publicapi/v1/restaurant/{}/menu?includeCustomizations=false'.format(arr[i])
    menu_response = requests.get(menu, headers=headers).json()
    for j in range(0, len(menu_response)):
        for k in menu_response[j]['items']:
            if 'description' not in k:
                print("Name: " +  k['name'] + "  |  " + "Price: " + str(k['basePrice']))
            else:
                print("Name: " +  k['name'] + "\nPrice: " + str(k['basePrice']) + "\nDescriptions: " + str(k['description']) + '\n')


# pprint.pprint(response)


