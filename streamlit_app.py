
import numpy as np
import pandas as pd
import streamlit as st
import requests


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
card_templates_df = pd.DataFrame(card_templates_data)
st.write(card_templates_df)