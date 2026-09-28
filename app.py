import streamlit as st
from logic import sum

st.title('My Home Page')
st.header('I am header')
st.markdown('**STREAMLIT IS AMAZING**')
st.markdown('# HEADING 1')
st.markdown('## HEADING 2')
st.markdown('### HEADING 3')
st.markdown('#### HEADING 4')
st.markdown('##### HEADING 5')
st.markdown('###### HEADING 6')

st.title('You rock :heart_eyes: :100: :white_check_mark:')

st.code('''
//Hello world in java
class Test{
public static void main(String args[])
{
System.out.println("Hello All");
}
}
''',language='java'
)
st.divider()

st.text("I am amitava",help='https://github.com/cloudsony999?tab=repositories')
st.text(f"the sum of {10} and {20} is {sum(10,20)}",help='calling function')


t1=st.text_input('enter name')

if st.button('click me'):
    st.write('your name is ',t1)