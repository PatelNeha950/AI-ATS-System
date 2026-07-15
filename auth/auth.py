import bcrypt

from auth.database import get_connection


# =====================================================
# Register User
# =====================================================

def register_user(name, email, password):

    conn = get_connection()

    cursor = conn.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    if cursor.fetchone():

        conn.close()

        return False, "Email already registered."

    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Save user
    cursor.execute(
        """
        INSERT INTO users(name, email, password)
        VALUES (?, ?, ?)
        """,
        (
            name,
            email,
            hashed_password.decode("utf-8")
        )
    )

    conn.commit()
    conn.close()

    return True, "Registration Successful."


# =====================================================
# Login User
# =====================================================

def login_user(email, password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:

        return False, "Email not found."

    stored_password = user["password"]

    if bcrypt.checkpw(
        password.encode("utf-8"),
        stored_password.encode("utf-8")
    ):

        return True, dict(user)

    return False, "Incorrect Password."