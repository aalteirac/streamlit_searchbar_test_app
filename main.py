import streamlit as st
import streamlit_searchbar as sr
 

def main():
    st.set_page_config(layout="wide")
    hide_streamlit_style = """
        <style>
            #root > div:nth-child(1) > div > div > div > div > section > div { padding: 0rem 1rem;}
            header[data-testid="stHeader"]{display:none}
        </style>

        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    value = sr.streamlit_searchbar(label="Search Customer...")
    if value is not None and value !="":st.write(value)
    if st.button("Check"):
        st.info(value + " has been typed")
    with st.expander("code"):
        st.code(body="\
# pip install streamlit-searchbar\r\n\
import streamlit as st \r\n\
import streamlit_searchbar as sr \r\n \r\n\
value = sr.streamlit_searchbar(label='Search Customer...') \r\n\
st.write(value) \
    ",language="python")



if __name__ == "__main__":
    main()