# import dependencies
from bs4 import BeautifulSoup

with open('export.xml', 'r') as f:
    data = f.read()

bs_data = BeautifulSoup(data, 'xml')

b_hr = bs_data.find(type='HKQuantityTypeIdentifierHeartRate')

print(b_hr['value'])
print(b_hr['unit'])
print(b_hr['startDate'])