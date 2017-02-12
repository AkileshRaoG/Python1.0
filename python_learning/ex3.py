from urllib import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

print WORDS
