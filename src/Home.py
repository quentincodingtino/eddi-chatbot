import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="📬", page_title="Eddi likes an email 📬")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**Email:**",
"[Q@teamcircle.tech)]")

    st.write("**Linkedin:** "
"linkedin.com/in/qawesome")

    st.write("**Created by Circle**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Eddi, your email writing assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Eddi, an intelligent email bot created from publically available information like historical email's you've sent my creators. I use large language models to provide
    context-sensitive interactions. My goal is to help you work faster and get future fit.
    I also support PDF, TXT, CSV reference uploads 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Get Started")
st.write(""" **Head over the "Eddi likes an email" tab and give me a topic of the email, who it is for, and and any key points to include and I'll right you up an email. **
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Approval")
st.markdown("""
**Eddi likes an email. Please approve the scope so Eddi can have more emails. **
""", unsafe_allow_html=True)





