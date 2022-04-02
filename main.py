import streamlit as st
from time import sleep

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    sleep(0.1)

'Done !!!!!'    

left_colunm, right_column = st.columns(2)
button = left_colunm.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
