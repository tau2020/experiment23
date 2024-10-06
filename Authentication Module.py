class AuthenticationModule:
    def __init__(self):
        # Initialize user database and session storage
        self.user_db = {}  # Dictionary to store user credentials
        self.sessions = {}  # Dictionary to store active sessions
        self.session_timeout = 3600  # Session timeout in seconds
        self.user_roles = {}  # Dictionary to store user roles

    def register_user(self, username, password, role):
        """
        Register a new user with a username, password, and role.
        :param username: str - The username of the user
        :param password: str - The password of the user
        :param role: str - The role of the user (e.g., 'admin', 'user')
        """
        if username in self.user_db:
            raise ValueError("Username already exists.")
        self.user_db[username] = password
        self.user_roles[username] = role

    def authenticate(self, username, password):
        """
        Authenticate a user with their username and password.
        :param username: str - The username of the user
        :param password: str - The password of the user
        :return: str - Authentication token if successful
        """
        if username in self.user_db and self.user_db[username] == password:
            token = self.generate_token(username)
            self.sessions[token] = username  # Store the session
            return token
        else:
            raise ValueError("Invalid username or password.")

    def generate_token(self, username):
        """
        Generate a simple token for the authenticated user.
        :param username: str - The username of the user
        :return: str - A simple token (for demonstration purposes)
        """
        import time
        return f"{username}:{int(time.time())}"

    def get_user_role(self, token):
        """
        Get the role of the user associated with the provided token.
        :param token: str - The authentication token
        :return: str - The role of the user
        """
        if token in self.sessions:
            username = self.sessions[token]
            return self.user_roles[username]
        else:
            raise ValueError("Invalid session token.")

    def invalidate_session(self, token):
        """
        Invalidate a user's session.
        :param token: str - The authentication token
        """
        if token in self.sessions:
            del self.sessions[token]

    def is_authenticated(self, token):
        """
        Check if the provided token is valid and the user is authenticated.
        :param token: str - The authentication token
        :return: bool - True if authenticated, False otherwise
        """
        return token in self.sessions

# Example usage
if __name__ == "__main__":
    auth_module = AuthenticationModule()
    auth_module.register_user("user1", "password123", "user")
    token = auth_module.authenticate("user1", "password123")
    print("Authenticated Token:", token)
    print("User Role:", auth_module.get_user_role(token))
    print("Is Authenticated:", auth_module.is_authenticated(token))
    auth_module.invalidate_session(token)
    print("Is Authenticated after invalidation:", auth_module.is_authenticated(token))