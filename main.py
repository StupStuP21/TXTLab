# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import stanza
from pyvis import network as net
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def GetText(fileName):
    file = open(fileName,'r')
    text = file.read()
    return text

def SplitTextOnSentecnces(text):
    return sent_tokenize(text)



def TextSplittingForSentences(text):
    listOfSenteces = text.split('.')
    return listOfSenteces

def TextSplittingForWords(listOfSenteces):
    listOfWords = []
    for i in listOfSenteces:
        listOfWords.append(i.split())
    return listOfWords

def GetCountOfWordsInText(listOfWords):
    count=0
    for i in listOfWords:
        count+=len(i)
    return count

def GetListOfInvisibleWords():
    fileOfInvisibleWords = open('служебные части речи (список).txt', 'r')
    listOfInvisibleWords = fileOfInvisibleWords.read()
    listOfInvisibleWords = listOfInvisibleWords.split('\n')
    return listOfInvisibleWords

def GetMaxAndMinWords(listOfWords):
    listOfInvisibleWords = GetListOfInvisibleWords()
    minWord = listOfWords[0][0]
    maxWord = listOfWords[0][0]
    for i in listOfWords:
        for j in i:
            if (j not in listOfInvisibleWords):
                if (len(j)<len(minWord)):
                    minWord = j
                elif (len(j)>len(maxWord)):
                    maxWord = j
    return minWord,maxWord

def GetMeanOfWord(listOfWords):
    countOfCharsInAllWords=0
    countOfWords=0
    for i in listOfWords:
        for j in i:
            countOfCharsInAllWords+=len(j)
            countOfWords+=1
    meanOfWord = countOfCharsInAllWords/countOfWords
    return meanOfWord

def GetMeanOfLenghtSentences(listOfWords):
    countOfSentences = len(listOfWords)
    countOfWordsInAllSentences = 0
    for i in listOfWords:
        for j in i:
            countOfWordsInAllSentences+=1
    mean = countOfWordsInAllSentences/countOfSentences
    return mean

def GetMeadianLenghtOfWords(listOfWords):
    arrayOfWords = []
    for i in listOfWords:
        arrayOfWords = arrayOfWords + i
    arrayOfWords.sort(key = lambda x: len(x))
    meanIndex = len(arrayOfWords)//2
    MeadianLenght = len(arrayOfWords[meanIndex])
    return MeadianLenght

def GetMedianLenghtOfSentences(listOfWords):
    arrayOfSentences = listOfWords.copy()
    arrayOfSentences.sort(key = lambda x: len(x))
    meanIndex = len(arrayOfSentences) // 2
    MeadianLenght = len(arrayOfSentences[meanIndex])
    return MeadianLenght

def GetListOfWordsByStartChar(listOfWords,firstChar):
    arrayOfWords = []
    for i in listOfWords:
        for j in i:
            if (j.startswith(firstChar.lower()) or j.startswith(firstChar.upper())):
                arrayOfWords.append(j)
    return arrayOfWords

def GetResultForTxt(fileName):
    print('Текстовый файл:')
    text = GetText(fileName)
    sentences = TextSplittingForSentences(text)
    words = TextSplittingForWords(sentences)
    # print(words)
    countOfWords = GetCountOfWordsInText(words)
    print('Кол-во слов в тексте: ', countOfWords)
    minWord, maxWord = GetMaxAndMinWords(words)
    print('Самое короткое слово: ', minWord)
    print('Самое длинное слово: ', maxWord)
    meanOfWords = GetMeanOfWord(words)
    print('Средняя длина слов: ', meanOfWords)
    medianOfWords = GetMeadianLenghtOfWords(words)
    print('Мединная длина слов: ', medianOfWords)
    meanOfSenteces = GetMeanOfLenghtSentences(words)
    print('Средняя длина предложений: ', meanOfSenteces)
    medianOfSentences = GetMedianLenghtOfSentences(words)
    print('Медианная длина предложений: ', medianOfSentences)
    firstChar = input('Введите символ начала: ')
    arrayOfStartedWithWords = GetListOfWordsByStartChar(words, firstChar)
    print(arrayOfStartedWithWords)
    return words

def fdsfsf(splittedText):
    nlp = stanza.Pipeline(lang='ru', processors='tokenize,pos,lemma,ner,depparse')
    triplets = []
    for s in tqdm(splittedText):
        doc = nlp(s)
        for sent in doc.sentences:
            entities = [ent.text for ent in sent.ents]
            res_d = dict()
            temp_d = dict()
            for word in sent.words:
                temp_d[word.text] = {"head": sent.words[word.head - 1].text, "dep": word.deprel, "id": word.id}
            for k in temp_d.keys():
                nmod_1 = ""
                nmod_2 = ""
                if (temp_d[k]["dep"] in ["nsubj", "nsubj:pass"]) & (k in entities):
                    res_d[k] = {"head": temp_d[k]["head"]}

                    for k_0 in temp_d.keys():
                        if (temp_d[k_0]["dep"] in ["obj", "obl"]) & \
                                (temp_d[k_0]["head"] == res_d[k]["head"]) & \
                                (temp_d[k_0]["id"] > temp_d[res_d[k]["head"]]["id"]):
                            res_d[k]["obj"] = k_0
                            break

                    for k_1 in temp_d.keys():
                        if (temp_d[k_1]["head"] == res_d[k]["head"]) & (k_1 == "не"):
                            res_d[k]["head"] = "не " + res_d[k]["head"]

                    if "obj" in res_d[k].keys():
                        for k_4 in temp_d.keys():
                            if (temp_d[k_4]["dep"] == "nmod") & \
                                    (temp_d[k_4]["head"] == res_d[k]["obj"]):
                                nmod_1 = k_4
                                break

                        for k_5 in temp_d.keys():
                            if (temp_d[k_5]["dep"] == "nummod") & \
                                    (temp_d[k_5]["head"] == nmod_1):
                                nmod_2 = k_5
                                break
                        res_d[k]["obj"] = res_d[k]["obj"] + " " + nmod_2 + " " + nmod_1

            if len(res_d) > 0:
                triplets.append([s, res_d])
    clear_triplets = []
    for tr in triplets:
        for k in tr[1].keys():
            if "obj" in tr[1][k].keys():
                clear_triplets.append([tr[0], k, tr[1][k]['head'], tr[1][k]['obj']])
    return clear_triplets

def buildNet(triplets):
    n = net.Network()

if __name__ == '__main__':
    text = GetText('ezhikwtumane.txt_Ascii.txt')
    splittedText = SplitTextOnSentecnces(text)
    print(fdsfsf(splittedText))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
