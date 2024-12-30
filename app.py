
# Preprocessing
# -> drop remarks column 
# -> set index sno 
# -> rename col  
# -> convert amount to cr rs   
# -> date col  
# -> dropna    
import streamlit as st
# import pandas as pd

from func import usd_to_inr,clean_date_column,pd,load_investors_details,st,load_general_analysis
st.set_page_config(layout='wide',page_title='Startup Funding Analysis')
df=pd.read_csv('/Users/shiv_sharan/Desktop/datasets/startup_funding.csv')
df.drop(columns=['Remarks'],inplace=True)
df.set_index('Sr No',inplace=True)
df.rename(columns={'Date dd/mm/yyyy' : 'Date',
                   'Startup Name': 'Startup',
                   'Industry Vertical':'Vertical',
                   'SubVertical':'subvertical',
                   'City  Location':'City',
                   'Investors Name':'Investors',
                   'InvestmentnType':'round',
                   'Amount in USD':'Amount',
                   },inplace=True)
df['Investors']=df['Investors'].fillna('undisclosed')
df['Amount']=df['Amount'].fillna('0')
df['Amount']=df['Amount'].str.replace(',','')
df['Amount']=df['Amount'].str.replace('undisclosed','0')
df['Amount']=df['Amount'].str.replace('unknown','0')
df['Amount']=df['Amount'].str.replace('Undisclosed','0')
df=df[df['Amount'].str.isdigit()]
df['Amount']=df['Amount'].astype('float')
#amount to crore
df['Amount']=df['Amount'].apply(usd_to_inr)
df.info()
#cleaning date column
df = clean_date_column(df, "Date")
#cleaning data column wise 
df.dropna(subset=['Date','Startup','Vertical','City','Investors','round','Amount'], inplace=True)

# df.info()
# st.dataframe(df)
#unique investors
# unique_investors = get_unique_investors(df)
# print("----->",unique_investors)
st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')
    # btn0=st.sidebar.button('Show Overall Analysis')
    # if btn0:
    load_general_analysis(df)
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup')
    st.title('Startup analysis')
else:
    selected_investors=st.sidebar.selectbox('Select Investor',sorted(set(df['Investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investors')
    st.title('Investors Analysis')
    if btn2:
        load_investors_details(selected_investors,df)

        



