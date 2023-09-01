from bs4 import BeautifulSoup
from fileInformation import xamlFile


# file path to open
filePath = '/Users/everchicas/GIT/ReadPath/test/ActivacionEquiposServiciosFijosGT/Main.xaml'
with open(filePath, 'r') as f:
	data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, "xml")

# Finding all instances of tag
# x:Property
b_propertys = Bs_data.find_all('x:Property')

# Show arguments name
for member in b_propertys:
	#name = member.get('Name')
	#nameTag = BeautifulSoup(member,'xml.parser')
	print(member.get('Name'))

