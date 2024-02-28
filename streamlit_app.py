
import numpy as np
import pandas as pd
import streamlit as st
import requests
from streamlit_card import card


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

data = card_templates_data['items']
col1, col2, col3, col4 = st.columns(4)
count = 0
for val in data:
    count = count+1
    variable = 'res'
    dyres = variable + str(count) 
    if (count % 4 == 1):
        with col1:
            
            res = card(
                title = val['description'],
                text = val['category'],
                image = val['iconURL'],
                styles = {
                    "card": {
                        "width": "40vw",
                        "height": "40vw",
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
                        "width": "100vw",
                        "height": "100vw",
                        "border-radius": "10px",
                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                    
                    },
                    "text": {
                        "font-family": "serif"
                    }
                }
            )