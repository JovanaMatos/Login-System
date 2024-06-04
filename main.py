from mysql.connector import (connection)
import customtkinter
from PIL import Image
from tkinter import messagebox
import hashlib

class LoginWindow:
    def __init__(self):
        self.janela = customtkinter.CTk()

    def login_Janela(self):#Configurações Janela
        self.janela1 = self.janela
        self.janela1.title("Login")
        self.janela1.geometry("600x400")
        self.janela1.iconbitmap("D:\JOVANA\PI04\Python\src\Parte2\loginCustomer\icone.ico")
        self.janela1.resizable(False, False)
        customtkinter.set_appearance_mode("Light") # Other: "Light", "System" (only macOS)

        my_image = customtkinter.CTkImage(light_image=Image.open('D:\JOVANA\PI04\Python\src\Parte2\loginCustomer\logo.png'),#Config imagem
                                          dark_image=Image.open('D:\JOVANA\PI04\Python\src\Parte2\loginCustomer\logo.png'),
                                          size=(250, 250))

        my_label = customtkinter.CTkLabel(self.janela1, text='' ,image=my_image)
        my_label.place(x=25, y=65)

        self.framelogin = customtkinter.CTkFrame(master=self.janela1, width=320, height=396) #Criando uma frame para info
        self.framelogin.pack(side=customtkinter.RIGHT)

        label_titulo = customtkinter.CTkLabel(master=self.framelogin, text="Welcome",#titulo
                                              font=("Helvetica", 30, "italic", "bold"),
                                              text_color="#1E90FF")
        label_titulo.place(x=100, y=20)

        label_titulo2 = customtkinter.CTkLabel(master=self.framelogin,
                                                text="Please log in to access your account!",
                                                font=("Helvetica", 10, "italic"),
                                                text_color="#1E90FF")
        label_titulo2.place(x=90, y=50)

        self.email_entry = customtkinter.CTkEntry(master=self.framelogin, placeholder_text="Email Address", width=290,#Entries
                                                font=("Helvetica", 12))
        self.email_entry.place(x=20, y=105)

        self.password_entry = customtkinter.CTkEntry(master=self.framelogin, placeholder_text="Password", show="*",
                                                width=290, font=("Helvetica", 12))
        self.password_entry.place(x=20, y=175)

        checkbox_var = customtkinter.StringVar(value="off")#checkbox
        checkbox = customtkinter.CTkCheckBox(master=self.framelogin, text="Remember", variable=checkbox_var,
                                             onvalue="on", offvalue="off", font=("Helvetica", 8, "italic"),
                                             text_color="#1E90FF", checkbox_width=20, checkbox_height=20,
                                             border_color="#808080")
        checkbox.place(x=20, y=225)

        login_button = customtkinter.CTkButton(master=self.framelogin, text="Log In", width=290, command=lambda:self.login_verifica())
        login_button.place(x=20, y=285)#Button

        create_button = customtkinter.CTkButton(master=self.framelogin, text="Create Account",#Nova conta
                                              font=("Helvetica", 10, "italic"),
                                              command=self.CreateAccount)
        create_button.place(x=100, y=325)

        self.janela1.mainloop()

    def CreateAccount(self):#Janela para criar nova conta
        
        #remover o frame de login
        self.framelogin.pack_forget()

        self.frame1 = customtkinter.CTkFrame(master=self.janela1, width=320, height=396)
        self.frame1.pack(side=customtkinter.RIGHT)

        label_titulo3 = customtkinter.CTkLabel(master=self.frame1, text="Create Account",
                                              font=("Helvetica", 30, "italic", "bold"),
                                              text_color="#1E90FF")
        label_titulo3.place(x=45, y=20)

        label_titulo4 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Please fill in all required fields before proceeding.",
                                                font=("Helvetica", 10, "italic"),
                                                text_color="#1E90FF")
        label_titulo4.place(x=20, y=80)

        self.new_username_entry = customtkinter.CTkEntry(master=self.frame1, placeholder_text="Username", width=290,
                                                font=("Helvetica", 12))
        self.new_username_entry.place(x=20, y=105)

        self.new_email_entry = customtkinter.CTkEntry(master=self.frame1, placeholder_text="Email Address", width=290,
                                                font=("Helvetica", 12))
        self.new_email_entry.place(x=20, y=145)

        self.course_entry = customtkinter.CTkEntry(master=self.frame1, placeholder_text="Course", width=290,
                                                font=("Helvetica", 12))
        self.course_entry.place(x=20, y=185)

        self.new_password_entry = customtkinter.CTkEntry(master=self.frame1, placeholder_text="Password", show = "*",
                                                width=290, font=("Helvetica", 12))
        self.new_password_entry.place(x=20, y=225)

        checkbox1_var = customtkinter.StringVar(value="off")#checkbox
        checkbox1 = customtkinter.CTkCheckBox(master=self.frame1, text="I have read and agree to the Terms of Service",
                                             variable=checkbox1_var,
                                             onvalue="on", offvalue="off", font=("Helvetica", 10, "italic","bold"),
                                             text_color="#1E90FF", checkbox_width=20, checkbox_height=20,
                                             border_color="#808080")
        checkbox1.place(x=25, y=265)

     
            

        back_button = customtkinter.CTkButton(master=self.frame1, text="Back", width=135, command=self.backLogin )
        back_button.place(x=15, y=345)

        sign_Up_button = customtkinter.CTkButton(master=self.frame1, text="Sign up", width=135, command= self.insert_new_user_db)
        sign_Up_button.place(x=175, y=345)


        self.janela1.mainloop()

    def backLogin(self):
            self.clear_entry_login()
            self.frame1.pack_forget()#removendo o freme de cadastro
            self.framelogin.pack(side=customtkinter.RIGHT)#devolvendo o frame de login
    
    def db_connection(self):#conecta bd
        self.cnx = connection.MySQLConnection(user="root", password="", host="localhost", database="School_db")
        self.cursor= self.cnx.cursor()
        if self.cnx and self.cnx.is_connected():
            print("Banco de dados conectado!")
        else:
            print("Erro ao conectar ao banco de dados.")

    def db_close_connection(self):#desconecta bd
        self.cnx.close()
        print("Banco de dados desconectado!")




            
    def insert_new_user_db(self):#inseri novo usuario bd
        
        email = self.new_email_entry.get()
        pass_word = self.new_password_entry.get()
        username=self.new_username_entry.get()
        course= self.course_entry.get()
        
        if (not email.strip() or not pass_word.strip() or not username.strip() or not course.strip()):
                messagebox.showerror(title="Login", message="Please fill in all required fields before proceeding.")
                return
        
        elif ('@' not in email):
            messagebox.showerror(title="Login", message="Warning, Please enter a valid email address.")
            self.new_email_entry.delete(0, 'end')
            return
        
        elif (self.password_Verification() == False):
                self.new_password_entry.delete(0, 'end')
                return
    
                                                        
        
        self.read_db() #lendo banco de dados
        #email = email.islower()
        
        for lines in self.rows:
            if (email in lines):
                messagebox.showerror(title="Aviso", message="Usuário ja existe ")
                return
        pass_word_encriptada = hashlib.sha256(pass_word.encode()).hexdigest()
        self.db_connection()

        self.cursor.execute("INSERT INTO `users`(`Email`, `Pass_Word`) VALUES (%s , %s );", 
                                (email, pass_word_encriptada) )
        
        self.cnx.commit()#para confirmar as alterações
        
        #Pegando o userID da tabela users criado para passar para chave estrangeira na tabela final_grade
        self.cursor.execute("SELECT userID FROM `users` WHERE Email = %s and Pass_Word = %s;", (email, pass_word_encriptada))
        userID = self.cursor.fetchone()
        userID_str = "".join(map(str, userID))#passando a tupla para string
        

        self.cursor.execute("INSERT INTO `final_grade`(`UserID`,`Name`, `Course`) VALUES (%s, %s, %s );",
                                (userID_str,username, course))
        
        
        messagebox.showinfo(title="Aviso", message="Registrado com sucesso!")
                    
        self.cnx.commit()#para confirmar as alterações 
        self.db_close_connection()
        self.clear_new_entry()
        self.backLogin()

    def clear_new_entry(self):#limpar entry
          
          self.new_email_entry.delete(0, 'end')
          self.new_password_entry.delete(0, 'end')
          self.new_username_entry.delete(0, 'end')
          self.course_entry.delete(0, 'end')
          

    def clear_entry_login(self):

        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')


                
    def password_Verification(self):     #verifica senha e condições 
        msg ="" 
        errors = []
        letterCount = 0
        numberCount = 0
        spaceCount = 0
        valid = True
        
        for char in self.new_password_entry.get():
            if char.isalpha():
                letterCount += 1
            elif char.isdigit():
                numberCount += 1
            elif char.isspace():
                spaceCount += 1

        if len(self.new_password_entry.get()) < 8:
            errors.append("Password must have at least 8 characters!")

        if len(self.new_password_entry.get()) > 12:
            errors.append("Password must have at most 12 characters!")

        if not letterCount:
            errors.append("Password must contain letters!")

        if not numberCount:
            errors.append("Password must contain numbers!")
        
        if spaceCount > 0:
            errors.append("Password must not contain spaces!")

        # Conclusion
        if errors:
            valid = False
            for error in errors:
                msg += "- " + error + "\n"
            messagebox.showerror(title="Login", message= msg)
        
        return valid
    

    def read_db(self):#ler base de dados
        self.db_connection()
        self.cursor.execute("SELECT * FROM users")#Mostra tabela
        self.rows = self.cursor.fetchall() #busca todos os registro e cria uma tupla.
        
        print("Dados buscados com sucesso!")
        self.db_close_connection()
        return self.rows
        
        
        
    def login_verifica(self): #Verifica Senha e user Existe
        
        dados = self.read_db()
        self.email_Login= self.email_entry.get()
        self.senha_Login =self.password_entry.get()
        self.encrypted_password = hashlib.sha256(self.senha_Login.encode()).hexdigest()
        msn= "Welcome"
       
        for lines in dados:
            if (self.email_Login in lines and self.encrypted_password in lines):
                messagebox.showinfo(title="Aviso", message = msn)
                self.grade_db()
                return
                
        messagebox.showerror(title="Aviso", message="Senha ou usuário Invalido ")
        return
    
    def grade_db(self):
        self.db_connection()
        self.cursor.execute("""SELECT `Name`, `Course`, `Grade_1`, `Grade_2`, `Grade_3`, `Average_Grade`
                                FROM `final_grade`,`users`
                                WHERE `final_grade`.`UserID` = `users`.`UserID` AND Email = %s and Pass_Word = %s;""", (self.email_Login, self.encrypted_password))
        
        result= self.cursor.fetchall() #busca todos os registro e cria uma tupla.
        data1= []#passando para uma lista
        self.db_close_connection()
        for data in result:
            data1 += data
            

         #remover o frame de login
        self.framelogin.pack_forget()

        self.frame1 = customtkinter.CTkFrame(master=self.janela1, width=320, height=396)
        self.frame1.pack(side=customtkinter.RIGHT)

        label_titulo3 = customtkinter.CTkLabel(master=self.frame1, text="Your grades",
                                              font=("Helvetica", 30, "italic", "bold"),
                                              text_color="#1E90FF")
        label_titulo3.place(x=45, y=20)
        

        label_titulo4 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Hi "+ data1[0],
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo4.place(x=20, y=80)
        
        label_titulo5 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Course: "+ data1[1],
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo5.place(x=20, y=110)
        
        label_titulo6 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Grade 1: "+ str(data1[2]),
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo6.place(x=20, y=150)
        
        label_titulo7= customtkinter.CTkLabel(master=self.frame1,
                                                text="Grade 2: "+ str(data1[3]),
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo7.place(x=20, y=180)
        
        label_titulo8 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Grade 3: "+ str(data1[3]),
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo8.place(x=20, y=210)


        label_titulo9 = customtkinter.CTkLabel(master=self.frame1,
                                                text="Final Grade: "+ str(data1[4]),
                                                font=("Helvetica", 20, "italic"),
                                                text_color="#1E90FF")
        label_titulo9.place(x=20, y=240)
        
        
        
        back_button = customtkinter.CTkButton(master=self.frame1, text="Back", width=100, command=self.backLogin )
        back_button.place(x=190, y=350)
        
        
        self.janela1.mainloop()
        
 

login_window = LoginWindow()
login_window.login_Janela()


        
