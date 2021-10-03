# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:24:55 2021

@author: hp
"""

from tkinter import*
import random
   
root=Tk()
root.title("RANDOM LIST ANS LUCKY FRIEND GENERATER")
root.geometry("700x400")

enter_country=Entry(root)
enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)
enter_city=Entry(root)
enter_city.place(relx=0.5,rely=0.4,anchor=CENTER)

label_country_list=Label(root)
label_random_country=Label(root)
label_random_country_name=Label(root)

label_city_list=Label(root)
label_random_city=Label(root)
label_random_city_name=Label(root)

list1=[]
list2=[]
def add_country_and_city():
    country_name=enter_country.get()
    list1.append(country_name)
    label_country_list["text"]="Your country list is : " + str(list1)
    
    city_name=enter_country.get()
    list2.append(city_name)
    label_city_list["text"]="Your city list is : " + str(list2)

def random_country_city():
    length=len(list1)
    random_no=random.randint(0,lenght-1)
    label_random_country["text"]= str(list1)
    genarated_random_country=list1[list1]
    label_random_country_name["text"]="YOUR RANDOM COUNTRY IS : " + str(genarated_random_country)

    length=len(list2)
    random_no2=random.randint(0,lenght-1)
    label_random_city["text"]= str(list2)
    genarated_random_city=list1[list2]
    label_random_city_name["text"]="YOUR RANDOM CITY IS : " + str(genarated_random_city)

button1=Button(root,text="ADDD TO YOUR COUNTRY AND CITY LIST!!" , command=add_country_and_city)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)
label_country_list.place(relx=0.5,rely=0.4,anchor=CENTER)
  
button2=Button(root,text="DISPLAY RANDOM COUNTRY AND CITY!!!!" , command=random_country_city)
button2.place(relx=0.5,rely=0.5,anchor=CENTER) 

label_random_country.place(relx=0.5,rely=0.7,anchor=CENTER)
label_random_country_name.place(relx=0.5,rely=0.8,anchor=CENTER)

label_random_city.place(relx=0.5,rely=0.9,anchor=CENTER)
label_random_city_name.place(relx=0.5,rely=1,anchor=CENTER)
root.mainloop()
