
import pyttsx3
import datetime


#import speech_recognition as sr


nome = input("Seja Bem-vindo! Digite seu nome:")


def voz(audio):

    altofalante = pyttsx3.init()

    voices = altofalante.getProperty('voices')
    altofalante.setProperty('voice', voices[0].id)
    altofalante.say(audio)   # define o texto que será lido
    altofalante.runAndWait()

def bem_vindo():
    voz("Olá lorde  " + nome + "   sou sua inteligencia artificial, como posso ajudalo?")

bem_vindo()

def resposta(resposta01):

    resposta01 = voz("estou otimo e com você?")

    pass

def data():
    ano = int(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    voz("a data atual é:")
    voz(dia)
    voz("do     " + mes + "  de")
    voz(ano)
pass

f = open('C:/Users/Camilo Verner/Downloads/Joji run.txt','r', encoding= "utf8")  #O local do arquivo que será lido
musica =f.read()

texto = 'S'

while texto == 'S':

    voz("digite algo")
    n = (input("digite algo:"))
    if n == 'ola':
        print("olá mestre " + nome)
        voz("olá mestre " + nome)


    if n == 'como você esta?':
        print("estou otimo e com você?")
        voz("estou otimo e com você?")

    if n == 'quem criou você?':
        print("Quem me criou foi o meu mestre Camilo Verner")
        voz("Quem me criou foi o meu mestre Camilo Verner")

    if n == 'quem é você?':
        print("Sou uma assistente virtual, criada para facilitar e ajudar voce")
        voz("Sou uma assistente virtual, criada para facilitar e ajudar voce")

    if n == 'cante uma música':
        print(musica)
        voz(musica)

    if n == 'cante uma música':
        print(musica)
        voz(musica)


    if n == 'que dia é hoje?':
        voz(data())



    texto = str(input("quer continuar? [S/N]")).upper()
voz("obrigado!")
print("fim")














'''def microfone():
    rec = sr.Recognizer()
    # print(sr.Microphone().list_microphone_names())

    with sr.Microphone() as mic:
        rec.pause_threshold = 1
        audio = rec.listen(mic)

    try:

        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)

    except Exception as e:
        print(e)
        voz("por favor repita!")

        return None

    return texto'''

