
from flask import Flask, flash, request, render_template, redirect, url_for
from posixpath import sep
import flask
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os
import json
import sys


dir = os.path.dirname
path = dir(dir(dir(__file__)))
sys.path.append(path)

from src.utils.apis_tb import read_json


df = None
menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Graphs", "API"])

st.title('Maritime industry web app')
st.write('This is a web app to show with different graphs the evolution of merchant fleet and the possible relation oil price has on the industry.')
if menu == 'Welcome':
    st.title('Maritime industry web app')
st.write('This is a web app to show.')
if menu == 'Graphs':
    graph = st.selectbox('Select a graph:',
                        options= ['BrentvsBDI', 'fleet growth', 'fleetvsSeatrade', 'seatrade GDP correlation', 'seatrade and Brent price correlation'])
    if graph == 'BrentvsBDI':
        image = Image.open(path + os.sep + 'Resources' + os.sep + 'BrentvsBDI.png')
        st.image(image,use_column_width=True)
    if graph == 'fleet growth':
        col1, col2 = st.beta_columns([2, 4])
        with col1:
            image = Image.open(path + os.sep + 'Resources' + os.sep + 'World_fleet_evol.png')
            st.image(image,use_column_width=True)
        with col2:
            image2= Image.open(path + os.sep +  'Resources' + os.sep + 'avgeVStotalDweight.png')
            st.image (image2,use_column_width=True)
    if graph == 'fleetvsSeatrade':
        image = Image.open(path + os.sep + 'Resources' + os.sep + 'seatrade_Brent.png')
        st.image(image)
    if graph == 'seatrade GDP correlation':
        image = Image.open(path + os.sep + 'Resources' + os.sep + 'seatrade_world_GDP.png')
        st.image(image)
    if graph == 'seatrade and Brent price correlation':
        image = Image.open(path + os.sep + 'Resources' + os.sep + 'seatrade_Brent.png')
if menu == 'API':
    #user_input = st.text_area("Enter password")
    #if st.button('Submmit'):
        #answer = 'http:localhost:6060/get_API' + '?password=' + user_input
        #readed_json = pd.read_csv(answer)
    st.table(pd.read_json('http://localhost:6060/get_API?password=L16092222'))
    


    



