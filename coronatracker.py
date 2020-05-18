import speech_recognition as sr
import requests
from bs4 import BeautifulSoup as bs
import pyttsx3

run=True

url=requests.get("https://www.worldometers.info/coronavirus/")
contents=url.content
soup=bs(contents,'html.parser')
body=soup.body.find_all("div",{"class":"container"})[1]
totalcase=body.find_all('div',{'class':"row"})[1].find('div',{'class':'col-md-8'}).find('div',{'class':"content-inner"}).find_all('div',{'id':'maincounter-wrap'})[0].div.span.string
totaldeath=body.find_all('div',{'class':"row"})[1].find('div',{'class':'col-md-8'}).find('div',{'class':"content-inner"}).find_all('div',{'id':'maincounter-wrap'})[1].div.span.string

table=body.find_all('div',{'class':"row"})[2].find('div',{'class':'col-md-8'}).find('div',{'class':"tab-content"}).find('div',{'class':"tab-pane active"}).find('div',{'class':"main_table_countries_div"}).table.tbody.find_all('tr',{"style":""})[1:]

sy=pyttsx3.init()
speech=sr.Recognizer()

while run:    
    sy.say("Which country do you need to know")
    sy.runAndWait()

    with sr.Microphone() as source:
        
        while True:
            try:
                print("listening")
                audio=speech.listen(source)
                text=speech.recognize_google(audio)
                print(text)
                break
            except:
                print("Sorry speak again")
                continue
    if text.lower()=="world":
        sy.say(f"total cases are {totalcase} and total deaths are {totaldeath}")
        sy.runAndWait()
    elif text.lower=='exit' :
        run=False
    else:
        country=text.lower()
        print(country)
        for cnt in table:
            
            try :
                if cnt.find_all('td')[1].a.string.lower()==country:
                    #print(cnt.td.a.string.lower())
                    
                    sy.say(f"Total Case in {country} is {cnt.find_all('td')[2].string} and total death is {cnt.find_all('td')[4].string} and active cases are {cnt.find_all('td')[5].string}")
                    sy.runAndWait()
                    break
            except :
                continue



