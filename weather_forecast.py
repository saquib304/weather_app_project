from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2a9785a8cb0e597de1c1a37007e2b285").json()
    W_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    pr_label1.config(text=data["main"]["pressure"])

win=Tk()
win.title("Weather")
win.config(bg="light blue")
win.geometry("500x570")
     
name_label=Label(win,text="Saquib Weather App",font=("Aerial",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Saquib Weather App",values=list_name,font=("Aerial",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)



W_label=Label(win,text="Weather Climate",font=("Aerial",20))
W_label.place(x=25,y=260,height=50,width=210)
W_label1=Label(win,text="",font=("Aerial",20))
W_label1.place(x=250,y=260,height=50,width=210)


wd_label=Label(win,text="Weather Description",font=("Aerial",17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1=Label(win,text="",font=("Aerial",17))
wd_label1.place(x=250,y=330,height=50,width=210)



temp_label=Label(win,text="Temperature",font=("Aerial",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("Aerial",20))
temp_label1.place(x=250,y=400,height=50,width=210)



pr_label=Label(win,text="Pressure",font=("Aerial",20))
pr_label.place(x=25,y=470,height=50,width=210)
pr_label1=Label(win,text="",font=("Aerial",20))
pr_label1.place(x=250,y=470,height=50,width=210)

done_button=Button(win,text="Done",font=("Aerial",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()
