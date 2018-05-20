from xml.etree import ElementTree as ET

tree = ET.parse('E:/xhy_python/data-wrangling-master/data/chp3/data-text.xml')
root = tree.getroot()
print root
print dir(root)
print list(root)

data = root.find('Data')
print list(data)
all_data = []
for observation in data:
    recode = {}
    for item in observation:
        lookup_key = item.attrib.keys()[0]
        if lookup_key == 'Numeric':
            rec_key = 'Numeric'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        print rec_key, rec_value
        recode[rec_key] = rec_value
    all_data.append(recode)
print all_data

