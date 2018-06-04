# Sentiment Analysis v0.1
# by Dean Lalap
# (c) 2017

import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# def analyze(food_review):
# 	"""Run a sentiment analysis request on text within a passed filename."""
# 	client = language.LanguageServiceClient()

# 	with open(food_review, 'r') as review_file:
# 		# Instantiates a plain text document.
# 		content = review_file.read()

# 	document = types.Document(content = content, type = enums.Document.Type.PLAIN_TEXT)
# 	annotations = client.analyze_sentiment(document = document)
# 	print_result(annotations)

def analyze(food_review):
	client = language.LanguageServiceClient()
	document = types.Document(content = food_review, type = enums.Document.Type.PLAIN_TEXT)
	annotations = client.analyze_sentiment(document = document)
	return print_result(annotations) 

def print_result(annotations):
	resultValues = {}
	score = annotations.document_sentiment.score
	magnitude = annotations.document_sentiment.magnitude

	for index, sentence in enumerate(annotations.sentences):
		sentence_sentiment = sentence.sentiment.score
		# print('Sentence "{}" has a sentiment score of {}'.format(sentence.text.content, sentence_sentiment))
		print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))
		resultValues[index] = sentence_sentiment
	print('Overall Sentiment: score of {} with a magnitude of {}'.format(score, magnitude))
	return score, magnitude, resultValues

# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser(
# 		description=__doc__,
# 		formatter_class=argparse.RawDescriptionHelpFormatter)
# 	parser.add_argument(
# 		'food_review',
# 		help='The filename of the Yelp review you\'d like to analyze.')
# 	args = parser.parse_args()

# 	analyze(args.food_review)