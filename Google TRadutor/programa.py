import idioma as d
import custom as cs
from tkinter import *
from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import ttk, messagebox

class GoogleTranslate:
    def __init__(self, root):
        self.window = root
        self.window.geometry("900x540")
        self.window.title('Google Tradutor - Evandro Moresco')
        self.window.resizable(width = False, height = False)
        self.window.configure(bg="white")

        self.frame = Frame(self.window,width=300, height=60)
        self.frame.pack()
        self.frame.place(x=20, y=20)

        self.DisplayLogo()


        aboutBtn = Button(self.window, text="Sobre", \
        font=(cs.font2, 8, 'bold'), bg=cs.color2, \
        fg="white", width=5, command=self.About)
        aboutBtn.place(x=800, y=20)

        exitBtn = Button(self.window, text="Sair", \
        font=(cs.font2, 8, 'bold'), bg=cs.color2, \
        fg="white", width=5, command=self.Exit)
        exitBtn.place(x=800, y=60)
        # ==============================

        self.MainWindow()

    # Function for displaying the logo image
    def DisplayLogo(self):
        # Opening the image
        image = Image.open('GoogleTranslate.png')
        # Resizing the image
        resized_image = image.resize((300, 60))

        self.img1 = ImageTk.PhotoImage(resized_image)
        # A Label Widget to display the Image
        label = Label(self.frame, bg=cs.color1, image=self.img1)
        label.pack()

    # The Main Window: Containing other widgets
    def MainWindow(self):
        # String Variable
        self.currLang = StringVar()
        self.currLang.set("Não reconhecido")
        # Label: For showing the name of detected language
        self.detectedLang = Label(self.window, \
        textvariable=self.currLang, font=(cs.font3, 20), \
        bg=cs.color1)
        self.detectedLang.place(x=160, y=130)

        # Combobox: To select the language to be translated
        text = StringVar()
        self.toLang = ttk.Combobox(self.window, textvariable=text, \
        font=(cs.font1, 15))
        self.toLang['values'] = d.lang_list
        self.toLang.current(0)
        self.toLang.place(x=550, y=130)

        self.fromText_Box = Text(self.window, bg=cs.color3, 
        font=(cs.font1, 15), height=9, width=34)
        self.fromText_Box.place(x=80, y=190)

        self.toText_Box = Text(self.window, bg=cs.color3, \
        relief=GROOVE, font=(cs.font1, 15), height=9, width=34)
        self.toText_Box.place(x=480, y=190)

        translateBtn = Button(self.window, text="Traduzir", \
        font=(cs.font2, 14, "bold"), bg=cs.color4, fg=cs.color1, \
        command=self.Translator)
        translateBtn.place(x=385, y=430)

    def Translator(self):
        try:
            fromText = self.fromText_Box.get("1.0", "end-1c")

            # instance of Translator class
            translator = Translator()

            dest_lang = self.toLang.get()

            if dest_lang == '':
                messagebox.showwarning("Escolhou nada!", \
                "Selecione um idioma")
            else:
                if fromText != '':
                    langType = translator.detect(fromText)

                    # Translating the text
                    result = translator.translate(fromText, dest=dest_lang)

                    self.currLang.set(d._languages[langType.lang.lower()])
                    
                    self.toText_Box.delete("1.0", END)

                    self.toText_Box.insert(INSERT, result.text)
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")
    
    # For About Button
    def About(self):
        messagebox.showinfo("Google Tradutor - Python", \
        "Desenvolvido por Evandro Moresco\nOggiSec\n18/05/22")
    # For Exit Button: All window will be closed
    def Exit(self):
        self.window.destroy()

if __name__ == "__main__":
    # Instance of Tk Class
    root = Tk()
    # Object of GoogleTranslator Class
    obj = GoogleTranslate(root)
    root.mainloop()