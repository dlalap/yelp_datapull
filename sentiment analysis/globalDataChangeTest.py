globalVar = 10

def changeGloVar():
	resultsToAppend = []
	for i in range(1,11):
		resultsToAppend.append(unicode(i))
	print resultsToAppend

results = changeGloVar()
# globalVar.append(results)
print globalVar	
