import wikipedia
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import nltk
import pyphen

dic = pyphen.Pyphen(lang='nl_NL')

ps = PorterStemmer()

data = str(wikipedia.summary("frog"))


def isComplexWord(word):
    # Rejects proper nouns
    pos = nltk.pos_tag([word])

    if pos[0][1] == 'NNS' or pos[0][1] == 'NNP' or pos[0][1] == 'NNPS':
        return False

    # removes "ing" and similar suffixes, seems unnecessary for now.
    #stem = ps.stem(word)

    hyphenated = dic.inserted(word)
    syllables = 1 + hyphenated.count('-')
    return syllables >= 3


def fogIndex(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    numWord = len(words)
    numSent = len(sentences)

    numComplex = 0
    for word in words:
        if isComplexWord(word):
            numComplex += 1

    return 0.4 * ((numWord/numSent) + 100 * (numComplex / numWord))


print(fogIndex(data))
