import streamlit as st
from auth.auth import register_user


def signup_page():

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.title("🤖 AI Resume Screening System")
        st.caption("Create your Recruiter Account")

        with st.form("signup_form"):

            name = st.text_input(
                "👤 Full Name",
                key="signup_name"
            )

            email = st.text_input(
                "📧 Email",
                key="signup_email"
            )

            show = st.checkbox(
                "👁 Show Password",
                key="signup_show"
            )

            if show:

                password = st.text_input(
                    "🔒 Password",
                    key="signup_password_show"
                )

                confirm = st.text_input(
                    "🔒 Confirm Password",
                    key="signup_confirm_show"
                )

            else:

                password = st.text_input(
                    "🔒 Password",
                    type="password",
                    key="signup_password_hide"
                )

                confirm = st.text_input(
                    "🔒 Confirm Password",
                    type="password",
                    key="signup_confirm_hide"
                )

            agree = st.checkbox(
                "I agree to the Terms & Conditions",
                key="signup_agree"
            )

            signup = st.form_submit_button(
                "✨ Create Account",
                use_container_width=True
            )

        if signup:

            if not name or not email or not password or not confirm:

                st.error("Please fill all fields.")

            elif password != confirm:

                st.error("Passwords do not match.")

            elif not agree:

                st.warning("Please accept the Terms & Conditions.")

            else:

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
            <center>
                <span style="color:#9ca3af;">
                    Secure Recruiter Registration
                </span>
            </center>
            """,
            unsafe_allow_html=True
        )