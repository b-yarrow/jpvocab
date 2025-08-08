# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from tabulate import tabulate


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
    ("take a photo", "とります", "撮ります"),
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
    ("make phone call", "かけます", ""),
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
    print("Starting JPVocab!")

    print(tabulate(ch4verbs + ch5verbs + ch6verbs + ch7verbs, headers=headings))
    #print(tabulate(ch4verbs, headers=headings))
    #print(tabulate(ch5verbs, headers=headings))
    #print(tabulate(ch6verbs, headers=headings))
    #print(tabulate(ch7verbs, headers=headings))

    #row_format ="{:>15}" * (len(headings) + 1)
    #for t in ch4verbs[0]: row_format+="{:<"+str(len(t)+5)+"}"
    #print(row_format.format("", *headings))
    #for verb, row in zip(headings, ch4verbs):
    #    print(row_format.format(verb, *row))
    
    

    #print("ENGLISH\t\tHIRAGANA\t\tKANJI")
    #print("---------------------------------------")
    #for verb in Ch4verbs:
    #    print (f"{verb[0]}\t\t{verb[1]}\t\t{verb[2]}")
    #print(Ch5verbs[1][1])


if __name__ == "__main__":
    main()