from tkinter import *
from tkinter import ttk
from math import *
import re

response = ""
equation = ""

#Interface 
app = Tk() #création de l'interface
app.geometry("650x500") #création de la taille
app.resizable(False, False)
app.title("Math Fonction App")

app.config(pady=150)

#widget liste déroulante 
li = ttk.Combobox(app, width=1)
li['values'] = ['<', '=', '>'] #elements
li.current(0) #permet d'avoir un par défaut

#widget input number
input_one = Entry(app, justify=CENTER, bd=5) #création du input
input_one.insert(1, "placer un nombre") #création du placeholder *humhum*

#widget input's label
labeltxt = StringVar() #permet à une string d'être une variable tkinter
label_one = Label(app, justify=CENTER, textvariable=labeltxt)
labeltxt.set(f"x² < Ø")

#answer text
answer = Label(app, fg='red', font=3)

#fonction x²>a
def f(a):
    if a < 0:
        response = "Ø"
    elif a == 0:
        response = "0"
    elif a > 0:
        response = f"\u007B -√{a} ; √{a} \u007D"
    
    print(f"x² > {a}")
    print(f"S = {response}")
    answer.config(text=f"S = {response}") #met à jour la string d'une valeur de "" 

#fonction x² = a 
def g(a):
    if a < 0:
        response = "Ø"
        
    elif a == 0:
        response = "0"
        
    elif a > 0:
        response = f"\u007B -√{a} ; √{a} \u007D"
    
    print(f"x² > {a}")
    print(f"S = {response}")
    answer.config(text=f"S = {response}")

#fonction x² > a
def h(a):
    if a < 0:
        response = "Ø"
        
    elif a == 0:
        response = "0"
        
    elif a > 0:
        response = f"] -∞ ; √{a}] U [√{a} ; +∞ [ "
    
    print(f"x² > {a}")
    print(f"S = {response}")
    answer.config(text=f"S = {response}")

#widget button
#la fonction utilise get() pour ensuite mettre à jour le label 
# et utilise les diverse fonctions pour ensuite mettre à jour la string de la réponse
def Exe(): 
    regex = re.findall('[-+]?\d+',input_one.get()) #permet d'inclure les nombres négatifs

    if li.get() == "<": #<= li["values"][0]
        print(li["values"][0])
        labeltxt.set(f"x² < {regex[0]}") #regex = '[number]' donc regex[0] = number car regex est une liste
        f(int(regex[0])) #transforme la string en number pour effectuer l'operation
        
    elif li.get() == "=":
        print(li["values"][1])
        labeltxt.set(f"x² = {regex[0]}")
        g(int(regex[0]))

    elif li.get() == ">":
        print(li["values"][2])
        labeltxt.set(f"x² > {regex[0]}")
        h(int(regex[0]))
        
buttonExe = Button(app, text="Executer", command=Exe)



#(affichage)
label_one.pack()    
input_one.pack()
li.pack()

buttonExe.pack()
answer.pack()


app.mainloop() #affichage de l'app
