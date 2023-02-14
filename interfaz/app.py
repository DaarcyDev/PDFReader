from tkinter import * 
import root as root
import PyPDF2
from tkinter.filedialog import askopenfile
from gtts import gTTS
import os
import pyglet
from time import sleep



class actions:
    root.root
    root.root.minsize(500,700)
    root.root.resizable(0,0)
    root.root.title("PDF Reader")
    root.root.grid_columnconfigure(1, weight=1)
    root.root.grid_rowconfigure(0, weight=0)
    root.root.config(bg="#5BB99E")

    botonBrowseText= StringVar()
    textBox = Text(root.titleFrame)

    def home(self):
        title = Label(root.titleFrame,text="PDF Reader")
        title.config(bg="#5BB99E",fg="#000",height=3,font=("arial",20))
        title.grid(row=0,column=1)

        Instruction = Label(root.titleFrame,text="Select a PDF file on your computer to extract all its text")
        Instruction.config(bg="#5BB99E",fg="#000",height=3,font=("arial",15))
        Instruction.grid(row=1,column=1)

        actions.botonBrowse = Button(root.titleFrame,textvariable=actions.botonBrowseText,relief="groove",command=lambda:actions.openFiles())
        actions.botonBrowseText.set("Browse")
        actions.botonBrowse.config(width=10,bg="#408571",fg="#000",font=("arial",15),pady=3,padx=7)
        actions.botonBrowse.grid(row=2,column=1,padx=5,pady=10)
        
        actions.textBox.grid(row=3,column=1)

        actions.botonSpeech = Button(root.titleFrame,text="Speech",relief="groove",command=lambda:actions.speak())
        actions.botonSpeech.config(width=10,bg="#408571",fg="#000",font=("arial",15),pady=3,padx=7)
        actions.botonSpeech.grid(row=4,column=1,padx=5,pady=10)

        root.titleFrame.config(bg="#5BB99E",padx=20,pady=20)
        root.titleFrame.grid(row=0,column=0, columnspan=3)
        
        root.root.mainloop()


    def openFiles():
        actions.textBox.delete(1.0,END)
        actions.botonBrowseText.set("loading...")
        file = askopenfile(parent=root.root, mode='rb', title="Choose a file", filetypes=[("PDF file", "*.pdf")])
        if(file):
            
            readPDF=PyPDF2.PdfFileReader(file)
            page=readPDF.getPage(0)
            pageContent = page.extractText()


            actions.textBox.insert(1.0,pageContent)
            actions.textBox.tag_configure("center", justify="center")
            actions.textBox.tag_add("center", 1.0, "end")
    

            actions.botonBrowseText.set("Browse")

    def transformText():
        print ("hola")

    def speak():
        
        text=actions.textBox.get(1.0, END)

        tts = gTTS(text=text, lang='es-us',slow=True)
        filename = 'voice.mp3'
        tts.save(filename)
        music = pyglet.media.load(filename, streaming=False,)
        music.play()
        
        sleep(music.duration) #prevent from killing
        os.remove(filename) #remove temperory file
        

    




        


    


