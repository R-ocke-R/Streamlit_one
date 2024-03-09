import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image

#--- Path Settings 
# using pathlib to import Path function which helps me keep track of the 
# current directory, making my code resilient/ poratble.
page_title = "Investing"
page_icon = "random"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
imageEarly = current_dir / "assets" / "PercentEarly10.png"
imageLate = current_dir / "assets" / "PercentLate10.png"
imagetwenty = current_dir / "assets" / "percent20.png"
video = "https://www.youtube.com/watch?v=WEDIj9JBTC8&ab_channel=BigThink"
stdocs = "https://streamlit.io"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout = "wide", initial_sidebar_state="collapsed")

st.title('Investing 101: Visualizing the Value of Time')
#st.markdown("Hey There! This project Investing 101 is an web app that is created and hosted ")

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("Why ?"):
        st.write("""This project is based on a [video](%s) by Big Think. Where William Ackman introduces finance and investing in under an hour. My mentor shared this video with me during a discussion about whether to delay my masters by a year. 
                 You can watch the full video or from 21:30 mark, where it gets pretty exciting as Ackman highlights the importance of compound interest and the significant impact of starting early on a person's portfolio with the charts that I have captured below. """ % video)
with col2:
    with st.expander("How?"):
        st.write("""This interactive web app is built using [Streamlit](%s), a Python library. 
                 Inspired by the investing lecture, I set out to test Streamlit's capabilities by creating this application. 
                 During development, I encountered various challenges, leading me to learn additional Python libraries such as 
                 Pillow for image handling, BeautifulSoup for web scraping, and requests for data retrieval. 
                 I also utilized pathlib to ensure portability and resilience to path changes. 
                 Streamlit provided an ideal platform for translating my idea into a functional and user-friendly interface.""" %stdocs) 
with col3:
    with st.expander("Who is William Ackman?"):
        st.write("Bill Ackman founded and runs Pershing Square Capital Management, a hedge fund with $16 billion in assets under management.")
        st.write("Pershing Square's stock portfolio is concentrated in just seven companies, including Chipotle, Hilton and Google parent Alphabet. ")
        col1, col2, col3 = st.columns([0.3, 2, 2])
        with col2:
            st.metric(label='Net Worth', value = '$4.3B', delta = '-0.57%', help="According to Forbes as of 9/3/24" )
        with col3:
            flink= "https://www.forbes.com/profile/william-ackman/?sh=2a6adb10298d"
            st.link_button("Forbes Link", flink, help="William Ackman")

#RULE 1
with st.expander("Rule No. 1: Starting Early", True):
    cl1, cl2 = st.columns(2)
    ie=Image.open(imageEarly)
    il=Image.open(imageLate)
    with cl1:
        st.image(ie, caption = """Investing $10000 dollars at age 22 at 10% rate""")
    with cl2:
        st.image(il, caption = 'Investing $10000 dollars at age 32 at 10% rate')

# Warren 20% Percent
with st.expander("What if you're warren buffet. 10% Interest Ain't enough for you. right?"):
    cc,cv,cb = st.columns([1,2,1])
    i20=Image.open(imagetwenty)
    with cv :
        st.image(i20, caption = """Yeah that's 24 million dollars from an original $10000 investment """)

#
st.header("""So here comes my contribution (yes my aim wasn't to just show you 
         some images from youtube) this project highlight is the iteractive
        visualisaiton of growth of money which can help you decide 
        how much you wanna invest at what right and at what time 
        """)


# Currency type input
col1, col2, col3 = st.columns(3)
with col1:
    currency_type = st.selectbox('Select Currency Type', ['USD', 'EUR', 'GBP', 'INR'])

# Amount input
with col2:
    amount = st.number_input(f'Enter Amount in {currency_type}', step=1000)

# Years to invest input
with col3:
    years = st.number_input('Enter Years to Invest', min_value=1, step=1, value=1)

# Projected rate of increase input
# rate_of_increase = st.slider('Projected Rate of Increase (%)', min_value=0.1, max_value=20.0, step=0.1)

# # Calculate compound interest
# years_range = np.arange(1, years + 1)
# compound_interest = amount * (1 + rate_of_increase / 100) ** years_range

# # Plot growth over the years
# fig, ax = plt.subplots()
# ax.plot(years_range, compound_interest, marker='o', color='b')
# ax.set_xlabel('Years')
# ax.set_ylabel('Amount')
# ax.set_title('Projected Growth Over the Years')
# st.pyplot(fig)

# # Calculate and display metrics
# total_growth = compound_interest[-1] - amount
# times_increased = len(compound_interest[1:] > compound_interest[:-1])
# st.metric('Total Growth', f'{currency_type} {total_growth:.2f}')
# st.metric('Times Increased', times_increased)
