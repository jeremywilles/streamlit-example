
import numpy as np
import pandas as pd
import streamlit as st
import requests
from streamlit_card import card

def post_to_vinyl(data_list, email, password):
    for item in data_list:
        if item['Email'] == '':
            item['Email'] = email
            print(item['Email'])
        if item['Password'] == '':
            item['Password'] = password

    url = 'https://app.getourdata.com/rest/v1/getourdata/tableaudataconnector'

    headers = {'X-API-KEY': "Vzg_5NsT6_zv1cLxvG5bSQ", "Content-Type": "application/json"}
    try:
        requests.post(url, headers=headers, data=data_list)
    except Exception as error:
         print("error posting to vinyl: ", error)

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

st.set_page_config(
    page_title="GetOurData API Selection",
    layout="wide"
)

img1,img2,img3 = st.columns(3, gap="small")

with img2:

    st.image('https://uploads-ssl.webflow.com/632dd68fe0b7c272647b519b/63346c400e5b737f80250c4a_GoD%20Logo%20(no%20tagline).svg.svg')

    st.header('Enter your email address and select your APIs.')



name, pw, button1 = st.columns(3, gap='large')



with pw:
    newuser = st.radio("",["New User", "Existing User"])
    email = st.text_input('Email:')
    password = ''
        
    if newuser == 'Existing User':
        password = st.text_input('Password:', type='password')
    if email != '':
        #st.button('Submit', on_click=post_to_vinyl, args=[data_list, email, password])
        if st.button('Submit'):
            post_to_vinyl(data_list, email, password)
            st.subheader("Thank you for your submission! New users check for an email from GetOurData with login instructions.")
            st.subheader("Existing users login here:")
            st.link_button('GetOurData:' , "https://app.getourdata.com")

    
st.divider()
    
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
            if res:
                #st.write(res)
                #st.write(val['templateAPIID'], email, password)
                try:
                    newPassword = password
                except NameError:
                    password = ''
                values = {'templateAPIID': val['templateAPIID'], 'Email': email, 'Password': password}
                
                if values in data_list:
                    data_list.remove(values)
                else:
                    data_list.append(values)
                #st.write(data_list)
                st.write('API Added')
            
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
            if res:
                #st.write(res)
                #st.write(val['templateAPIID'], email, password)
                try:
                    newPassword = password
                except NameError:
                    password = ''
                values = {'templateAPIID': val['templateAPIID'], 'Email': email, 'Password': password}
                
                if values in data_list:
                    data_list.remove(values)
                else:
                    data_list.append(values)
                #st.write(data_list)
                st.write('API Added')
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
            if res:
                #st.write(res)
                #st.write(val['templateAPIID'], email, password)
                try:
                    newPassword = password
                except NameError:
                    password = ''
                values = {'templateAPIID': val['templateAPIID'], 'Email': email, 'Password': password}
                
                if values in data_list:
                    data_list.remove(values)
                else:
                    data_list.append(values)
                #st.write(data_list)
                st.write('API Added')
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
            
#           st.button('Add API', key=val['templateAPIID'], on_click=data_insert, args=[val['templateAPIID'], email, password], use_container_width=True)
            if res:
                #st.write(res)
                #st.write(val['templateAPIID'], email, password)
                try:
                    newPassword = password
                except NameError:
                    password = ''
                values = {'templateAPIID': val['templateAPIID'], 'Email': email, 'Password': password}
                
                if values in data_list:
                    data_list.remove(values)
                else:
                    data_list.append(values)
                #st.write(data_list)
                st.write('API Added')
                


    
# def data_insert(templateID, email, password):
#     values = {'templateAPIID': templateID, 'Email': email, 'Password': password}
#     if values in data_list:
#         data_list.remove(values)
#     else:
#         data_list.append(values)
#     st.write(data_list)
              
                
# def data_insert(templateID, email, password):
#     values = {'templateAPIID': templateID, 'Email': email, 'Password': password}
#     if values in data_list:
#         data_list.remove(values)
#     else:
#         data_list.append(values)
#     st.write(data_list)



# '''
# IF in data_list
#     pop
# ELSE
#     append

# data_list= [

#     {'templateAPIID': '089e9ec4-a7fc-11ed-81a5-062e82398976', 'Email': email, 'Password': password}
# ]
# '''