import streamlit as st
import streamlit_searchbar as sr


def main():
    st.write("## Example")
    value = sr.streamlit_searchbar(label="Search Customer...")
    st.write(value)
    if st.button("Check"):
        st.info(value + " has been typed")
    with st.expander("code"):
        st.code(body="import streamlit as st \r\n \
                      import streamlit_searchbar as sr \r\n \r\n \
                      value = sr.streamlit_searchbar(label='Search Customer...') \r\n \
                      st.write(value) \
    ",language="python")



if __name__ == "__main__":
    main()