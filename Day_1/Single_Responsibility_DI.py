"""
Problem Statement: A User handles user data persistence (saving to a database) and email notification in one place.  
This is violating to Single Responsibility Principle also
Dependency inversion as we will see that it is directly affected by implementations rather than abstractions 
"""

#Bad Design
# class BadUserManager:
#     def __init__(self):
#         self.database = PostgreSQLDatabase()
#         self.email_service = SendGridEmailService() # Violating Dependency inversion
    
#     def create_user(self, user_data):
#         self.database.insert(user_data) #Violating Single Responsibility.
#         self.email_service.send("Some spam email.")

