from datetime import datetime
from dateutil import parser
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
def usd_to_inr(usd):
    return (usd*85)/10000000

def clean_date_column(df, column_name):
    """
    Cleans and parses dates in a specified column of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the column to clean.
        column_name (str): The name of the column with dates to clean.

    Returns:
        pd.DataFrame: DataFrame with cleaned date column as datetime type.
    """
    def parse_date(date_str):
        try:
            # Try to parse the date using dateutil.parser
            parsed_date = parser.parse(date_str, fuzzy=True)
            # Remove time and return only the date
            return parsed_date.date()
        except (ValueError, TypeError):
            # Return NaT if parsing fails
            return pd.NaT

    # Apply the parsing function to the column
    df[column_name] = df[column_name].apply(parse_date)
    # Convert the column to datetime type
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df

def get_unique_investors(df, column_name='Investors'):
    """
    This function takes a DataFrame and a column name, splits the strings in the column by ',', 
    converts them to lowercase, removes duplicates, and returns the unique investors.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column containing investor strings.

    Returns:
        list: A list of unique investor names.
    """
    # Flatten the list of investors by splitting and converting to lowercase
    all_investors = df[column_name].str.split(',').sum()
    all_investors_lower = [investor.strip().lower() for investor in all_investors]
    print("investors", all_investors,all_investors_lower)
    # Create a sorted set of investors
    unique_investors_set = sorted(set(all_investors_lower))

    # Iterate through the rows and filter out duplicates
    filtered_investors = []
    for investor in unique_investors_set:
        if all(investor not in row.lower() for row in df[column_name].dropna()):
            filtered_investors.append(investor)
    print("Filtered",filtered_investors)
    return filtered_investors
def load_investors_details(selected_investors,df):
    """
    This function loads investor details from a DF.
    """
    st.dataframe(df)
    # st.title(selected_investors)
    #load the recent five investors
    last5_df=df[df['Investors'].str.contains(selected_investors)].head()[['Date','Startup','Vertical','City','round','Amount']]
    st.subheader(f"Recent 5 investments by {selected_investors}")
    st.dataframe(last5_df)
    col1,col2 = st.columns(2)
    with col1:
        #load Biggest investments
        st.subheader(f"Biggest investments by {selected_investors}")
        biggest_invest=df[df['Investors'].str.contains(selected_investors)].groupby('Startup')['Amount'].sum().sort_values(ascending=False)
        # st.dataframe(biggest_invest.head())
        fig, ax = plt.subplots()
        ax.bar(biggest_invest.index,biggest_invest.values)
        st.pyplot(fig)
    with col2:
        vector_series=df[df['Investors'].str.contains(selected_investors)].groupby('Startup')['Amount'].sum()
        st.subheader(f"Sectors invested in {selected_investors}")
        fig, ax = plt.subplots()
        ax.pie(vector_series,labels=vector_series.index,autopct='%1.1f%%')
        st.pyplot(fig)
    #     st.dataframe(biggest_invest.head())
    #stage wise pie
    col3,col4 = st.columns(2)
    with col3:
        round_series=df[df['Investors'].str.contains(selected_investors)].groupby('round')['Amount'].sum()
        st.subheader(f"Stage wise invested by {selected_investors}")
        fig, ax = plt.subplots()
        ax.pie(round_series,labels=round_series.index,autopct='%1.1f%%')
        st.pyplot(fig)
        # return selected_investors
    with col4:
        city_series=df[df['Investors'].str.contains(selected_investors)].groupby('City')['Amount'].sum()
        st.subheader(f"City Wise invested by {selected_investors}")
        fig, ax = plt.subplots()
        ax.pie(city_series,labels=city_series.index,autopct='%1.1f%%')
        st.pyplot(fig)
    df['year']=df['Date'].dt.year
    yearwise_series=df[df['Investors'].str.contains(selected_investors)].groupby('year')['Amount'].sum()
    st.subheader(f"YOY investment by {selected_investors}")
    fig, ax = plt.subplots()
    ax.plot(yearwise_series.index,yearwise_series.values)
    st.pyplot(fig)

def load_general_analysis(df):
    """
    This function loads general analysis.
    """
    # st.title('General Analysis')
    total = round(df['Amount'].sum())
    col1,col2,col3,col4=st.columns(4)
    
    max_fund = df.groupby('Startup')['Amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_fund = df.groupby('Startup')['Amount'].sum().mean()
    total_fund = df['Startup'].nunique()
    print(total_fund)
    with col1:
        st.metric('Total Fund Spent in Indian Market',str(total)+'Cr')
    with col2:
        st.metric('Maximum Fund Raised by a Startup', str(max_fund) +'Cr')
    with col3:
        st.metric('Average Fund Raised by a Startup', str(round(avg_fund))+'Cr')
    with col4:
        st.metric('Total Fund Startups',str(total_fund)+'Cr')
    
    #Month on month chart(line)
    st.header('MoM chart')
    df['year']=df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    selected_options=st.selectbox('select type',['Total','Count'])
    if selected_options=='Total':
        temp_df = df.groupby(['year','month'])['Amount'].sum().reset_index()
    elif selected_options=='Count':
        temp_df = df.groupby(['year','month'])['Amount'].count().reset_index()
    
    # temp_df = df.groupby(['year','month'])['Amount'].sum().reset_index()
    temp_df['x_axis']=temp_df['month'].astype(str) + temp_df['year'].astype(str)
    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'], temp_df['Amount'])
    st.pyplot(fig)
    

    


