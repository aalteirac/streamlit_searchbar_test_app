import streamlit as st
import streamlit_searchbar as sr


def main():
    st.write("## Example")
    value = sr.streamlit_searchbar(label="Search Customer...")
    st.write(value)
    if st.button("Check"):
        st.info(value + " has been typed")



if __name__ == "__main__":
    main()