import streamlit as st

# Define colors
background_color = "#f8f9fa"
accent_color = "#007bff"
text_color = "#343a40"

# Define typography
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: """ + text_color + """;
        text-align: center;
        padding-top: 20px;
        padding-bottom: 20px;
    }
    .section-title {
        font-size: 24px;
        color: """ + accent_color + """;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    .content {
        font-size: 18px;
        color: """ + text_color + """;
        padding-bottom: 20px;
    }
    .link {
        color: """ + accent_color + """;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown(
        f"""
        <div style="background-color:{background_color};">
            <h1 class="title">My Portfolio</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="section-title">About Me</div>
        <div class="content">
            Hello! I'm [Your Name], a passionate [Your Profession].
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="section-title">Projects</div>
        <div class="content">
            <ol>
                <li>Project 1</li>
                <li>Project 2</li>
                <li>Project 3</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="section-title">Contact</div>
        <div class="content">
            You can reach me at [Your Email] or connect with me on:
            <br>
            <a class="link" href="Your LinkedIn Profile URL">LinkedIn</a>
            <br>
            <a class="link" href="Your GitHub Profile URL">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
