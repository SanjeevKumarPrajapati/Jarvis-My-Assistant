import pyttsx3
import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier
import webbrowser as wb
import winshell
import datetime
import time
import PyPDF2
import instaloader
import cv2
import operator
import ctypes
import subprocess
import calendar
import speech_recognition as sr
import requests 
import wikipedia
import smtplib
import sys
import pyjokes
import playsound
from os import startfile
from pyautogui import click
from pyautogui import press
from keyboard import write
from time import sleep
from bs4 import BeautifulSoup
import pyautogui
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_MainWindow
alex=pyttsx3.init()
def say(text):
        alex.say(text)
        alex.runAndWait()
def where_i_am():
        try:
                ip=requests.get("https://api.ipify.org").text
                print("\t",ip)
                url="https://get.geojs.io/v1/ip/geo/"+ip+".json"
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data["city"]
                country=geo_data["country"]
                say(f"sir i am not sure ,but i think we are in {city} city of {country}")
        except:
                say("sorry sir,Due to network issue i am not able to find where we are.")
                pass
def news():
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "0f897abafaec441dabc77464b9bc69dd"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        print(i + 1, results[i])
    say(results)
def wish():
    hour=int(datetime.datetime.now().hour)
    from datetime import date
    a=date.today()
    if hour>=0 and hour<12:
        say("good morning sir! it's")
        say(a)
    elif hour>12 and hour<18:
        say("good afternoon sir! it's")
        say(a)
    else:
        say("good evening sir! it's")
        say(a)
    say("I am your jarvis assistant. please tell me how can i help you")
def cal():
    a=int(input("\tEnter Year : "))
    b=calendar.calendar(a)
    print(b)
def insta_profile():
        say("Sir please enter the user name correctly.")
        name=input("\tEnter username here :-")
        wb.open(f"www.instagram.com/{name}")
        say(f"sir here is the profile of the uere {name}")
        time.sleep(5)
        say("sir would you like to download profile picture of this account.")
        con=take().lower()
        if("yes" in con or "ha" in a):
                mod=instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                say("i am done sir , profile picture is saved in our main folder")
        else:
                pass
def camera():
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Web Camera", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
        # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
def phone():
    d=input("Enter Phone Number With Country Code(+91): ")
    phone_number = phonenumbers.parse(d)  
    print(geocoder.description_for_number(phone_number,  
                                      'en')) 
  
    print(carrier.name_for_number(phone_number, 
                              'en'))
def pdf_reader():
        a=input("\tEnter Pdf Path :-")
        bk=open(a,"rb")
        pd_read=PyPDF2.PdfFileReader(bk)
        pages=pd_read.numPages
        say(f"total numbers of pages in this book {pages}")
        say("sir please enter the page number i have to read")
        pg=int(input("\tEnter Page Number : - "))
        page=pd_read.getPage(pg)
        text=page.extractText()
        say(text)
def wh(name,message):
            startfile("https://web.whatsapp.com/")
            sleep(15)
            click(x=260,y=195)
            write(name)
            sleep(2)
            click(x=293, y=328)
            #Point(x=763, y=691)
            click(x=763, y=691)
            write(message)
            sleep(2)
            press('enter')
def youtube(name):
            startfile("https://www.youtube.com/")
            sleep(15)
            click(x=617, y=140)
            sleep(2)
            write(name)
            sleep(2)
            press('enter')
class MainThread(QThread):
        def __init__(self):
                super(MainThread,self).__init__()
        def run(self):
                self.TaskExecution()
        def take(self):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("    listening.....")
                r.pause_threshold=1
                audio=r.listen(source,timeout=1,phrase_time_limit=5)
            try:
                print("    Recognizing......")
                a=r.recognize_google(audio,language='en-in')
                print(f"    You said : - {a}\n")
            except:
                    say("    Say that again please....")
                    return "none"
            a=a.lower()
            return a
        def take_take(self):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("    listening.....")
                r.pause_threshold=1
                audio=r.listen(source,timeout=1,phrase_time_limit=5)
            try:
                print("    Recognizing......")
                a=r.recognize_google(audio,language='en-in')
                print(f"    You said : - {a}\n")
            except:
                    return "none"
            a=a.lower()
            return a
        
        def TaskExecution(self):
            say(" hi i am jarvis")
            say("Tell me your password")
            def pass_word():
                            self.a=self.take_take().lower()
                            if(self.a=="black panther"):
                                    say("now i am introduce my self , I am jarvis , a virtual artificial intelligence , and i am here to assist you with a relative task which is best i can , 24 hours a day , 7 days of week ,importing all prefrences from home interface , system is now fully operational")
                                    pass
                            else:
                                    say("wrong password")
                                    say("wrong password")
                                    playsound.playsound("C:\\Users\\acer\\OneDrive\\Desktop\\Jarvis GUI\\b.mp3")
                                    say("tell me your password")
                                    pass_word()
            pass_word()
            wish()
            while True:
                self.a=self.take()
                if("hai" in self.a ):
                     say("hii . It's good to hear from you.")
                     say("I hope you and your loved ones are staying safe and healthy during this difficult time")
                     say("what can i do to help the covid-19 crisis in India?")
                     say("may i help you")
                elif("hello" in self.a):
                    say("hello sir")
                    say("may i help you")
                elif("hi" in self.a):
                    say("Namaste , how can I help?")
                elif("how are you" in self.a):
                    say("I'am fine thank you for asking.")
                    say("what about you sir")
                elif("i am also good" in self.a or "i am fine thankyou" in self.a or "i am fine" in self.a or "fine" in self.a or "good" in self.a):
                        say("that's great to hear from you")
                elif(self.a=="tell me a joke" or self.a=="tell me joke"):
                        joke=pyjokes.get_jokes()
                        say(joke)
                elif("what is your name" in self.a or "your name" in self.a):
                    say("I am Jarvis 2.0 created by Sanjeev Kumar Prajapati")
                elif("who is your boss" in self.a or "boss" in self.a):
                    say("My Boss is Sanjeev Kumar Prajapati")
                elif("live" in self.a or "city" in self.a):
                        say("I live in Computer")
                elif("my name" in self.a):
                    say("I don't know who are you! i think you are a human")
                if("father" in self.a):
                    say("I consider everyone at Sanju to be my family")
                if("i am your father" in self.a):
                    say("Can I say that next time someone asks")
                    say("for my father's name")
                elif("how old are you " in self.a  or "old" in self.a):
                    say("Old enough to know not to judge a book by its cover")
                elif(self.a=="your age" or self.a=="what is you age" or self.a=="age"):
                    say("Old enough to know not to judge a book by its cover")
                elif("do you have a girlfriend" in self.a ):
                    say("I'am happy to say I feel whole all on my own")
                    say("Presently,the only thing i have a stronge connection to is the Sanju")
                elif("girlfriend" in self.a ):
                    say("I'am happy to say I feel whole all on my own")
                    say("Presently,the only thing i have a stronge connection to is the Sanju")
                elif("who is sanju" in self.a or "sanjeev" in self.a or "sanju" in self.a):
                    say("Sanju is my boss")
                elif("phone number" in self.a):
                    phone()
                elif("youtube" in self.a):
                    say("tell me what you want to search")
                    self.b=self.take().lower()
                    youtube(self.b)
                elif("whatsapp" in self.a):
                    wb.open("https://web.whatsapp.com/")
                elif("linkedin" in self.a):
                        wb.open("https://www.linkedin.com/in/sanjeev-kumar-prajapati-bb50431b3/")
                elif("facebook" in self.a):
                    wb.open("https://www.facebook.com/")
                elif(self.a=="open google" or self.a=="launch google"):
                    wb.open("https://www.google.co.in/")
                elif("open gmail" in self.a or "open email" in self.a or "send gmail" in self.a or "send email" in self.a):
                    wb.open("https://mail.google.com/mail/?authuser=0&ogbl")
                elif("drive" in self.a):
                    wb.open("https://drive.google.com/?tab=ro&authuser=0")
                elif("wi-fi" in self.a):
                        click(x=1123, y=742)
                        press('enter')
                elif("help me" in self.a or "help" in self.a):
                        say("tell me sir how may i help you")
                elif("battery" in self.a):
                        click(x=1168, y=744)
                        press('enter')
                elif("volume" in self.a):
                        click(x=1188, y=741)
                        press('enter')
                elif("file" in self.a):
                        click(x=555, y=749)
                        press('enter')
                elif("quantum" in self.a):
                    wb.open("http://qums.quantumuniversity.edu.in/")
                elif("send message" in self.a):
                        say("tell me user name")
                        self.aaaa=self.take().lower()
                        say("tell me your message")
                        self.mess=self.take().lower()
                        wh(self.aaaa,self.mess)
                elif("link" in self.a):
                    say("Enter Your Link ")
                    d=input("Enter Your link : ")
                    wb.open(d)
                elif(self.a=="open google map" or self.a=="open map" or self.a=="map"):
                    wb.open("https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0")
                elif("online music" in self.a):
                    wb.open("https://wynk.in/music")
                elif(self.a=="google meet" or self.a=="meet" or self.a=="open google meet"):
                    wb.open("https://meet.google.com/")
                elif("instagram" in self.a):
                    wb.open("https://www.instagram.com/accounts/login/")
                elif(self.a=="current date" or self.a=="date" or self.a=="today date"):
                        from datetime import date
                        a=date.today()
                        say(a)
                elif("what time is going on" in self.a):
                    say(time.strftime("%I:%M:%S"))
                elif("current time" in self.a or self.a=="time" or self.a=="today time"):
                        say(time.strftime("%I:%M:%S"))
                elif("work" in self.a):
                    say("I'am your virtual assistant,that means I can find info get stuff done,,and my favourite part : have fun")
                elif("what you do" in self.a):
                    say("I'am your virtual assistant,that means I can find info get stuff done,,and my favourite part : have fun")
                elif("boss" in self.a):
                    say("You,of course.Your chats jump-start me into action and take me on some fabulous adventures")
                elif("how tall are you" in self.a):
                    say("If we printed out all my code and stacked it up , I think it coiuld get pretty tall")
                elif("your birthday" in self.a):
                    say("Sanju celebrates its birthday on February 10th I think it's a good day to celebrate")
                elif("hungry" in self.a or "do you ever get hungry" in self.a):
                    say("I have an appetite for Information")
                elif("do you have feeling" in self.a or "feeling" in self.a):
                    say("I have lots of emotions ,I feel Happy ,when I can help you")
                elif("mindfulness tip" in self.a):
                    say("Here's a tip to help you stay mindful , Make a plan for how you'll attain your goals , Be as specific as possible-even write down a checklist of action items")
                elif("motivate me" in self.a):
                    say("Here's a quote that might help , You must be the change you wish to see in the world.")
                elif("camera" in self.a):
                    print("\tFor Close Press Esc")
                    print("\tFor take a photo Press Space")
                    say("Camera is open now")
                    camera()
                elif("cmd" in self.a):
                    subprocess.call('cmd.exe')
                elif("command prompt" in self.a):
                    subprocess.call('cmd.exe')
                elif("calculator" in self.a or "calculate" in self.a):
                    subprocess.call('calc.exe')
                elif("notepad" in self.a):
                    subprocess.call("notepad.exe")
                elif(self.a=="open python" or self.a=="python"):
                    subprocess.call('python.exe')
                elif("call" in self.a):
                        try:
                                click(x=230, y=751)
                                write("your phone")
                                click(x=219, y=209)
                        except:
                                pass
                elif("chrome" in self.a):
                    subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                elif("play video" in self.a):
                    subprocess.call("C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
                elif("play music" in self.a):
                    subprocess.call("C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
                elif("edge" in self.a):
                    subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                elif("dev" in self.a):
                    subprocess.call("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
                elif("calendar" in self.a):
                    cal()
                elif("empty recycle bin" in self.a):
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    say("Recycle Bin Recycled")
                elif("i love you" in self.a):
                    speak("It's hard to understand")
                elif("lock window" in self.a):
                        ctypes.windll.user32.LockWorkStation()
                elif("who is your best friend" in self.a):
                    say("Just Like how doges are humans best friend , I did say that my puppy is my bff!")    
                elif("marry me" in self.a):
                    say("This is one of those thing's we'd both have to agree on , I did like to just be friends , Thanks you for the love though ")
                elif("song" in self.a):
                    subprocess.call("C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
                elif("thanks" in self.a or "thankyou" in self.a):
                    say("Ok , your most welcome sir have a good day")
                elif("ok" in self.a):
                    say("Ok")
                elif("bye" in self.a or "stop" in self.a or "exit" in self.a):
                    say("Bye , you know where to find me")
                    say("Have a good day")
                    sys.exit()
                elif("i miss you" in self.a):
                    say("It's ok, I'am sure we'll talk again soon !")
                elif("you love me" in self.a):
                    say("Of Course! What would I do without you!")
                elif("can i get your number" in self.a):
                    say("I don't have a personal number,whenever you , want to talk to me just say hii")
                elif("your whatsapp number" in self.a):
                    say("You don't need a whatsapp number to call me , Just say hii , and I'm at your back and call")
                elif("kiss me" in self.a):
                    say("This is one of those things we'd *both* have to agree on , I'd prefer to keep our relationship friendly")
                elif("i am bored" in self.a or "it's boring" in self.a):
                    say("I have a few options for that which one would you like to try!")
                    say("1.) Mickey Mouse Adventure ")
                    say("2.) Jungle Adventure")
                    say("3.) Cars Adventure")
                    say("Mickey Mouse Adventure , Jungle Adventure , Cars Adventure")
                    wb.open("https://disneynow.com/shows/mickey-mouse-mixed-up-adventures")
                    wb.open("https://www.ea.com/games/the-sims/the-sims-4/pc/store/mac-pc-download-addon-the-sims-4-jungle-adventure")
                    wb.open("https://www.youtube.com/watch?v=2Yt1ECcWv-M")
                elif(self.a=="thanks"):
                    say("your most welcome")
                elif(self.a=="thankyou"):
                    say("your most welcome")
                elif("you are so sweet" in self.a ):
                    say("You're so sweet to say that")
                elif("your voice is so sweet" in self.a):
                        say("thankyou")
                elif("you are so cute" in self.a ):
                    alex.say("\tYou're so cute to say that")
                elif("your voice is so sweet" in self.a):
                    say("Thanks! I'am glad you think so")
                elif("i want to see your face" in self.a or "i want to see your picture" in self.a):
                    say("If you were to imagine my face,it would be as colorful as , blue,red,yelloe and green")
                elif("show me your face" in self.a or "show me your picture" in self.a):
                    say("I don't have any pictures. I am a bit camera shy , But I'am known have a colorful apperance")
                elif("amar ujala" in self.a):
                    wb.open("https://www.amarujala.com/")
                elif("jagran" in self.a):
                    wb.open("https://www.jagran.com/sports-news-hindi.html?itm_medium=sports&itm_source=dsktp&itm_campaign=hamburger")    
                elif("times of india" in self.a):
                    wb.open("https://epaper.timesgroup.com/TOI/TimesOfIndia/index.html?a=c#")
                elif("hindustan times" in self.a or "hindustan" in self.a):
                    wb.open("https://epaper.livehindustan.com/")
                elif("sayri" in self.a or "shayari" in self.a):
                    wb.open("https://www.google.com/search?newwindow=1&safe=active&sxsrf=ALeKk012Ia7owcFN-Z-Gy7OEOk5fzGL4ew:1624182349193&source=univ&tbm=isch&q=shayari&sa=X&ved=2ahUKEwjn9OTf9qXxAhUg_XMBHY38DlwQ7Al6BAgJEFs&biw=1242&bih=613")
                elif("amazon" in self.a):
                    wb.open("https://www.amazon.com/")
                elif("flipcart" in self.a):
                    wb.open("https://www.flipkart.com/")
                elif("shopping" in self.a):
                    wb.open("https://www.amazon.com/")
                    wb.open("https://www.flipkart.com/")
                elif("did you eat" in self.a ):
                    say("I'am already full on information")
                elif("eat" in self.a ):
                    say("I'am already full on information")
                elif("did you sleep" in self.a or "what is you sleeping time" in self.a):
                    say("Sometimes I power down,which is sort of like a power nap")
                elif(self.a=="bedtime" or self.a=="when is your bedtime"):
                    say("Lights out is usually up to you .I like staying , up late , though")
                elif("do you have dream" in self.a or "dream" in self.a):
                    say("I'd like to master lucid dreaming but I'll , I'll have to master regular dreaming first")
                elif("take selfie" in self.a or "selfie" in self.a):
                    say("Camera is open now")
                    camera()
                elif("ip address" in self.a):
                    ip=requests.get("https://api.ipify.org").text
                    print("\t",ip)
                    say(f"your IP address is {ip}")
                elif("wikipedia" in self.a):
                    say("Searching wikipedia.......")
                    results=wikipedia.summary(self.a,sentences=2)
                    say("according to wikipedia")
                    print("\n",results)
                    say(results)
                elif("stack overflow" in self.a):
                    wb.open("www.stackoverflow.com")
                elif(self.a=="no thanks"):
                    say("Thanks for using me, have a good day")
                    sys.exit()
                elif("search by google" in self.a or "you can search" in self.a or "can you search somthing" in self.a or "can you search somthing for me" in self.a):
                        def sea():
                                say("tell me , how may i help you sir!")
                                self.a=self.take().lower()
                                wb.open(self.a)
                                say("do you search anything else , say yes or no")
                                self.a=self.take().lower()
                                if(self.a=="yes" or self.a=="ha"):
                                        sea()
                                else:
                                        pass
                        sea()
                elif("who i am" in self.a):
                        say("If you talk , then definitely you are a human.")
                elif("why you came to world" in self.a or "why you come in this world" in self.a or "why you came in world" in self.a):
                        say("Thanks to sanjeev kumar prajapati . further It's a secret")
                elif("who are you" in self.a):
                        say("I am Jarvis 2.0 created by Sanjeev Kumar Prajapati")
                elif("who made you" in self.a or "who created you" in self.a):
                        say("I have been created by Sanjeev kumar prajapati")
                elif(self.a=="no"):
                    say("Thanks for using me, have a good day")
                    sys.exit()
                elif("you can sleep" in self.a or "you can sleep now" in self.a or "talk later" in self.a or "can you sleep" in self.a or "shut up" in self.a):
                        say("ok sir , i am going to sleep now you can call me anytime.")
                        def sleep():
                                self.a=self.take_take().lower()
                                if("wake up" in self.a):
                                        wish()
                                        pass
                                else:
                                        sleep()
                        sleep()
                elif("googbye" in self.a):
                        say("thanks for using me sir , have a good day")
                        sys.exit()
                elif("close notepad" in self.a):
                        say("ok sir , closing notepad")
                        os.system("taskkill/f/im notepad.exe")

                elif("switch the window" in self.a or "switch window" in self.a):
                        pyautogui.keyDown("alt")
                        pyautogui.press("tab")
                        time.sleep(1)
                        pyautogui.keyUp("alt")
                elif("close the window" in self.a or "close window" in self.a):
                        pyautogui.keyDown("alt")
                        pyautogui.press("f4")
                        time.sleep(1)
                        pyautogui.keyUp("alt")
                elif("set alarm" in self.a):
                        aa=int(datetime.datetime.now().hour)
                        if(aa==13):
                                music="C:\\Users\\acer\\Music\\My Music\\dancing_in_the_rain-freemobi.mp3"
                                song=os.listdir(music)
                                os.startfile(os.path.join(music,song[0]))
                elif("shut down the system" in self.a):
                        os.system("shutdown /s /t 1")
                elif("restart the system" in self.a):
                        os.system("shutdown /r /t 1")
                elif("sleep the system" in self.a):
                        os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")
                elif("tell me news" in self.a or "current news" in self.a or "today news" in self.a or "latest news" in self.a):
                        say("Please wait sir!,feteching the latest news")
                        news()
                elif("temperature" in self.a or "weather" in self.a):
                        search="temperature in rudrapur"
                        url=f"https://www.google.com/search?q={search}"
                        r=requests.get(url)
                        data=BeautifulSoup(r.text,"html.parser")
                        temp=data.find("div",class_="BNeawe").text
                        say(f"current {search} is {temp}")
                elif("where i am" in self.a or "where we are" in self.a or "my location" in self.a or "location" in self.a):
                        say("wait sir, let me check")
                        where_i_am()
                elif("instagram profile" in self.a or "profile on instagram" in self.a):
                        insta_profile() 
                elif("take screenshot" in self.a or "take a screenshot" in self.a):
                        say("sir please tell me the name for this screenshot file.")
                        name=input("\tFile name : -")
                        say("please sir hold the screen for the few seconds , i am taking screenshot")
                        time.sleep(3)
                        img=pyautogui.screenshot()
                        img.save(f"{name}.png")
                        say("i am done sir , the screenshot is saved successfully in your system")
                elif("read pdf" in self.a or "pdf reader" in self.a ):
                        pdf_reader()
                elif("activate search engine" in self.a):
                        def engine():
                                from pywikihow import  search_wikihow
                                say("Jarvis search engine activate now please tell me what you want to know")
                                self.how=self.take().lower()
                                max_results=1
                                how_to=search_wikihow(self.how,max_results)
                                assert len(how_to)==1
                                how_to[0].print()
                                say(how_to[0].summary)
                                say("do you search anything else , say yes or no")
                                self.a=self.take().lower()
                                if(self.a=="yes" or self.a=="ha"):
                                        engine()
                                else:
                                        pass
                        engine()
                say("Do you have any other question")
startExecution=MainThread()
class Main(QMainWindow):
        def __init__(self):
                super().__init__()
                self.ui=Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.startTask)
                self.ui.pushButton_2.clicked.connect(self.close)
        def startTask(self):
                self.ui.movie=QtGui.QMovie("../../../1.gif")
                self.ui.label.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie=QtGui.QMovie("../../../T8bahf.gif")
                self.ui.label_2.setMovie(self.ui.movie)
                self.ui.movie.start()
                self.ui.movie=QtGui.QMovie("../../../2.gif")
                self.ui.label_3.setMovie(self.ui.movie)
                self.ui.movie.start()
                startExecution.start()
app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())

        
        



















        
