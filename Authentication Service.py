class AuthenticationService:
    def __init__(self):
        # Initialize a dictionary to store user credentials and roles
        self.user_db = {
            "user1": {"password": "password1", "role": "admin"},
            "user2": {"password": "password2", "role": "user"},
        }
        self.sessions = {}  # Store active session tokens

    def authenticate(self, username, password):
        """
        Authenticate a user based on username and password.
        
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        
        Returns:
            tuple: (auth_token, user_role) if authentication is successful, else (None, None).
        """
        if username in self.user_db and self.user_db[username]["password"] == password:
            auth_token = self.generate_auth_token(username)
            user_role = self.user_db[username]["role"]
            self.sessions[auth_token] = username  # Store the session
            return auth_token, user_role
        return None, None

    def generate_auth_token(self, username):
        """
        Generate a simple authentication token for the user.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            str: A simple token based on the username.
        """
        import time
        return f"{username}:{int(time.time())}"

    def authorize(self, auth_token):
        """
        Authorize a user based on the provided authentication token.
        
        Args:
            auth_token (str): The authentication token of the user.
        
        Returns:
            str: The role of the user if authorized, else None.
        """
        if auth_token in self.sessions:
            username = self.sessions[auth_token]
            return self.user_db[username]["role"]
        return None

    def logout(self, auth_token):
        """
        Log out a user by invalidating the authentication token.
        
        Args:
            auth_token (str): The authentication token of the user.
        """
        if auth_token in self.sessions:
            del self.sessions[auth_token]

# Example usage
if __name__ == "__main__":
    auth_service = AuthenticationService()
    token, role = auth_service.authenticate("user1", "password1")
    print(f"Token: {token}, Role: {role}")
    print(f"Authorization: {auth_service.authorize(token)}")
    auth_service.logout(token)
    print(f"Authorization after logout: {auth_service.authorize(token)}")