from kivy.app import App
from kivy.core.window import Window
from tkinter import messagebox
from kivy.config import Config
import sqlite3
from kivy.uix.popup import Popup
import string
from kivy.uix.screenmanager import Screen,ScreenManager
from cryptography.fernet import Fernet
from kivy.clock import Clock
import rsa
import random
import time
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Window.clearcolor =("#edf7f3")
user = [""]
Value = [False,False,False,False]
Value1 = [False]
class PassSaverApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(PassSaverFirst(name='first'))
        self.sm.add_widget(PassSaverSecond(name='second'))
        return self.sm
class InfReader(Popup):
    def Read(self):
        Name_Element = self.ids.PassName.text
        Main_Pass = self.ids.Main.text
        self.sm = App.get_running_app().root
        User1 = self.sm.current_screen.ids.user.text
        conn = sqlite3.connect("SystemVault.sqlite",timeout=5)
        cur = conn.cursor()
        Book = [Name_Element]
        cur.execute(f'SELECT * FROM {User1} WHERE Name=?',(Book))
        row  = cur.fetchall()
        self.ids.OutWeb.text = ""
        self.ids.OutAge.text = ""
        self.ids.OutPhone.text = ""
        if row == []:
            messagebox.showerror("Error",f"Account '{Name_Element}' not found")
        else:
            if User1 == "Guest":
                        with open("System.key","rb") as Starter:#Open The Key file
                            Key_Offcial = b'Qlqeg6eT2E3QAIUwk3RjcvnWf0uJvCJaNN9nFqeqZc8='
                            F_Obg = Fernet(Key_Offcial)
                            Reader = Starter.read()
                            #Here we are Decrypting the First Key
                            Decrypter = F_Obg.decrypt(Reader)
                            Key_Second = Fernet(Decrypter)
                            with open("SystemCore.key","rb") as Seconder:#Open The second key file
                                Reader1 = Seconder.read()
                                #Here We are Decrypting the Second Key
                                cur.execute(f"SELECT * FROM {User1} WHERE Name=?",([Name_Element]))
                                row2 = cur.fetchall()
                                Extract4 = list(row2[0])
                                Decrypter1 =  Key_Second.decrypt(Reader1)
                                Loader = rsa.PrivateKey.load_pkcs1(Decrypter1)
                                try:
                                    self.ids.OutWeb.text = ""
                                    self.ids.OutAge.text = ""
                                    self.ids.OutPhone.text = ""
                                    Decrypter2 = rsa.decrypt(Extract4[1], Loader)
                                    Decrypter3 = rsa.decrypt(Extract4[2], Loader)
                                    Decrypter4 = rsa.decrypt(Extract4[3], Loader)
                                    Decrypter5 = rsa.decrypt(Extract4[4], Loader)
                                    Decrypter6 = rsa.decrypt(Extract4[5], Loader)
                                    self.ids.OutEmail.text = Decrypter2
                                    self.ids.Outpassword.text = Decrypter3
                                    self.ids.OutWeb.text = Decrypter4
                                    self.ids.OutAge.text = Decrypter5
                                    self.ids.OutPhone.text = Decrypter6
                                except:
                                    Decrypter2 = rsa.decrypt(Extract4[1], Loader)
                                    Decrypter3 = rsa.decrypt(Extract4[2], Loader)
                                    self.ids.OutEmail.text = Decrypter2
                                    self.ids.Outpassword.text = Decrypter3
                                    self.ids.OutWeb.text = ""
                                    self.ids.OutAge.text = ""
                                    self.ids.OutPhone.text = ""
            else:
                cur.execute(f"SELECT Password FROM users WHERE Name=?", ([User1]))
                row1 = cur.fetchall()
                Extract = row1[0]
                Extract1 = list(Extract)
                Extract2 = Extract1[0]


                with open("SystemSecure.key", "rb") as Getter_Pass:
                    RD = Getter_Pass.read()
                    key = b'5RMqCg5MW1wZNmspYgQU7pXs7AyDYrTUPIdmw02SOUc='
                    Obb = Fernet(key)
                    Dec = Obb.decrypt(RD)
                    key1 = Fernet(Dec)
                    Dec1 = key1.decrypt(Extract2)
                    Deco = Dec1.decode()
                    if Main_Pass == Deco:
                        with open("System.key","rb") as Starter:#Open The Key file
                            Key_Offcial = b'Qlqeg6eT2E3QAIUwk3RjcvnWf0uJvCJaNN9nFqeqZc8='
                            F_Obg = Fernet(Key_Offcial)
                            Reader = Starter.read()
                            #Here we are Decrypting the First Key
                            Decrypter = F_Obg.decrypt(Reader)
                            Key_Second = Fernet(Decrypter)
                            with open("SystemCore.key","rb") as Seconder:#Open The second key file
                                Reader1 = Seconder.read()
                                #Here We are Decrypting the Second Key
                                cur.execute(f"SELECT * FROM {User1} WHERE Name=?",([Name_Element]))
                                row2 = cur.fetchall()
                                Extract4 = list(row2[0])
                                Decrypter1 =  Key_Second.decrypt(Reader1)
                                Loader = rsa.PrivateKey.load_pkcs1(Decrypter1)
                                try:
                                    Decrypter2 = rsa.decrypt(Extract4[1], Loader)
                                    Decrypter3 = rsa.decrypt(Extract4[2], Loader)
                                    Decrypter4 = rsa.decrypt(Extract4[3], Loader)
                                    Decrypter5 = rsa.decrypt(Extract4[4], Loader)
                                    Decrypter6 = rsa.decrypt(Extract4[5], Loader)
                                    self.ids.OutEmail.text = Decrypter2
                                    self.ids.Outpassword.text = Decrypter3
                                    self.ids.OutWeb.text = Decrypter4
                                    self.ids.OutAge.text = Decrypter5
                                    self.ids.OutPhone.text = Decrypter6
                                except:
                                    Decrypter2 = rsa.decrypt(Extract4[1], Loader)
                                    Decrypter3 = rsa.decrypt(Extract4[2], Loader)
                                    self.ids.OutEmail.text = Decrypter2
                                    self.ids.Outpassword.text = Decrypter3
                    else:
                        messagebox.showerror("Error",f"Wrong Password")
    def AllInf(self,instance,value):

        if value == True:
            Value1[0] = True


class PassSaverFirst(Screen):

    def Guest(self):
        asker = messagebox.askyesno("PassSaver Account Manager",
                                    "Do You Want Really Sign in as Guest\nNote:Anyone can manage Passwords")
        if asker == 1:

            try:
                user = [""]
                db = sqlite3.connect("SystemVault.sqlite", timeout=5)
                cur = db.cursor()
                cur.execute(
                    f"CREATE TABLE IF NOT EXISTS Guest(Name VARCHAR(255) PRIMARY KEY, Email VARCHAR(255), Password VARCHAR(255), Web VARCHAR(255), Age VARCHAR(255), Phone VARCHAR(255))")
                db.close()

                with open("Co_Login.psvr","r+") as Reader:
                    Reader1 = Reader.read()
                    Ext = int(Reader1)

                    if Ext == 0:
                        with open("Co_Login.psvr", "w+") as Writer:
                            Writer.write('2')
                            Writer.close()
                    else:
                        self.sm = App.get_running_app().root
                        self.sm.current = 'second'
                        self.sm.current_screen.ids.start.text = "Welcome Back!"
                    Reader.close()

                user[0] += "Guest"

                self.sm = App.get_running_app().root
                self.sm.current = 'second'
                self.sm.current_screen.ids.user.text = user[0]
            except:


                with open("Co_Login.psvr", "w+") as Writer:
                    Writer.write('0')
                    Writer.close()
                messagebox.showinfo("PassSaver -Entry Gate Manager",
                                    "Welcome To Saad Studio PassSaver\nFor Help Click 'Help Button'\nThank You!")
                self.sm = App.get_running_app().root
                self.sm.current = 'second'

class SavePopup(Popup):
    def Save(self):
        Name = self.ids.SaveName.text
        Email = self.ids.SaveEmail.text
        Password = self.ids.Savepassword.text
        Web = self.ids.SaveWeb.text
        Age = self.ids.SaveAge.text
        Phone = self.ids.SavePhone.text
        if Name == "" or Email == "" or Password == "" or Web == "" or Age == "" or Phone == "":
            messagebox.showerror("PassSaver -Saver Information Manager", "Please Fill All Fields")
        else:
            try:
                with open("SystemConfiguration.pem","rb") as EncReader:
                    Encode2 = Email.encode()
                    Encode3 = Password.encode()
                    Encode4 = Web.encode()
                    Encode5 = Age.encode()
                    Encode6 = Phone.encode()
                    Geterr = EncReader.read()
                    Encrypter = rsa.PublicKey.load_pkcs1(Geterr)
                    Encrypter2 = rsa.encrypt(Encode2,Encrypter)
                    Encrypter3 = rsa.encrypt(Encode3, Encrypter)
                    Encrypter4 = rsa.encrypt(Encode4, Encrypter)
                    Encrypter5 = rsa.encrypt(Encode5, Encrypter)
                    Encrypter6 = rsa.encrypt(Encode6, Encrypter)
                    try:
                        self.sm = App.get_running_app().root
                        user1 = self.sm.current_screen.ids.user.text
                        book = [Name, Encrypter2, Encrypter3, Encrypter4, Encrypter5, Encrypter6]
                        conn = sqlite3.connect("SystemVault.sqlite", timeout=10)
                        cur = conn.cursor()
                        cur.execute(f"INSERT INTO {user1}(Name,Email,Password,Web,Age,Phone) VALUES(?,?,?,?,?,?)", book)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("PassSaver -Saver Information Manager","Account Saved Successfully")
                        self.dismiss()
                    except:
                        messagebox.showerror("PassSaver -Structure Manager", "System File Error\nTry Restart App")


            except FileNotFoundError:
                messagebox.showinfo("PassSaver -Encrypter Manager",
                                    "PassSaver Encrypting And Reading Your Information For More Security\nThis Opration Will Take 10seconds\nPlease Wait...")
                with open("System.key", "wb") as Writer:
                    Key = Fernet.generate_key()
                    Key1 = b'Qlqeg6eT2E3QAIUwk3RjcvnWf0uJvCJaNN9nFqeqZc8='
                    Key_Enc = Fernet(Key1)
                    Writer.write(Key_Enc.encrypt(Key))
                    Writer.close()
                    with open("SystemConfiguration.pem", "wb") as WriterRSA:
                        (pubKey, privKey) = rsa.newkeys(2048)
                        WriterRSA.write(pubKey._save_pkcs1_pem())
                        WriterRSA.close()
                        with open("System.key", "rb") as ReaderRSA:
                            Getter = ReaderRSA.readlines(90)
                            Decr = Key_Enc.decrypt(Getter[0])
                            Key_ENC_DCR = Fernet(Decr)
                            Encrypter = Key_ENC_DCR.encrypt(privKey._save_pkcs1_pem())
                            with open("SystemCore.key", "wb") as WriterCore:
                                WriterCore.write(Encrypter)
                                self.Save()
                                WriterCore.close()
class LoginPopup(Popup):
    def Login(self):
     user = [""]
     Verifier = self.ids.Email.text
     Verifier1 = self.ids.password.text
     Users = [Verifier]
     try:
      conn = sqlite3.connect("SystemVault.sqlite", timeout=5)
      cur = conn.cursor()
      cur.execute(f'SELECT Password FROM users WHERE Email=?', Users)
      row = cur.fetchall()
      Value = bool(row)
      if Value == False:
         messagebox.showerror("PassSaver Account Manager", "Email Not Founded")
      else:
         Extractor = row[0]
         Extractor1 = list(Extractor)
         with open("SystemSecure.key", "rb") as Decr:
             Reader = Decr.readlines(90)
             OffKey0 = b'5RMqCg5MW1wZNmspYgQU7pXs7AyDYrTUPIdmw02SOUc='
             Key_Decr = Fernet(OffKey0)
             Decrypter = Key_Decr.decrypt(Reader[0])
             Key_Decr_Pass = Fernet(Decrypter)
             Decrypter_1 = Key_Decr_Pass.decrypt(Extractor1[0])
             Decoder = Decrypter_1.decode()
             if Verifier1 == Decoder:
                 cur.execute(f'SELECT Name FROM users WHERE Email=?', Users)
                 row = cur.fetchall()
                 ex = row[0]
                 tp = list(ex)
                 user[0] += tp[0]
                 with open("Co_Login.psvr", "r+") as Reader:
                     Reader1 = Reader.read()
                     Ext = int(Reader1)
                     if Ext == 0:
                         with open("Co_Login.psvr", "w+") as Writer:
                             Writer.write('2')
                             Writer.close()
                     else:

                         self.sm = App.get_running_app().root
                         self.sm.current = 'second'
                         self.sm.current_screen.ids.user.text = user[0]
                         self.sm.current_screen.ids.start.text = "Welcome Back!"
                         self.dismiss()
                     Reader.close()
             else:
                 messagebox.showerror("PassSaver Account Manager", "Incorrect Password")
                 self.ids.password.text = ""
     except:
      messagebox.showerror("PassSaver Account Manager", "Email Not Founded")
class CrrPopup(Popup):
    def Crr(self):
        self.sm = ScreenManager()
        Verifier = self.ids.name.text
        Verifier1 = self.ids.Email.text
        Verifier2 = self.ids.password.text
        Verifier3 = self.ids.cfpassword.text
        Score  = [0,0,0]
        if Verifier == "" or Verifier1 == "" or Verifier2 == "" or Verifier3 == "":
            messagebox.showerror("Error", "Please Fill All Fields")
        if Verifier != "":
            Score[0] += 1
        else:messagebox.showerror("Name Error", "Invalid Name")
        if Verifier1 != "" and "@" in Verifier1:
            Score[1] += 1
        else:messagebox.showerror("Email Error", "Invalid Email")
        if Verifier3 == Verifier2:
            Score[2] += 1
        else:messagebox.showerror("Error", "Passwords Not Matching")
        upper_case = any([1 if c in string.ascii_uppercase else 0 for c in Verifier2])
        lower_case = any ([1 if a in string.ascii_lowercase else 0 for a in Verifier2])
        Puncutation = any([1 if a in string.punctuation else 0 for a in Verifier2])
        digit = any([1 if a in string.digits else 0 for a in Verifier2])
        if upper_case and lower_case and Puncutation and digit and len(Verifier2) > 8 and Score == [1,1,1] :
          try:
            with open('SystemSecure.key',"rb") as Encrypter:
                Reader = Encrypter.readlines(90)

                Off1Key =  b'5RMqCg5MW1wZNmspYgQU7pXs7AyDYrTUPIdmw02SOUc='
                G_obg = Fernet(Off1Key)
                decrypter = G_obg.decrypt(Reader[0])
                Encrypter_Pass = Fernet(decrypter)
                Encoder = Verifier2.encode()
                Encrypter1 = Encrypter_Pass.encrypt(Encoder)
                Encrypter.close()

                db = sqlite3.connect("SystemVault.sqlite", timeout=5)
                cur = db.cursor()

                book = [Verifier, Verifier1, Encrypter1]

                cur.execute("CREATE TABLE IF NOT EXISTS users(Name VARCHAR(255) PRIMARY KEY, Email VARCHAR(255), Password VARCHAR(255))")
                cur.execute("INSERT INTO users(Name,Email,Password) VALUES(?,?,?)", book)
                cur.execute(f"CREATE TABLE IF NOT EXISTS {Verifier}(Name VARCHAR(255) PRIMARY KEY, Email VARCHAR(255), Password VARCHAR(255), Web VARCHAR(255), Age VARCHAR(255), Phone VARCHAR(255))")
                db.commit()
                db.close()
                messagebox.showinfo("PassSaver -Entry Gate Manager","Welcome To Saad Studios PassSaver\nFor Help Click 'Help Button'\nThank You!")
                self.dismiss()
                user[0] += Verifier







          except:
              with open("SystemSecure.key", "wb") as Key:
                  OffKey = b'5RMqCg5MW1wZNmspYgQU7pXs7AyDYrTUPIdmw02SOUc='
                  key1 = Fernet.generate_key()
                  key = key1
                  F_obg = Fernet(OffKey)
                  encrypter = F_obg.encrypt(key)
                  Key.write(encrypter)
                  Key.close()
                  self.Crr()

        else:
            messagebox.showerror("Error","Password is very weak ")
            self.ids.password.text = ""
class PasswordGenSave(Popup):
    def SaveTHREE(self):
        Name1 = self.ids.SaveName.text
        Email1 = self.ids.SaveEmail.text
        Password1 = self.ids.GenTWOSavepassword.text
        Web1 = self.ids.SaveWeb.text
        Age1 = self.ids.SaveAge.text
        Phone1 = self.ids.SavePhone.text
        try:
            with open("SystemConfiguration.pem", "rb") as EncReader:

                Encode2 = Email1.encode()
                Encode3 = Password1.encode()
                Encode4 = Web1.encode()
                Encode5 = Age1.encode()
                Encode6 = Phone1.encode()
                Geterr = EncReader.read()
                Encrypter = rsa.PublicKey.load_pkcs1(Geterr)

                Encrypter2 = rsa.encrypt(Encode2, Encrypter)
                Encrypter3 = rsa.encrypt(Encode3, Encrypter)
                Encrypter4 = rsa.encrypt(Encode4, Encrypter)
                Encrypter5 = rsa.encrypt(Encode5, Encrypter)
                Encrypter6 = rsa.encrypt(Encode6, Encrypter)
                # try:
                self.sm = App.get_running_app().root
                user = self.sm.current_screen.ids.user.text
                book1 = [Name1, Encrypter2, Encrypter3,Encrypter4,Encrypter5,Encrypter6]
                conn = sqlite3.connect("SystemVault.sqlite", timeout=10)
                cur = conn.cursor()
                cur.execute(f"INSERT INTO {user}(Name,Email,Password,Web,Age,Phone) VALUES(?,?,?,?,?,?)",
                            book1)
                conn.commit()
                conn.close()
                messagebox.showinfo("PassSaver -Saver Information Manager", "Account Saved Successfully")

                # except:
                #     messagebox.showerror("PassSaver -Structure Manager", "System File Error\nTry Restart App")


        except FileNotFoundError:
            messagebox.showinfo("PassSaver -Encrypter Manager",
                                "PassSaver Encrypting And Reading Information For More Security\nthis Opration Will Take 10seconds\nPlease Wait...")
            with open("System.key", "wb") as Writer:
                Key = Fernet.generate_key()
                Key1 = b'Qlqeg6eT2E3QAIUwk3RjcvnWf0uJvCJaNN9nFqeqZc8='
                Key_Enc = Fernet(Key1)
                Writer.write(Key_Enc.encrypt(Key))
                Writer.close()
                with open("SystemConfiguration.pem", "wb") as WriterRSA:
                    (pubKey, privKey) = rsa.newkeys(2048)
                    WriterRSA.write(pubKey._save_pkcs1_pem())
                    WriterRSA.close()
                    with open("System.key", "rb") as ReaderRSA:
                        Getter = ReaderRSA.readlines(90)
                        Decr = Key_Enc.decrypt(Getter[0])
                        Key_ENC_DCR = Fernet(Decr)
                        Encrypter = Key_ENC_DCR.encrypt(privKey._save_pkcs1_pem())
                        with open("SystemCore.key", "wb") as WriterCore:
                            WriterCore.write(Encrypter)
                            self.SaveTHREE()
                            WriterCore.close()

    def SaveTWO(self):
        Lower_Case_Letter = "abcdefghijklmnopqrstuvwxyz"
        Upper_Case_Letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Symbols = "!@#$%^&*()-_=+[{]}|;:',<.>/"
        Numbers = "0123456789"
        source_pass = ""
        source_pass += Lower_Case_Letter
        source_pass += Symbols
        source_pass += Numbers
        source_pass += Upper_Case_Letter
        amount = 1
        lenght = 16
        for x in range(amount):
            Pass = "".join(random.sample(source_pass, lenght))
            self.ids.GenTWOSavepassword.text = Pass
            self.SaveTHREE()
class GenPopup(Popup):
    def SaveInf(self):
        try:
            with open("SystemConfiguration.pem", "rb") as EncReader:
                email1 = self.ids.GenSaveEmail.text
                password1 = self.ids.GenSavePassword.text
                Name = self.ids.GenSaveName.text
                Encode1 = email1.encode()
                Encode2 = password1.encode()
                Geterr = EncReader.read()
                Encrypter = rsa.PublicKey.load_pkcs1(Geterr)
                Encrypter1 = rsa.encrypt(Encode1, Encrypter)
                Encrypter2 = rsa.encrypt(Encode2, Encrypter)
                # try:
                self.sm = App.get_running_app().root
                user = self.sm.current_screen.ids.user.text
                book1 = [Name,Encrypter1,Encrypter2,None,None,None]
                conn = sqlite3.connect("SystemVault.sqlite", timeout=10)
                cur = conn.cursor()
                cur.execute(f"INSERT INTO {user}(Name,Email,Password,Web,Age,Phone) VALUES(?,?,?,?,?,?)",
                            book1)
                conn.commit()
                conn.close()
                messagebox.showinfo("PassSaver -Saver Information Manager", "Account Saved Successfully")
                self.dismiss()
                # except:
                #     messagebox.showerror("PassSaver -Structure Manager", "System File Error\nTry Restart App")


        except FileNotFoundError:
            messagebox.showinfo("PassSaver -Encrypter Manager",
                                "PassSaver Encrypting And Reading Information For More Security\nthis Opration Will Take 10seconds\nPlease Wait...")
            with open("System.key", "wb") as Writer:
                Key = Fernet.generate_key()
                Key1 = b'Qlqeg6eT2E3QAIUwk3RjcvnWf0uJvCJaNN9nFqeqZc8='
                Key_Enc = Fernet(Key1)
                Writer.write(Key_Enc.encrypt(Key))
                Writer.close()
                with open("SystemConfiguration.pem", "wb") as WriterRSA:
                    (pubKey, privKey) = rsa.newkeys(2048)
                    WriterRSA.write(pubKey._save_pkcs1_pem())
                    WriterRSA.close()
                    with open("System.key", "rb") as ReaderRSA:
                        Getter = ReaderRSA.readlines(90)
                        Decr = Key_Enc.decrypt(Getter[0])
                        Key_ENC_DCR = Fernet(Decr)
                        Encrypter = Key_ENC_DCR.encrypt(privKey._save_pkcs1_pem())
                        with open("SystemCore.key", "wb") as WriterCore:
                            WriterCore.write(Encrypter)
                            self.SaveInf()
                            WriterCore.close()
    def Core_Genration(self):
        Upper_Case_Letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Lower_Case_Letter = "abcdefghijklmnopqrstuvwxyz"
        Symbols = "!@#$%^&*()-_=+[{]}|;:',<.>/"
        Numbers = "0123456789"
        source_pass = ""
        source_email = ""
        if Value[0] == True:
            source_pass += Upper_Case_Letter
        if Value[1] == True:
            source_pass += Lower_Case_Letter
        if Value[2] == True:
            source_pass += Symbols
        if Value[3] == True:
            source_pass += Numbers
        amount = 1
        length = 12
        length1 = 6
        try:
         for x in range(amount):
            password = "".join(random.sample(source_pass,length))
            self.ids.GenSavePassword.text = password
        except:
            messagebox.showerror("Error", "The Password Selected is Too weak")

        source_email += Lower_Case_Letter
        source_email += Numbers
        for x in range(amount):
            email = "".join(random.sample(source_email, length1))
            email += "@gmail.com"
            self.ids.GenSaveEmail.text = email



    def Upper(self,instance,value):

      if value == True:
          Value[0] = True
      else:
          Value[0] = False
    def Lower(self,instance,value):

        if value == True:
            Value[1] = True
        else:
            Value[1] = False
    def Symbols(self,instance,value):

        if value == True:
            Value[2] = True
        else:
            Value[2] = False
    def Numbers(self,instance,value):

        if value == True:
            Value[3] = True
        else:
            Value[3] = False
class PassSaverSecond(Screen):
    Window.clearcolor = "#ffffff"
    def FileEnc(self):
        messagebox.showinfo("PassSaver -File Manager","We Are Very sorry\nThe File Encryption Function is Not Available For Now\nCheck App Update In Official Website")
    def Exit(self):
        asker =  messagebox.askyesno("PassSaver -Entry Gate Manager","Are You sure to Log out?")
        if asker == 1:
            user = [""]
            self.parent.current = "first"
if __name__ == "__main__":
    PassSaverApp().run()
