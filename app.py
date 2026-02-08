import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Happy Valentine’s Day 💖",
    page_icon="💘",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM CSS (BACKGROUND + POLAROID STYLE)
# -------------------------------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #F6A5C0;
}

/* Title */
.title {
    font-family: 'cursive';
    font-size: 48px;
    text-align: center;
    color: black;
    margin-bottom: 30px;
}

/* Polaroid */
.polaroid {
    background: white;
    padding: 15px 15px 40px;
    width: 300px;
    margin: auto;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    transform: rotate(-3deg);
    text-align: center;
}

/* Caption */
.caption {
    font-family: cursive;
    font-size: 22px;
    margin-top: 10px;
    color: black;
}

/* Question text */
.question-small {
    text-align: center;
    font-size: 22px;
    color: black;
}

.question-big {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown("<div class='title'>Happy Valentine’s Day 💘</div>", unsafe_allow_html=True)

# -------------------------------------------------
# POLAROID PHOTO
# -------------------------------------------------
st.markdown("<div class='polaroid'>", unsafe_allow_html=True)
st.image("assets/herpic.jpg", use_container_width=True)
st.markdown("<div class='caption'>My forever ❤️</div></div>", unsafe_allow_html=True)

# -------------------------------------------------
# SPACING
# -------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------
# VALENTINE QUESTION
# -------------------------------------------------
st.markdown("""
<div class='question-small'>
I made this app just to ask you one thing…
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='question-big'>
Will you be my Valentine? 💖
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# YES BUTTON (NO NO BUTTON 😌)
# -------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("💖 YES 💖"):
        st.balloons()
        st.markdown("""
        <h2 style='text-align:center; color:black;'>
        YAY!! You just made me the happiest person ever 😭❤️
        </h2>
        """, unsafe_allow_html=True)
