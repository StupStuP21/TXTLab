# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PyPDF2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

def GetText(fileName):
    file = open(fileName,'r')
    text = file.read()
    return text

def GetTextFromPDF(fileName):
    reader = PyPDF2.PdfReader(fileName)
    numOfPages = len(reader.pages)
    text = []
    textText = ''
    for i in range (0,numOfPages):
        page = reader.pages[i]
        text.append(page.extractText())
    for i in range(0,len(text)):
        textText +=text[i]
    return textText


def TextEndSpechSignReplacer(text): # все меняется на точку
    text = text.replace('?','.')
    text = text.replace('!','.')
    return text

def StraightSpeachRemover(text):
    text = text.replace('. - ',' ')
    text = text.replace('. "','.')
    text = text.replace('...','.')
    text = text.replace('..','.')
    text = text.replace('." - ',' ')
    text = text.replace(' - ',' ')
    text = text.replace(' -\n',' ')
    text = text.replace('-\n','-')
    arrayOfReplacedSigns = ['\n','(',')','[',']','"',':',","]
    for i in range(0,len(arrayOfReplacedSigns)):
        text = text.replace(arrayOfReplacedSigns[i],'')
    return text

def StraightSpeachRemoverForPdf(text):
    arrOfSignsReplacedProbels = ['. - ','." - ',' - ',' -\n',' \n \n ',' \n \n \n ']
    arrOfSignReplasedDot = ['. "','...','..']
    arrOfSignReplacedNoth = ['\n','(',')','[',']','"',':',","]
    for i in text:
        if i in arrOfSignsReplacedProbels:
            i=' '
        elif i in arrOfSignReplasedDot:
            i='.'
        elif i in arrOfSignReplacedNoth:
            i=''
    return text


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
    text = TextEndSpechSignReplacer(text)
    text = StraightSpeachRemover(text)
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

def GetResultForPdf(fileName):
    print('PDF файл:')
    text = GetTextFromPDF(fileName)
    text = TextEndSpechSignReplacer(text)
    text = StraightSpeachRemover(text)
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

def GetDifference(list1,list2):
    words1 = []
    words2 = []
    for i in list1:
        for j in i:
            words1.append(j)
    for j in list2:
        for i in j:
            words2.append(i)
    words=[]
    if (len(words1)>len(words2)):
        for x in words1:
            if x not in words2:
                words.append(x)
    else:
        for x in words2:
            if x not in words1:
                words.append(x)
    return words

if __name__ == '__main__':
    print('Первый TXT:')
    GetResultForTxt('dostoinstwo.txt_Ascii.txt')
    print('Первый PDF:')
    GetResultForPdf('dostoinstwo.txt_Ascii.pdf')
    print('Второй TXT:')
    res1TXT = GetResultForTxt('ezhikwtumane.txt_Ascii.txt')
    print('Второй PDF:')
    res1PDF = GetResultForPdf('ezhikwtumane.txt_Ascii.pdf')
    diff = GetDifference(res1TXT, res1PDF)
    print(diff)
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
