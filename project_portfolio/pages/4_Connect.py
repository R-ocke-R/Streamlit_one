import streamlit as st



def feedback_form():
    st.title("Let's Connect! 🚀")
    st.write("""Hello There 👋 
             Thank you for visiting this website. It's a new idea that I'm excited to bring to life, and work on it will be starting soon. Stay tuned for updates!""")
    st.write("If you want to be updated when this is up or wanna team up for a streamlit project,please drop down your information below, I will make sure do send through and enjoy. ")
    st.write("Have a great day ! ")
    st.write("I will be thrilled to hear from you! Your feedback will help me improve. 😊")
    st.write("Please share any thoughts, ideas, or suggestions you have. 💡")

    name = st.text_input("Your Name 👤", "")
    email = st.text_input("Your Email 📧", "")
    feedback = st.text_area("Your Feedback / Feature Request ✏️", "")

    if st.button("Submit Feedback"):
        if name and email and feedback:
            # You can save the feedback to a database or send it via email
            st.success("Thank you for your feedback! We'll get back to you soon. 🙌")
        else:
            st.warning("Oops! It looks like you missed filling out some fields. Please make sure to provide your name, email, and feedback. 🛑")

if __name__ == "__main__":
    feedback_form()
