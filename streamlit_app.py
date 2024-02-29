
import numpy as np
import pandas as pd
import streamlit as st
import requests
from streamlit_card import card



st.image('https://uploads-ssl.webflow.com/632dd68fe0b7c272647b519b/63346c400e5b737f80250c4a_GoD%20Logo%20(no%20tagline).svg.svg')

st.header('Select Multiple API Data Sources')



name, pw, button1 = st.columns(3, gap='large')

with name:
    email = st.text_input('Email:')

with pw:
    password = st.text_input('Password:', type='password')

with button1:
    st.button('Submit')

st.divider()

def fetch_card_templates():
    try:
        url = 'https://app.getourdata.com/rest/v1/getourdata/getapi'
        headers = {
            'x-api-key': 'Vzg_5NsT6_zv1cLxvG5bSQ',
            'content-type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except Exception as e:
        print(e)
        return []
    

card_templates_data = fetch_card_templates()

card_templates_df = pd.DataFrame(card_templates_data['items'])
#st.write(card_templates_data['items'])
#st.write(card_templates_df)
# adding a comment
data_list = []

data = card_templates_data['items']
col1, col2, col3, col4 = st.columns(4, gap='small')
count = 0
for val in data:
    count = count+1
    variable = 'res'
    dyres = variable + str(count) 
    if (count % 4 == 0):
        with col3:
            
            res = card(
                title = val['description'],
                text = val['category'],
                image = val['iconURL'],
                styles = {
                    "card": {
                        "width": "100%",
                        "height": "300px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    
                    },
                    "text": {
                        "font-family": "serif"
                    }
                }
                
            )
    if (count % 4 == 1):
        with col1:
            
            res = card(
                title = val['description'],
                text = val['category'],
                image = val['iconURL'],
                styles = {
                    "card": {
                        "width": "100%",
                        "height": "300px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    
                    },
                    "text": {
                        "font-family": "serif"
                    }
                }
            )
    if (count % 4 == 2):
        with col2:
            
            res = card(
                title = val['description'],
                text = val['category'],
                image = val['iconURL'],
                styles = {
                    "card": {
                        "width": "100%",
                        "height": "300px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    
                    },
                    "text": {
                        "font-family": "serif"
                    }
                }
            )
    if (count % 4 == 3):
        with col4:
            
            res = card(
                title = val['description'],
                text = val['category'],
                image = val['iconURL'],
                styles = {
                    "card": {
                        "width": "100%",
                        "height": "300px",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    
                    },
                    "text": {
                        "font-family": "serif"
                    }
                }
            )
            
            if res:
                st.write(val['description'])