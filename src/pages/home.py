from flet import View
import flet as ft
from flet import *
import random
import time
import socket
import logging

logging.basicConfig(filename="C:/Users/jacob/Documents/Python/Roscri-Studio/logs/rs-home_ui.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

rand_clr=random.randint(000000,999999)


def page_nav(e,):
    time.sleep(2)
    e.page.go("/dashboard")

# ft.after(3000,page_nav())

host_name=ft.Text(socket.gethostname(),color="#FFFFFF",size=25,style=ft.TextThemeStyle.TITLE_MEDIUM)


sim_status=ft.Text("Activate Simulation",color="#000000",style=ft.TextThemeStyle.LABEL_LARGE)
sim_switch=ft.Switch(value=False,active_color="0C5473",inactive_thumb_color="#559FBF",active_track_color="#F6F6F6",inactive_track_color="#FFFFFF",on_change=lambda e:sw_status(e))

def sw_status(e):
    if(sim_switch.value==True):
        sim_status.value="Simulation Activated"
        page_nav(e)
        e.page.update()
        #sim=sim_switch.value
        return sim_switch.value
    else:
        sim_status.value="Activate Simulation"
        e.page.update()

def check_on(e):
    home_login.visible=False
    loader.visible=True
    e.page.update()

loader=ft.ProgressRing(visible=False,width=30, height=30, stroke_width = 2,color="#0C5473")
    
title_bar=ft.Row(spacing=0,controls=[
        ft.Container(expand=0,width=100,height=40,bgcolor='#0C5473'),
        ft.Container(expand=0,width=300,padding=padding.only(left=13),height=40,bgcolor='#FFFFFF',content=
                     ft.Row(controls=[
                            sim_status,sim_switch
                            ])),
        ft.Container(expand=0,padding=padding.only(top=5,left=250),width=800,height=40, bgcolor='#FFFFFF',content=
                     ft.Text("Roscri Studio",color="#000000",style=ft.TextThemeStyle.TITLE_SMALL)),
        ft.Container(expand=0,width=120,height=40,bgcolor="#FFFFFF",padding=padding.only(left=80),content=
                     ft.Row(controls=[ft.Icon(ft.icons.CLOSE_FULLSCREEN_OUTLINED,color="#0C5473",size=18)])),
        ft.Container(expand=1,width=130,bgcolor="#FD5454",height=40,image_src='C://Users//jacob//Documents//Python//Roscri-Studio//img//Exit.png',on_click=lambda e: e.page.window_destroy() )
        
    ])
ip_add = ft.TextField(visible=True,label="IP Address", autofocus=True,hint_text="Please enter IP address here",border_color="#FFFFFF")
port = ft.TextField(label="Port No.", hint_text="Port",border_color="#FFFFFF")
connect_btn=ft.OutlinedButton(text="Connect Now",on_click=check_on)


home_login=ft.Container(visible=True,image_src='C://Users//jacob//Documents//Python//Roscri-Studio//img//home_bg.jpeg',image_fit=ImageFit.COVER, width=1100, height=600,border_radius=15, padding=padding.only(right=20),content=
                            ft.Row(alignment=ft.MainAxisAlignment.END,controls=[
                                ft.Container(padding=padding.only(left=20,right=20),border_radius=15,bgcolor="#0C5473", width=400, height=500,content=
                                    ft.Column(spacing=0,alignment=ft.MainAxisAlignment.SPACE_EVENLY,controls=[
                                        ft.Text("Welcome to Roscri",size=30,style=ft.TextThemeStyle.TITLE_SMALL),
                                        ft.Text("Connect your UR Arm",size=15),
                                        ip_add,port,connect_btn
                                    ]))]))

main_dashboard=ft.Row(controls=[
        ft.Container(width=1300,height=670,bgcolor="#EAF4F9",margin=margin.only(left=30,right=25),border_radius= ft.border_radius.all(10),content=
                     ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[home_login,loader])),
    ])



def _view_():
    return ft.View(
        "/home",spacing=0,padding=0,bgcolor="#EAF4F9",
        controls=[title_bar,main_dashboard])