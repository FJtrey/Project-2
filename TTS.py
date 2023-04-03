'''
Frederick Jeffrey Asiedu-Gyekye
10985048
BMEN
'''

import PySimpleGUI as sg
import pyttsx3

Engine_tts = pyttsx3.init()
VoiceTypes = Engine_tts.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='#000000', background_color='brown'),sg.Radio('Male', 'RADIO1', default=True, key='male', background_color='brown'),sg.Radio('Female', 'RADIO1', key='female', background_color='brown')],
     [sg.Text('Enter text to speak:',text_color='#000000', background_color='brown')],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='green')],
   
    
]

window = sg.Window('TEXT TO SPEECH APP', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            Engine_tts.setProperty('voice', VoiceTypes[1].id)
        elif values['female']:
           Engine_tts.setProperty('voice', VoiceTypes[0].id) 
    
        Engine_tts.say(text)
        Engine_tts.runAndWait()

window.close()