import pandas as pd
from gemini_getter import geminiGetter
import datetime
import time

math_tossups = pd.read_csv('<<QUESTION FILE NAME HERE>>.csv')
gemini = geminiGetter()

card_csv = open("<<NAME OF CSV YOU NEED TO WRITE TO>>.csv","w")

def script(num):

    #first, call qbreader api to get a new question
    str_q = math_tossups.iat[num,4] + " ANSWER: " + math_tossups.iat[num,5]

    #call gemini_api to ask the question
    response = gemini.make_card(formatted_question = str_q)

    #print the response into a csv (question, return)
    card_csv.write(response +"\n")

    print("Code executed")
if __name__ == "__main__":
    for i in range(len(math_tossups)):
        script(i)
        print(str(i) + "th code executed")
        time.sleep(5)
    card_csv.close()
