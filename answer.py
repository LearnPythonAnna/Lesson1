def get_answer(question):
	answers = {'hi': "hi you", 'how are you':'best of all', 'buy': 'see you'}
	return answers[question.lower()]

print(get_answer('Hi'))