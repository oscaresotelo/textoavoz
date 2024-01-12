# import asyncio
# import streamlit as st
# import docx
# from io import BytesIO
# import re
# import json
# import time
# import base64
# from st_pages import Page, show_pages, add_page_title
# from gtts import gTTS
# import tempfile
# import os
# from sydney import SydneyClient
# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events
# from buscarvideo import buscar_videos_en_youtube
# import pyttsx3
# import wikipedia
# wikipedia.set_lang("es")
# speak = pyttsx3.init()
# voices = speak.getProperty('voices')  # to set all the voices
# voice_id = 'spanish-latin-am'
# #voice_id = 'mbrola-es1'
# speak.setProperty('voice', voice_id)

# def talk(text):
#     speak.say(text)
#     speak.runAndWait()

# def text_to_speech(text):
#     tts = gTTS(text=text, lang="es", tld='us')
#     temp_file = tempfile.NamedTemporaryFile(delete=False)
#     temp_file.close()
#     tts.save(temp_file.name)
#     return temp_file.name
# async def main(prompt) -> None:
#     async with SydneyClient() as sydney:
#         response = await sydney.compose(prompt)
#         return response

# stt_button = Button(label="Speak", width=100)

# stt_button.js_on_event("button_click", CustomJS(code="""
#     var recognition = new webkitSpeechRecognition();
#     recognition.continuous = true;
#     recognition.interimResults = true;
 
#     recognition.onresult = function (e) {
#         var value = "";
#         for (var i = e.resultIndex; i < e.results.length; ++i) {
#             if (e.results[i].isFinal) {
#                 value += e.results[i][0].transcript;
#             }
#         }
#         if ( value != "") {
#             document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
#         }
#     }
#     recognition.start();
#     """))

# result = streamlit_bokeh_events(
#     stt_button,
#     events="GET_TEXT",
#     key="listen",
#     refresh_on_update=False,
#     override_height=75,
#     debounce_time=0)

# if result:
#     if "GET_TEXT" in result:
#         prompt  = st.write(result.get("GET_TEXT"))
#         validar = result.get("GET_TEXT")
#         if "Buscar en YouTube" in validar:
#             buscar_videos_en_youtube(validar.replace("buscar en youtube", ""))
#         elif 'Dame información' in validar:
#                 person = validar.replace('Dame información', ' ')
#                 st.write("entro")
                
#                 info = wikipedia.summary(person, 3)
               
#                 talk(info)
#                 st.rerun()


            # buscar_videos_en_youtube(validar,10)

        # result = asyncio.run(main(prompt))
        # # st.write(result)

        # # Convertir texto a voz y reproducirlo
        # sample_rate = 44100
        # audio_file = text_to_speech(result)
        # st.audio(audio_file, format='audio/mp3')
        # elapsed_time = time.time() - start_time
        # os.remove(audio_file)
        # st.write(f"Tiempo transcurrido: {elapsed_time} segundos")

import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from buscarvideo import buscar_videos_en_youtube
import wikipedia
import pyttsx3
from threading import Thread

wikipedia.set_lang("es")
speak = pyttsx3.init()
voices = speak.getProperty('voices')
voice_id = 'spanish-latin-am'
speak.setProperty('voice', voice_id)



# def talk(text):
#     speak.say(text)
#     speak.runAndWait()
    
    
def main(prompt) -> None:
    # Your existing SydneyClient logic here
    pass

stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        prompt = result.get("GET_TEXT")
        st.write(prompt)

        if "Buscar en YouTube" in prompt:
            buscar_videos_en_youtube(prompt.replace("buscar en youtube", ""))
        elif 'Dame información' in prompt:
            person = prompt.replace('Dame información', ' ')
            

            info = wikipedia.summary(person, 3)
            speak.say(info)
            speak.runAndWait()
            
