import flet as ft
from flet import *
import time
import logging
import os
import ctypes

from pages.splash import _view_ as v1
from pages.home import _view_ as v2
from pages.dashboard import _view_ as v3
from pages.home import sw_status as sim

from mods.controller import *

dir_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename="C:/Users/jacob/Documents/Python/Roscri-Studio/logs/rs-main.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

def master(page=ft.Page):
    
    page.title="Roscri Studio"
    page.window_center()
    page.padding=0
    page.window_height=345
    page.window_width=500
    page.window_frameless=True
    page.window_minimized=False
    page.window_resizable=False

    splash=v1()
    home=v2()
    dashboard=v3()
    
    # swstat=ctypes.cast(sim, ctypes.py_object).value
    # print(swstat)

    # Creating an object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.window_maximized=True
            page.window_visible=True
            page.update()
            page.views.append(home)
        if page.route == "/dashboard":
            page.views.append(dashboard)
        if page.route == "/splash":
            page.views.append(splash)
        else:
            logger.critical("[Criticial]Routing is not complete. Please check source code.")

        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view=page.views[-1]
        page.go(top_view.route)

    page.on_route_change=route_change
    page.on_view_pop=view_pop
    page.go(page.route)

    page.views.append(dashboard)
    page.views.append(home)
    page.views.append(splash)
    page.update()

    logger.debug("Harmless debug Message")
    logger.info("Just an information")
    logger.warning("Its a Warning")
    logger.error("Did you try to divide by zero")
    logger.critical("Internet is down")

ft.app(target=master)#,view=ft.WEB_BROWSER)