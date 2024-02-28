from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import re
import pprint
import json


url = 'https://www.stubhub.com/taylor-swift-miami-tickets-10-18-2024/event/152129101/'
static_file = './tswift.html'
urlretrieve(url, static_file)

with open(static_file, 'r') as f:
    html_page = f.read()

soup = BeautifulSoup(html_page, 'html.parser')
res = soup.find('script', id='index-data')
json_object = json.loads(res.contents[0])

# Ranges in Miami concert
seat_ranges = {
    '594': ('128491', '1133475'),
    '1724': ('128491', '149352'),
    '1724': ('128491', '149352'),
    '407': ('1135262', '1135294'),
}

look_for_qty = 3

for section in json_object['listingInfoBySection']:
    section_parts = section.split('_')
    group_section = section_parts[0]
    main_section = section_parts[1]
    if group_section in seat_ranges \
        and int(main_section) >= int(seat_ranges[group_section][0]) \
        and int(main_section) <= int(seat_ranges[group_section][1]) \
        and int(json_object['listingInfoBySection'][section]['count']) >= look_for_qty:
        #print(json_object['listingInfoBySection'][section])
        print(f"Section: {section}")
        print(f"Qty: {json_object['listingInfoBySection'][section]['count']}")
        print(f"Price: {json_object['listingInfoBySection'][section]['formattedMinPrice']}")
        print("")