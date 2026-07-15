import streamlit as st
from auth.auth import register_user


def signup_page():

    st.markdown(
        """
        <div class="login-card">

            <div class="login-title">
                🤖 AI Resume Screening System
            </div>

            <div class="login-subtitle">
                Create your Recruiter Account
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container():

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            with st.form("signup_form"):

                name = st.text_input(
                    "👤 Full Name"
                )

                email = st.text_input(
                    "📧 Email"
                )

                show = st.checkbox(
                    "Show Password"
                )

                if show:

                    password = st.text_input(
                        "🔒 Password"
                    )

                    confirm = st.text_input(
                        "🔒 Confirm Password"
                    )

                else:

                    password = st.text_input(
                        "🔒 Password",
                        type="password"
                    )

                    confirm = st.text_input(
                        "🔒 Confirm Password",
                        type="password"
                    )

                agree = st.checkbox(
                    "I agree to the Terms & Conditions"
                )

                signup = st.form_submit_button(
                    "✨ Create Account"
                )

            if signup:

                if not name or not email or not password or not confirm:

                    st.error(
                        "Please fill all fields."
                    )

                    return

                if password != confirm:

                    st.error(
                        "Passwords do not match."
                    )

                    return

                if not agree:

                    st.warning(
                        "Please accept the Terms & Conditions."
                    )

                    return

                success, message = register_user(
                    name,
                    email,
                    password
                )

                if success:

                    st.success(message)

                    st.info(
                        "Account created successfully. Please switch to the Login tab."
                    )

                else:

                    st.error(message)

    st.markdown(
        """
        <div style="text-align:center;
                    color:#9ca3af;
                    margin-top:15px;">

        Secure Recruiter Registration

        </div>
        """,
        unsafe_allow_html=True
    )