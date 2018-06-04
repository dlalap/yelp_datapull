from google.cloud import language


# content = 'This is an amazing addition to the area!  Counter service during the day and table service in evenings.  The food is simple, well-executed, and delicious.  The space itself is beautiful, with high open ceilings, tall glass windows, and simply decorated with tons of natural light and plants.'
# content2 = '''I dined here last night (Saturday, 9/16) with my mother, her friend, and my girlfriend. My mother used to dine there quite often back in her day and was excited and nostalgic to go back. FIrst of all, the food was bland. This is the first time I've ordered Scallops and not been happy. They were unusually chewy and simply NOT good. Then I had the King Crab and was unhappy as well, but that was more of a subjective matter of personal taste. Up until then our waiters had both been courteous and professional.'''
# content3 = 'The crab is okay.'

# content4 = '''Although the service was excellent, the food was TERRIBLE. I haven't been to a Chinese restaurant in the city that was so lacking in flavor in the dishes. I tasted literally everything and there was not one thing that really excited my taste buds. Even the ambience is not worth the price you put to dine here.'''
# content5 = '''The setting was a bit congested and it felt stuffy!
# The service was great  
# The food Wasn't good in my opinion ... I enjoyed the soup and my appetizer... where as the main dish looked and tasted too westernized.... so it was basically too expensive for a bad food lol

# All in all this is a place to look forward a good service only!'''

# chowReviews = (content4, content5)
occurances = {}
wordScoreList = {} # {'word':(1, 2, 3, 4, 5)}
wordMagnitudeList = {}
wordSentiment = {} # {'word1':{'Score':(1, 2, 3, 4, 5), 'Magnitude':(1, 2, 3, 4, 5)}}
# 				   # {'word1':{'Score':wordScoreList['word1'], 'Magnitude':wordMagnitudeList['word1']}, ...}


def occuranceUpdate(word):
	global occurances
	try:
		occurances[word] += 1
	except KeyError:
		occurances.update({word:1})

def scoreListUpdate(word, value=[]):
	global wordScoreList
	word = word.lower()
	try:
		wordScoreList[word] = wordScoreList[word] + [value,]
	except KeyError:
		wordScoreList.update({word:[value]})
	return 0

def magnitudeListUpdate(word, value=[]):
	global wordMagnitudeList
	word = word.lower()
	try:
		wordMagnitudeList[word] = wordMagnitudeList[word] + [value,]
	except KeyError:
		wordMagnitudeList.update({word:[value]})
	return 0

def wordSentimentUpdate(word, type, value):
	global wordSentimentUpdate
	try:
		wordSentiment[word][type] = wordSentiment[word][type],[value]
	except KeyError:
		wordSentiment.update({word:{}})

def avgWordValue(list):
	avg = sum(list)/len(list)
	return avg

def sumWordValue(list):
	sumVal = sum(list)
	return sumVal

def analyzeThis(contentInput):
	document = language.types.Document(
		content = contentInput,
		language = 'en',
		type = 'PLAIN_TEXT'
		)
	client = language.LanguageServiceClient()
	response = client.analyze_entity_sentiment(document = document, encoding_type='UTF32')
	entities = response.entities
	
	for entity in entities:
		occuranceUpdate(entity.name)

		print(entity.name)
		print(entity.sentiment.score)
		print(entity.sentiment.magnitude)

		scoreListUpdate(entity.name, entity.sentiment.score)
		magnitudeListUpdate(entity.name, entity.sentiment.magnitude)
	# compileSentiments()
	return 0

def printEntity(printInput):
	# print printInput[3].name
	# print printInput[3].sentiment.score
	# print printInput[3].sentiment.magnitude
	print('\n')
	for entity in printInput:
		print(str(entity.name) + ": sentiment score = " + str(entity.sentiment.score) + ", sentiment magnitude = " + str(entity.sentiment.magnitude))
		# print(entity)

def compileSentiments():
	global wordSentiment
	for word in wordScoreList.keys():
		wordSentiment.update({word:{'Score':wordScoreList[word],'Magnitude':wordMagnitudeList[word]}})
	return wordSentiment

# print("\n\n")

# for entity in entities:
# 	print(str(entity.name) + ": sentiment score = " + str(entity.sentiment.score))

# print entities[0].name
# print entities[3].name
# print entities[3].sentiment.score
# print entities[3].sentiment.magnitude


# printEntity(analyzeThis(content))
# printEntity(analyzeThis(content2))
# printEntity(analyzeThis(content3))

# for chows in chowReviews:
# 	printEntity(analyzeThis(chows))

# for word in occurances:
# 	print(word + ': ' + str(occurances[word]))

# print('wordScoreList \n')
# for word in wordScoreList.keys():
# 	print(word)
# 	print(wordScoreList[word])
# 	print(occurances[word])
# print('\n\n')
# print('wordMagnitudeList \n')
# for word in wordMagnitudeList.keys():
# 	print(word)
# 	print(wordMagnitudeList[word])
# 	print(occurances[word])

# print(wordSentiment)
# for word in wordScoreList.keys():
# 	wordSentiment.update({word:{'Score':wordScoreList[word],'Magnitude':wordMagnitudeList[word]}})

# print(wordSentiment)