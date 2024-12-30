# # import streamlit as st
# # import time
# # st.title('Startup Dashboard')
# # st.header('learning streamlit')
# # st.subheader('learning streamlit !!')
# # st.write('Starting')
# # st.markdown("""
# # ### My Favourite movies:-
# #     - Race 3
# #     - Inception
# #     - The Matrix
# #     - Interstellar
# # """)
# # st.code("""
# # import pandas as pd

# # df = pd.DataFrame({
# #     'Name': ['Alice', 'Bob', 'Charlie'],
# #     'Age': [25, 30, 35],
# #     'City': ['New York', 'London', 'Paris']
# # })""")

# # st.latex('x^2 +y^2 + 2=0')
# # import pandas as pd
# # df = pd.DataFrame({
# #     'Name': ['Alice', 'Bob', 'Charlie'],
# #     'Age': [25, 30, 35],
# #     'City': ['New York', 'London', 'Paris']
# # })
# # st.dataframe(df)

# # st.metric('revenue','Rs 3L','-3%')

# # st.json({
# #     'Name': ['Alice', 'Bob', 'Charlie'],
# #     'Age': [25, 30, 35],
# #     'City': ['New York', 'London', 'Paris']
# # })

# # st.image('/Users/shiv_sharan/Desktop/1.jpg')
# # st.video('/Users/shiv_sharan/Desktop/revision/4.Spark dataframe transformation/13. Week 6 - Summary.mp4')
# # st.sidebar.title('Sidebar Ka Title')
# # col1,col2,col3=st.columns(3)
# # with col1:
# #     st.text('Left Column')
# #     st.image('/Users/shiv_sharan/Desktop/1.jpg')
# # with col2:
# #     st.text('Right Column')
# #     st.image('/Users/shiv_sharan/Desktop/1.jpg')
# # with col3:
# #     st.text('Third Column')
# #     st.image('/Users/shiv_sharan/Desktop/1.jpg')
# # st.error('Something went wrong')
# # st.success('Success')
# # st.warning('Warning')
# # st.info('Information')
# # st.spinner('Loading...')
# # bar=st.progress(0)
# # for i in range(100):
# #     bar.progress(i+1)
# #     time.sleep(0.1)

# # #take input
# # email=st.text_input('Enter email address')
# # number=st.number_input('Enter age')
# # date=st.date_input('Enter dob')

# # #Taking input user and create login form 
# import streamlit as st
# # email=st.text_input('Enter email address')
# # password=st.text_input('Enter password')
# # gender=st.selectbox('Select Gender',['male','female'])
# # btn=st.button('login')

# # #if the button is clicked
# # if btn:
# #     if email=='admin@gmail.com' and password=='1234':
# #         st.balloons()
# #         st.write(gender)
# #         st.success('Logged in successfully')
# #     else:
# #         st.error('Invalid credentials')


# #file uploader
# import pandas as pd
# file=st.file_uploader('Upload a file')
# if file is not None:
#     df=pd.read_csv(file)
#     st.dataframe(df.describe())
#     st.text('File uploaded successfully')
#     st.write(file.read())

# # slider