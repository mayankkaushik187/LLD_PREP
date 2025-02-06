from abc import ABC, abstractmethod

class UserRepo(ABC):
    @abstractmethod
    def save(self, user_data: dict) -> None:
        pass

class EmailService(ABC):
    @abstractmethod
    def send_welcome_email(self, email: str) -> None: 
        pass

class PostgreSQLUserRepo(UserRepo):
    def save(self, user_data):
        print(f"Saving {user_data['name']}'s data to the DB.")

class SendGridEmailService(EmailService):
    def send_welcome_email(self, email):
        print(f"Sending notification to this email -> {email}")

class UserManager:
    def __init__(self, repo: UserRepo, email_service: EmailService):
        self.repo = repo
        self.email_service = email_service

    def create_user(self, user_data: dict) -> None:
        self.repo.save(user_data)
        self.email_service.send_welcome_email(user_data['email'])



postgrerepo = PostgreSQLUserRepo()
email_service = SendGridEmailService()
manager = UserManager(postgrerepo, email_service)
user_data = {}
user_data['name'] = "Mayank Kaushik"
user_data['email'] = "mayankcodes@hishome.com"
manager.create_user(user_data)