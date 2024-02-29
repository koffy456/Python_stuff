import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #engine voice option. 0 for male/1 for female
rate = engine.getProperty('rate')   # getting current speaking rate (words per minute)
engine.setProperty('rate', rate - 50) 


def speak(audio): #speak function,allows os to speak text
    engine.say(audio)
    engine.runAndWait() 
    
def time(): #sets time to current time
    Time = datetime.datetime.now().strftime("%I:%M %p") 
    speak("The current time is")
    speak(Time) 

def date(): #sets date to current date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is") 
    speak(date)
    speak(month)
    speak(year)

def welcome():
    speak("You are very welcome")    
   

def greeting(): #a greeting function
    speak('Hello user.')  
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("It is a nice morning isn't it?") #morning
    elif hour >= 12 and hour < 18: 
        speak("It sure is one nice afternoon") #afternoon
    elif hour >= 18 and hour <24:
        speak("What a good evening it is.") #evening
    else:
        speak("Good night user")  
               
    speak('Jarvis at your service. How can i help you')
    
def takecommand():
    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print("listening..")  
        r.pause_threshold = 1
        audio = r.listen(source) 
    
    try:
        print("Recogninzing..")   
        query = r.recognize_google(audio, language = 'en-us') 
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please..")    
        
        return "None"
    return query    


if __name__ == "__main__":
    greeting()  
    while True:
        query = takecommand().lower()
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        
        elif 'thank you' in query:
            welcome() 
        
        elif 'how are you' in query:
            speak("I am an ai assistant that is doing just fine. What do you need")    
        
        elif 'go offline' in query:
            speak("Alright sure. Goodbye")
            quit()  
        
        elif 'set a reminder' in query:
            speak("What should i remember")  
            data = takecommand()
            speak("You said i should remind you that"+data)
            remember = open('data.txt','w')  
            remember.write(data) 
            remember.close()   
            
        elif 'do i have any reminders' in query:
            remember = open('data.txt','r')  
            speak("You asked me to remind you that"+remember.read())   
        
        elif 'joke' in query: 
           speak(pyjokes.get_joke()) #jokes function
           
         
        
        
               
           
       
          
                 
    

    

    