import sys
import shutil

shutil.unpack_archive('wordlist.zip')

# loeb .txt fail ja esitab sisu jadas.
file = open('wordlist.txt', 'r')
listFromFile = file.read().split()

# sisestab otsitavad s6nad ja esitab jadas.
print('Sisesta otsitavad s6nad: ')
scrambledWords = sys.stdin.read().split()

# sorteerib t2hed s6nades ja v6rdleb, lisab jadasse
matchedWords = []

for word1 in scrambledWords:
	word11 = sorted(word1)
	for word2 in listFromFile:
		# kontrollib, kas string on sama pikk. kui ei ole, j2tab vahele - s22stab aega
		if (len(word1) == len(word2)):
			word22 = sorted(word2)
			if(word11 == word22):
				matchedWords.append(word2)
		

answer = ', '.join(matchedWords)
print(answer)

