import streamlit as st


def show_candidate(candidate):

    st.subheader("👤 Candidate")

    st.write("**Name:**", candidate["Name"])

    st.write("**Email:**", candidate["Email"])

    st.write("**Phone:**", candidate["Phone"])

    st.write("**Education:**")

    st.write(candidate["Education"])

    st.write("**GitHub:**", candidate["GitHub"])

    st.write("**LinkedIn:**", candidate["LinkedIn"])