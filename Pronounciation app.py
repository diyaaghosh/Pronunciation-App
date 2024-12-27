from tkinter import *
from win32com.client import Dispatch
def speak(str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
    
def click():
    st = display.get()
    if(st.strip):
      speak(st)    
root=Tk()
root.geometry("633x434")
root.configure(bg="#f0f8ff") 
root.minsize(200,200)
root.maxsize(900,600)
root.title("Pronunciation App")
TEXT=Label(text="Pronunciation App",font=("ariel",15),bg="#f0f8ff", fg="#333333")
TEXT.pack(pady=10)
root.grid_propagate(False)  # Disable grid resizing
display=Entry(root,font=("ariel",18),width=30, bd=5,relief=GROOVE)
display.pack(pady=10)
button=Button(root,font=("ariel",14),fg="white",bg="#1974D2",text="Pronounce",command=click,activebackground="#ADD8E6")
button.pack(pady=20)
footer = Label(root, text="Enter an English word or sentence to hear its pronunciation.", font=("Arial", 12), bg="#f0f8ff", fg="#555555")
footer.pack(side=BOTTOM, pady=10)
root.mainloop()  








