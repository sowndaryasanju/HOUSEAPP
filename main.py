from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import  MDCard
from tabulate import tabulate
import mysql.connector
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty




class HomeWindow(Screen):
    def _init_(self,**kwargs):

        super(HomeWindow,self)._init_(**kwargs)
        pass



class SearchWindow(Screen):
    temp=[]
    def _init_(self,**kwargs):
       # self.temp[]
        self.a="empty"
        super(SearchWindow,self)._init_(**kwargs)
        pass
    def FlatDetails(self,Screen):
        s=str(self.ids.FlatNo.text)
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="42R_68ch",
            database="yaanji")
        l=(s,)
        mycursor=mydb.cursor()
        mycursor.execute("select Status from block1 where FlatNo=%s",l)
        for i in mycursor:
            self.temp.append(i)
        a=str(self.temp[0])
        a.replace(')'," ")
        a.replace('(', " ")
        a.replace("/'", " ")
        self.ids.op.text=a
        mycursor.close()


class availabilityWindow(Screen):
    temp=[]
    def _init_(self,**kwargs):
        #self.temp[]
        super(availabilityWindow,self)._init_(**kwargs)
        pass
    def buy(self,Screen):
        self.temp.clear()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="42R_68ch",
            database="yaanji")
        mycursor = mydb.cursor()
        s = ("buy",)
        mycursor.execute("select * from block1 where Status=%s",s)
        for i in mycursor:
            self.temp.append(i)
        self.ids.table.text=tabulate(self.temp,tablefmt="plain")
    def rent(self,Screen):
        self.temp.clear()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="42R_68ch",
            database="yaanji")
        mycursor = mydb.cursor()
        s = ("rent",)
        mycursor.execute("select * from block1 where Status=%s",s)
        for i in mycursor:
            self.temp.append(i)
        self.ids.table.text=tabulate(self.temp,tablefmt='orgtbl')

class galleryWindow(Screen):
    temp=["1.png","2.png","3.png"]
    def _init_(self,**kwargs):
        #self.temp[]
        super(galleryWindow,self)._init_(**kwargs)
        pass
    def front(self,Screen):
        if(self.ids.img.source==self.temp[0]):
            self.ids.img.source=self.temp[1]
        elif(self.ids.img.source==self.temp[1]):
            self.ids.img.source=self.temp[2]
        else:
            self.ids.img.source = self.temp[0]
    def back(self, Screen):
         if (self.ids.img.source == self.temp[0]):
            self.ids.img.source = self.temp[2]
         elif (self.ids.img.source == self.temp[1]):
            self.ids.img.source = self.temp[0]
         else:
            self.ids.img.source =self.temp[1]
class contactWindow(Screen):
    temp=[]
    def _init_(self,**kwargs):
        #self.temp[]
        super(contactWindow,self)._init_(**kwargs)
        pass
    def info(self,Screen):
        self.temp.clear()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="42R_68ch",
            database="yaanji")
        mycursor = mydb.cursor()

        mycursor.execute("select * from contact")
        for i in mycursor:
            self.temp.append(i)
        return tabulate(self.temp)
class aboutWindow(Screen):
    pass
class WindowManager(ScreenManager):
     pass
#class MainWidget(Widget):
#    pass
kv = Builder.load_file('new_window.kv')

class HomeTaxApp(App):
    def build(self):
        return kv


if _name=='main_':
    HomeTaxApp().run()
