import os
import speech_recognition as sr

def hear():                                #it takes microphone input form the user and 
                                           #reutrns string output
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("listening...")
        r.pause_threshold = 0.5    # seconds of non-speaking audio before a phrase is 
                                 # considered complete, jab bhi ham bolenge and agar 
                                 # hamane gap liya 1 sec ka tho ye complete na kr de
        r.energy_threshold = 300 #it takes the sound in croud area , 
                                        #increse it if their is croud .. then we have to speak louad if we increse
                                        #threshod frequency
        r.dynamic_energy_ratio = 2 #dont know what changes this

        audio = r.listen(sourse)
        try:
            query = r.recognize_google(audio)
            print("user said:", end = " ")
            print(query)
        except Exception as e:
            print("i didn't get that...")
            #speak(f"i didn't get that....")
            print("say that again please...")
            #speak(f"say that again please... ")
            return "none"
        return query

while True:

    wake_up=hear()

    if 'wake up' in wake_up:
        os.startfile('C:\\Users\\Vishu_96.k\\Documents\\J_A_R_V_I_S\\J_A_R_V_I_S_.py')#copy the location of the path of jaris file
   
    else:
        print("nothing....")