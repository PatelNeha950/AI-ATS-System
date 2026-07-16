import streamlit as st
from auth.auth import login_user


def login_page():

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.title("🤖 AI Resume Screening System")
        st.caption("Intelligent Applicant Tracking System")

        email = st.text_input(
            "📧 Email",
            placeholder="Enter your email",
            key="login_email"
        )

        show = st.checkbox(
            "👁 Show Password",
            key="login_show"
        )

        if show:
            password = st.text_input(
                "🔒 Password",
                key="login_password_show"
            )
        else:
            password = st.text_input(
                "🔒 Password",
                type="password",
                key="login_password_hide"
            )

        remember = st.checkbox(
            "Remember Me",
            key="remember"
        )

        login = st.button(
            "🚀 Login",
            use_container_width=True,
            key="login_button"
        )

        if login:

            if not email or not password:
                st.error("Please enter Email and Password.")

            else:

                success, result = login_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user = result
                    st.session_state.remember_user = remember
                    st.rerun()

                else:
                    st.error(result)

        st.markdown(
            """
            <center>
                <span style="color:#9ca3af;">
                    Secure Login • AI Powered Recruitment
                </span>
            </center>
            """,
            unsafe_allow_html=True
        )