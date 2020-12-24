## 기능 1================================================

from tkinter import *
import requests
from tkinter import filedialog


window = Tk()
window.title('Translate')
lets_translate = Label(window, text='Let\'s translate')
lets_translate.place(x=135, y=1)
window.geometry('350x450')#창 사이즈

# 콤보 박스1 (번역 대상 언어)
from tkinter import ttk 
combolist1 = ttk.Combobox(window, width=20, state='readonly')
combolist1['values']= ("번역할 언어","English","Korean","Japanese","Chinese")
combolist1.current(0)
combolist1.place(x=100, y=55)

# muti_text1 : 번역할 언어 넣기
import tkinter.scrolledtext as Scrolledtext
#from tkinter import scrolledtext
multi_text1= Scrolledtext.ScrolledText(window, width=45, height=10, wrap=WORD)
multi_text1.place(x=10, y=80)


# 네이버 Papago NMT API id, 비번!
import os
import sys
import urllib.request
import json


client_id = "yourPapagoID"
client_secret = "yourPapagoPW"

#번역하기 --------------------------------------------- 
def Trans_():
		#한글 <-> 영어 번역 
        global translated_text
        encText = urllib.parse.quote(translated_text)
        if(combolist1.get()=="Korean" and combolist2.get()=="English"):
            data1 = "source=ko&target=en&text=" + encText

        #영어 <-> 한글 번역
        elif(combolist1.get()=="English" and combolist2.get()=="Korean"):        
            data1 = "source=en&target=ko&text=" + encText
			
		#한글 <-> 일본어 번역
        elif(combolist1.get()=="Korean" and combolist2.get()=="Japanese"):        
            data1 = "source=ko&target=ja&text=" + encText
		
		#일본어 <-> 한글 번역
        elif(combolist1.get()=="Japanese" and combolist2.get()=="Korean"):        
            data1 = "source=ja&target=ko&text=" + encText
		
		#한글 <-> 중국어 번역
        elif(combolist1.get()=="Korean" and combolist2.get()=="Chinese"):        
            data1 = "source=ko&target=zh-CN&text=" + encText
		
		#중국어 <-> 한글 번역
        elif(combolist1.get()=="Chinese" and combolist2.get()=="Korean"):        
            data1 = "source=zh-CN&target=ko&text=" + encText
				
        url1 = "https://openapi.naver.com/v1/papago/n2mt"
        request1 = urllib.request.Request(url1)
        request1.add_header("X-Naver-Client-Id",client_id)
        request1.add_header("X-Naver-Client-Secret",client_secret)
        response1 = urllib.request.urlopen(request1, data=data1.encode("utf-8"))
        rescode1 = response1.getcode()
        if(rescode1==200):
            response1_body = response1.read()
            result=json.loads(response1_body)  
            #type(result)  
            multi_text2.insert(INSERT,result['message']['result']['translatedText'])
            print("번역 후 : ", result['message']['result']['translatedText'])
        else:
            print("Error Code:" + rescode1)
			
#'번역하기' 버튼 동작 ----------------------------------------
def clicked():
        global translated_text
        #button1.configure(text="초기화")
        translated_text = multi_text1.get(1.0,END)
        print("번역 전 :", translated_text )
        
        #Sensing()
        multi_text2.delete(1.0,END)    
        Trans_()    
		
#'번역하기' 버튼
button1=Button(window, text='번역하기',command=clicked)
button1.place(x=110, y=220)

#초기화----------------------------------------------- 
def reset():
        multi_text1.delete(1.0,END)
        multi_text2.delete(1.0,END) 

#'초기화' 버튼
reset=Button(window, text='초기화',command=reset, bg='#c7dbf4')
reset.place(x=180, y=220)


# 콤보 박스2 (번역 언어)----------------------------------
combolist2 = ttk.Combobox(window, width=20, state='readonly')
combolist2['values']= ("번역된 언어","English","Korean","Japanese","Chinese")
combolist2.current(0)
combolist2.place(x=100, y=250)

# multi_text2 : 번역 결과 텍스트
multi_text2= Scrolledtext.ScrolledText(window, width=45, height=10)
multi_text2.place(x=10, y=275)



#=======================================================





## 기능 2================================================

#언어 자동 감지------------------------------------------
def SensingLan():
    global sensing
    if(sensing=="en"):
        return "English"
    elif(sensing=="ko"):
        return "Korean"
    elif(sensing=="ja"):
        return "Japanese"
    elif(sensing=="ch"):
        return "Chinese"
    
def Sensing():
        global sensing, translated_text
        encQuery = urllib.parse.quote(translated_text)
        data2 = "query=" + encQuery
        url2 = "https://openapi.naver.com/v1/papago/detectLangs" 
        request2 = urllib.request.Request(url2)
        request2.add_header("X-Naver-Client-Id",client_id)
        request2.add_header("X-Naver-Client-Secret",client_secret)
        response2 = urllib.request.urlopen(request2, data=data2.encode("utf-8"))
        rescode2 = response2.getcode()
        if(rescode2==200):
            response2_body = response2.read()
            result2=json.loads(response2_body)  
            #type(result2)  
            print("사용한 언어는:",result2['langCode'])
            sensing=result2['langCode']
        else:
            print("Error Code:" + rescode2)

				
#파일 추가하고 STT-------------------------------------
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        global speech_text
        speech_text=data
            
    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))
        

					
def STT():  
        
        global speech_text,sensing,file,translated_text

        multi_text1.delete(1.0,END)
        multi_text2.delete(1.0,END) 
        
        speech_to_text = SpeechToTextV1(
            iam_apikey="yourKey",
            url="URL"
        )
        
        myRecognizeCallback = MyRecognizeCallback()
        
        with open(join(dirname(__file__), file),
                      'rb') as audio_file:
                audio_source = AudioSource(audio_file)
                speech_to_text.recognize_using_websocket(
                    audio=audio_source,
                    content_type='audio/mp3',
                    recognize_callback=myRecognizeCallback,
                    max_alternatives=3,
                    word_alternatives_threshold=0.5,
                    model='en-US_BroadbandModel',
                    keywords=None)

         
        sentence=""
        for i in speech_text['results']:
            sentence=sentence+i['alternatives'][0]['transcript']
        print("번역 전 : ", sentence)
        multi_text1.insert(INSERT,sentence)
        translated_text=sentence
        Sensing()
        combolist1.set(SensingLan()) # sensing에 따른 언어

#클릭시 file dialog 
def clicked2():
        global file
        button.configure(text="번역중", bg="#f6c4c4")
        file = filedialog.askopenfilename()
        print(file)
        STT()
        button.configure(text="번역할 음성")
        combolist2.set("Korean") # 음성번역은 항상 한국어로
        Trans_()
		
#파일 업로드 버튼
button=Button(window, text='번역할 음성',command=clicked2) 
button.place(x=130, y=25)

window.mainloop()
#print(words1)