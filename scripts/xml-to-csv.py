import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../class-data/armor.xml")
root = tree.getroot()

# open a file for writing
csv_data = open('exported-data.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(csv_data)
csv_head = []

count = 0
for child in root[0]:
  print('--->', child.tag, child.attrib.get('name'))

  child_data = []

  if count == 0:
    csv_head.append('id')
    csv_head.append('name')
    csv_head.append('weight')
    csv_head.append('cost')
    csvwriter.writerow(csv_head)
    count = count + 1

  child_data.append(child.tag)
  child_data.append(child.attrib.get('name'))
  child_data.append(child.attrib.get('weight').replace('lbs', ''))
  child_data.append(child.attrib.get('cost'))
  csvwriter.writerow(child_data)

csv_data.close()