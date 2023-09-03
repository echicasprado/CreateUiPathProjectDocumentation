from bs4 import BeautifulSoup
from fileInformation import xamlFile


TestFilePath = [
	'/Users/everchicas/GIT/ReadPath/test/UseReThrow/Test/Flowchart.xaml',
	'/Users/everchicas/GIT/ReadPath/test/UseReThrow/Test/Sequence.xaml',
	'/Users/everchicas/GIT/ReadPath/test/UseReThrow/Test/StateMachine.xaml',
	'/Users/everchicas/GIT/ReadPath/test/UseReThrow/Test/Workflow.xaml',
 	'/Users/everchicas/GIT/ReadPath/test/UseReThrow/Test/WorkflowWithTemplate.xaml'
]

def openFile(filePath):
	with open(filePath, 'r') as f:
		data = f.read()
	return BeautifulSoup(data, "xml")
 
def getDescription(XML_DATA):
	FILES_TYPE_UIPATH = ["Flowchart","StateMachine","Sequence"]
 
	for currentType in FILES_TYPE_UIPATH:
		currentFileType = XML_DATA.find(currentType)
		if(currentFileType == None):
			continue
		else:
			# print("###########################")
			# print(f'Current file type: {currentType}\nContent: {currentFileType.get("sap2010:Annotation.AnnotationText")}')
			# print("###########################")
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
	for temp in TestFilePath:
		print('-----------------------------------------')
		main(temp)
		print('-----------------------------------------')