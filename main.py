# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import os
import random
from tabulate import tabulate

ENGLISH = 0
JAPANESE = 1

KANA = 1
KANJI = 2


headings = ["ENGLISH", "KANA", "KANJI"]


ch4verbs = [
    ("wake up", "おきます", "起きます"),
    ("sleep", "ねます", "寝ます"),
    ("work", "はたらきます", "働きます"),
    ("rest", "やすみます", "休みます"),
    ("study", "べんきょうします", "勉強します"),
    ("finish", "おわります", "終わります"),
]

ch5verbs = [
    ("go", "いきます", "行きます"),
    ("come", "きます", "来ます"),
    ("return", "かえります", "帰ります")
]

ch6verbs = [
    ("eat", "たべます", "食べます"),
    ("drink", "のみます", "飲みます"),
    ("smoke", "すいます", "吸います"),
    ("see", "みます", "見ます"),
    ("hear", "ききます", "聞きます"),
    ("read", "よみます", "読みます"),
    ("write", "かきます", "書きます"),
    ("buy", "かいます", "買います"),
    ("take (a photo)", "とります", "撮ります"),
    ("do", "します", ""),
    ("meet", "あいます", "会います"),
]

ch7verbs = [
    ("cut", "きります", "切ります"),
    ("send", "おくります", "送ります"),
    ("give", "あげます", ""),
    ("receive", "もらいます", ""),
    ("lend", "かします", "貸します"),
    ("borrow", "かります", "借ります"),
    ("teach", "おしえます", "教えます"),
    ("learn", "ならいます", "習います"),
    ("make (phone call)", "かけます", ""),
]

ch0verbs = [
    ("verb", "", ""),
]

ch9verbs = [
    ("understand", "わかります", ""),
    ("have", "あります", ""),
]

ch10verbs = [
    ("exist (thing)", "あります", ""),
    ("exist (alive)", "います", ""),
]

def main():
    os.system('clear')
    print("Starting JPVocab!")
    print("Choose input language:")
    print("1) English")
    print("2) Japanese")
    outputLang = None

    while outputLang == None:
        choice = float(input("Enter a Number: "))
        if choice == 1:
            inputLang = ENGLISH
            print("Choose display:")
            print("1) Kana")
            print("2) Kanji")
            choice = float(input("Enter a Number: "))
            if choice == 1:
                outputLang = KANA
            elif choice == 2:
                outputLang = KANJI
        elif choice == 2:
            inputLang = JAPANESE
            outputLang = ENGLISH
        else:
            print("Invalid input, try again.")
    
    sortedList = sorted(ch4verbs + ch5verbs + ch6verbs + ch7verbs)
    #sortedList = sorted(ch7verbs)

    while True:
        randomword = random.randint(0, len(sortedList)-1)
        
        if sortedList[randomword][outputLang] == "":
            print(f"Random word is {sortedList[randomword][KANA]}")
        else:
            print(f"Random word is {sortedList[randomword][outputLang]}")
        answer = input(f"Your answer: ")

        if answer == sortedList[randomword][inputLang]:
            print(f"{answer} is correct!")
            sortedList.pop(randomword)
            if len(sortedList) == 0:
                break
            
        else:
            print(f"{answer} is wrong!")
            print(f"Correct answer is {sortedList[randomword][inputLang]}!")
        
        print(f"{len(sortedList)} words remaining!")
    
    print(f"All finished!  Exiting program...")

if __name__ == "__main__":
    main()