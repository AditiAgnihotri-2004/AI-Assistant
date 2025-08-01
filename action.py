import datetime
import text_to_speech
import webbrowser
import weather
import os




def Action(send):
    data_btn=send.lower()

    if "what is your name" in   data_btn :
      text_to_speech.text_to_speech("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        text_to_speech.text_to_speech("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            text_to_speech.text_to_speech("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           text_to_speech.text_to_speech("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           text_to_speech.text_to_speech("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          text_to_speech.text_to_speech(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            text_to_speech.text_to_speech("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        text_to_speech.text_to_speech("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans= weather.Weather()
       text_to_speech.text_to_speech(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.text_to_speech("songs playing...")
        return "songs playing..." 

    else :
        text_to_speech.text_to_speech( "i'm  not able to understand!")
        return "i'm not able to understand!"       
