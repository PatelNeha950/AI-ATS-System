import streamlit as st
from auth.auth import login_user


def login_page():

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([2, 1, 2])

    with center:

        st.markdown(
            """
            <div class="login-card">
                <div class="login-title">
                    🤖 AI Resume Screening System
                </div>

                <div class="login-subtitle">
                    Intelligent Applicant Tracking System
                </div>
            """,
            unsafe_allow_html=True
        )

        email = st.text_input(
            "📧 Email",
            placeholder="Enter your email"
        )

        show_password = st.checkbox(
            "👁 Show Password"
        )

        if show_password:

            password = st.text_input(
                "🔒 Password"
            )

        else:

            password = st.text_input(
                "🔒 Password",
                type="password"
            )

        remember = st.checkbox(
            "Remember Me"
        )

        login = st.button(
            "🚀 Login",
            use_container_width=True
        )

        if login:

            if email == "" or password == "":

                st.error(
                    "Please enter Email and Password."
                )

            else:

                success, result = login_user(
                    email,
                    password
                )

                if success:

                    st.session_state.logged_in = True
                    st.session_state.user = result
                    st.session_state.remember = remember

                    st.success(
                        "Login Successful!"
                    )

                    st.rerun()

                else:

                    st.error(result)

        st.markdown(
            """
            <br>

            <center>

            <span style='color:#9ca3af;'>

            Secure Login • AI Powered Recruitment

            </span>

            </center>

            </div>
            """,
            unsafe_allow_html=True
        )