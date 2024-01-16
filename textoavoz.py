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
st.title("mensaje")
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
            
# import streamlit as st
# from bokeh.models.widgets import Button
# from bokeh.models import CustomJS
# from streamlit_bokeh_events import streamlit_bokeh_events

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
#         st.write(result.get("GET_TEXT"))