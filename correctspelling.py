from textblob import TextBlob
sentence = TextBlob('I havv a bad spelling ')
print(sentence.correct())
language = TextBlob('Bonjour')
print(language.detect_language())