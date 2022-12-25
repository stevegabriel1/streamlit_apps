import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
lists = st.container()
user_input = st.container()

with header:
    st.title('Welcome -  this is for my exploration of Streamlit functionality!')
    st.text('Modified from YouTube video "How to Integrate Machine Learning to Streamlit')
    st.text('- Part 3" (Misra Turp)')


with dataset:
    st.header('Google shares data')

    gdat = pd.read_csv('data/goog_stock.csv')
    st.write(gdat.head())
    st.subheader('Closing price from 2014 to current')
    st.subheader('GOOG')
    close_dat = pd.DataFrame(gdat['close'])
    st.line_chart(close_dat)

with lists:
    st.header('Here is some of the best music of 2022')
    st.markdown('* **The Smile:**   A Light For Attracting Attention ')
    st.markdown('* **King Stingray:**   King Stingray ')
    st.markdown('* **Sault:**   11 ')

with user_input:
        st.header('This section provides some user input options:')
        # create two columns within the user_input row/container
        select_col, display_col = st.columns(2)

        dave_runs = select_col.slider('What score will David Warner get in the 1st innings of the Boxing Day test (2022)?', min_value=0, max_value=250, value=35, step =1)
        dave_ducks = select_col.selectbox('How many ducks will he get in the test?', options = [0,1,2])

        display_col.text('1st innings runs: ')
        display_col.write(dave_runs, font_size = 100)
