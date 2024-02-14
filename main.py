import streamlit as st
st.write("# Hi there 👋 I am Manu Sharma \n ### This is my first streamlit website \n ### I am really excited to explore how streamlit can help me build apps to better showcase my data science projects" )

st.write(" \n")


st.subheader('Subheader', divider='rainbow')
# st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')


col1, col2 = st.columns(2)
# col1.write(' :red[Column 1]')
# col2.write(' :red[Column 2]')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
# col1 is wider

st.subheader('Button Feature', divider='rainbow')

if st.button('Cat'):
    st.write("Cat")
    st.image('cat.gif')
else:
    st.write("Dog")
    st.image('dog.gif')

# Using 'with' notation:
# with col1: 
#     st.image('cat.gif')
# with col2:
#     st.image('dog.gif')

# st.write("\n \n ##### Here is a video of kanye west")
# st.video('kanye.mp4')
    

