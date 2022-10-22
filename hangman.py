from operator import index
import random


wordsList = []                    #wordsList is used to store all words from the text file
generatedRandomWord: str = ""           #generatedRandomWord is used to store randomly selected word from the words list
wordLetterList = []                    #wordLettersList is used to store all letters of the randomly generated word
generatedWordsIndexList: list = []      #Stores all the index to be replaced in randomly generated word
generatedRandomNumber = 0               #to store generated random number
indexes=[]                              #indexes list is used to store all the indexes to be replaced with underscore
replacedWordLettersList = []            #ReplacedWordLettersList is used to store the letters after they are replaced with underscore
userInputLetters=[]                     #used to store correct input letters by the user.
lives = halflength = 0                  #used to store half length of the list to find how many letters to replace

def main():
    print("\nWelcome to Hangman Game, Developed with ❤️ by Saugat Timilsina(https://saugattimilsina.com.np)")
    chooseRandomWord()
    print("\n")

def setAllValues():
    global replacedWordLettersList, wordsList, generatedRandomWord, wordsList, wordLetterList, generatedWordsIndexList, generatedRandomNumber, indexes, userInputLetters, lives, halflength
    wordsList = []
    generatedRandomWord = ""
    wordLetterList = []
    generatedWordsIndexList = []
    generatedRandomNumber = 0
    indexes=[]
    replacedWordLettersList = []
    userInputLetters=[]
    lives = halflength = 0

def askToPlayAgain():
    global replacedWordLettersList
    userPlayAnswer = input("Do you want to play again? Press y to play again.\t")
    if (userPlayAnswer.lower() == 'y'):
        setAllValues()
        chooseRandomWord()
    else:
        print("\nGoodbye! Hope to see you again soon.")
        print("\nDeveloped with ❤️  by Saugat Timilsina.\n")
        exit(0)

def getRandomNumber():
    global generatedRandomNumber, generatedWordsIndexList
    generatedRandomNumber = random.randint(0,999)
    #Appending randomNumber to generatedWordsIndexList so as to not repeat it again further.
    if(not generatedRandomNumber in generatedWordsIndexList):
        # print("\nRandom Number:", generatedRandomNumber, "")
        generatedWordsIndexList.append(generatedRandomNumber)
    else:
        getRandomNumber()

def chooseRandomWord():
    global generatedRandomNumber, generatedRandomWord
    getRandomNumber()
    #getting words from txt file and storing in words array
    with open('1000words.txt', 'r') as file:
        for line in file:
            for word in line.split():
                wordsList.append(word)
    generatedRandomWord = wordsList[generatedRandomNumber]
    replaceCharactersWithUnderscore()
        
def replaceCharactersWithUnderscore():
    global wordLetterList, replacedWordLettersList, halflength
    halflength = int(len(generatedRandomWord)/2) # halfLength is used to store half of the word length of string parsed to integer so as to hide the same number while displaying letters to be shown
    # print("Length:", len(generatedRandomWord), "Halflength: ", halflength)
    wordLetterList = [x for x in generatedRandomWord] #Store list of letters in reverseWordLetterList and wordLetterList variable
    replacedWordLettersList.extend(wordLetterList) #storing the indexes which need to be replaced.
    for i in range(halflength):
        #if the index is empty which it will be the first time this loop launches, append 1
        if(not indexes):
            i+=1
            indexes.append(i)
            # print("Empty, Appended:", indexes)
        #else if the index isn't empty get the last item in the list and append value of 2 of the last index inside the list
        else:
            tempStorer = indexes[len(indexes)-1]
            indexes.append(tempStorer+2)
            # print("NotEmpty, Appended:", indexes)
    # print("Indexes to be replaced: ", indexes)
    for i in indexes:
        replacedWordLettersList[i] = "_"
    # print(replacedWordLettersList)
    print("Word Letters List:", wordLetterList, "Comment out this line at line 85 to hide full word.")
    playHangman()

def playHangman():
    global wordLetterList, replacedWordLettersList
    lives = int(len(generatedRandomWord)/2)
    print("\nYour Word: ", replacedWordLettersList)
    while not len(userInputLetters) == len(indexes):
        userVal = askUserValue()
        if(userVal == wordLetterList[indexes[len(userInputLetters)]]):
            userInputLetters.append(userVal)
        else:
            lives-=1
            if(lives == 0):
                print("\nYou died you stupid son of a buffalo.")
                break
            else:
                print("\nSorry! The letter you entered was incorrect. Your Remaining lives: ", lives)
    askToPlayAgain()

def askUserValue():
    tag=""
    if(len(userInputLetters)+1==1):
        tag = "st"
    elif(len(userInputLetters)+1==2):
        tag = "nd"
    elif(len(userInputLetters)+1==3):
        tag = "rd"
    else:
        tag="th"
    userValue = input(f"Please enter the {len(userInputLetters)+1}{tag} letter.\t")
    if(len(indexes) == len(userInputLetters)):
        print("Congratulations! You got the whole word correct.\n")
    return userValue

main()