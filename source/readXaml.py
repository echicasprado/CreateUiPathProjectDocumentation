from bs4 import BeautifulSoup
from fileInformation import xamlFile

FILES_TYPE_UIPATH = ["Flowchart","StateMachine","Sequence"]
XML_DATA = None

# file path to open
TestFilePath = '/Users/everchicas/GIT/ReadPath/test/ActivacionEquiposServiciosFijosGT/Main.xaml'
#with open(filePath, 'r') as f:
#	data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
#Bs_data = BeautifulSoup(data, "xml")

# Finding all instances of tag
# x:Property
# b_propertys = Bs_data.find_all('x:Property')
#b_type = Bs_data.find("Flowchart")

# for currentType in FILES_TYPE_UIPATH:
# 	CURRENT_FILE_TYPE = Bs_data.find(currentType)
# 	if(CURRENT_FILE_TYPE == None):
# 		continue
# 	else:
# 		print("###########################")
# 		print(f'Current file type: {currentType}\nContent: {CURRENT_FILE_TYPE.get("sap2010:Annotation.AnnotationText")}')
# 		print("###########################")
# 		break

# Show arguments name
#for member in b_propertys:
	#name = member.get('Name')
	#nameTag = BeautifulSoup(member,'xml.parser')
	#print(member.get('Name'))

def openFile(filePath):
	with open(filePath, 'r') as f:
		data = f.read()
	return BeautifulSoup(data, "xml")
 
def getDescription(XML_DATA):
	for currentType in FILES_TYPE_UIPATH:
		currentFileType = XML_DATA.find(currentType)
		if(currentFileType == None):
			continue
		else:
			print("###########################")
			print(f'Current file type: {currentType}\nContent: {currentFileType.get("sap2010:Annotation.AnnotationText")}')
			print("###########################")
			return currentFileType.get("sap2010:Annotation.AnnotationText")

def getArguments(XML_DATA):
	arrayProperty = []
	currentArguments = XML_DATA.find_all('x:Property')
	for arg in currentArguments:
		arrayProperty.append(arg.get('Name'))
	return arrayProperty
	
def main(filePath):
	XML_DATA = openFile(filePath)
	informationXaml = xamlFile("","",[])
	informationXaml.description = getDescription(XML_DATA)
	informationXaml.arguments = getArguments(XML_DATA)
	informationXaml.path = filePath
	print(str(informationXaml))
    
if __name__ == "__main__":
	main(TestFilePath)