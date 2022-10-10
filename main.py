import streamlit as st


def main():
    st.write("## Example")
    value = streamlit_searchbar(label="Search Customer...")
    st.write(value)
    st.button("test")


if __name__ == "__main__":
    main()