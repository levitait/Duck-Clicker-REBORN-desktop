import customtkinter

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")



labeltest = customtkinter.CTkLabel(app, text="Hello World... Find my voice!")

app.mainloop()
