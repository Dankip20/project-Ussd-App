# cli.py
from models import User, USSDSession
from colorama import init, Fore, Style
from termcolor import colored

init(autoreset=True)

class USSDApp:
    def __init__(self):
        self.users = []
        self.sessions = []

    def create_user(self):
        name = input(colored("Enter user name: ", 'cyan'))
        phone_number = input(colored("Enter phone number: ", 'cyan'))
        if not phone_number.isdigit():
            print(colored("Invalid phone number. Must be digits only.", 'red'))
            return
        user = User(name, phone_number)
        self.users.append(user)
        print(colored(f"User {name} created successfully.", 'green'))

    def delete_user(self):
        phone_number = input(colored("Enter phone number of user to delete: ", 'cyan'))
        user = self.find_user(phone_number)
        if user:
            self.users.remove(user)
            print(colored(f"User with phone number {phone_number} deleted successfully.", 'green'))
        else:
            print(colored("User not found.", 'red'))

    def display_users(self):
        if not self.users:
            print(colored("No users found.", 'yellow'))
            return
        for user in self.users:
            print(colored(f"Name: {user.name}, Phone: {user.phone_number}", 'blue'))

    def find_user(self, phone_number):
        for user in self.users:
            if user.phone_number == phone_number:
                return user
        return None

    def create_session(self):
        phone_number = input(colored("Enter phone number of user to start session: ", 'cyan'))
        user = self.find_user(phone_number)
        if user:
            session = USSDSession(user)
            self.sessions.append(session)
            print(colored(f"Session started for user {user.name}.", 'green'))
            self.session_menu(session)
        else:
            print(colored("User not found.", 'red'))

    def delete_session(self):
        phone_number = input(colored("Enter phone number of user to end session: ", 'cyan'))
        session = self.find_session(phone_number)
        if session:
            self.sessions.remove(session)
            print(colored(f"Session for user with phone number {phone_number} ended successfully.", 'green'))
        else:
            print(colored("Session not found.", 'red'))

    def find_session(self, phone_number):
        for session in self.sessions:
            if session.user.phone_number == phone_number:
                return session
        return None

    def display_sessions(self):
        if not self.sessions:
            print(colored("No sessions found.", 'yellow'))
            return
        for session in self.sessions:
            print(colored(f"User: {session.user.name}, Balance: {session.balance}", 'blue'))

    def session_menu(self, session):
        while True:
            print(colored("\nSession Menu", 'magenta', attrs=['bold']))
            print(colored("1. Check Balance", 'cyan'))
            print(colored("2. Recharge", 'cyan'))
            print(colored("3. View Transaction History", 'cyan'))
            print(colored("b. Back to Main Menu", 'cyan'))
            choice = input(colored("Select an option: ", 'cyan'))

            if choice == '1':
                balance = session.check_balance()
                print(colored(f"Your balance is ${balance}", 'green'))
            elif choice == '2':
                amount = input(colored("Enter amount to recharge: ", 'cyan'))
                if amount.isdigit():
                    new_balance = session.recharge(int(amount))
                    print(colored(f"Recharged successfully. New balance is ${new_balance}", 'green'))
                else:
                    print(colored("Invalid amount. Must be digits only.", 'red'))
            elif choice == '3':
                history = session.view_transaction_history()
                if history:
                    print(colored("Transaction History:", 'blue'))
                    for record in history:
                        print(colored(record, 'blue'))
                else:
                    print(colored("No transactions found.", 'yellow'))
            elif choice.lower() == 'b':
                break
            else:
                print(colored("Invalid choice. Please try again.", 'red'))

    def run(self):
        while True:
            print(colored("\nUSSD App", 'magenta', attrs=['bold']))
            print(colored("1. Create User", 'cyan'))
            print(colored("2. Delete User", 'cyan'))
            print(colored("3. Display Users", 'cyan'))
            print(colored("4. Start Session", 'cyan'))
            print(colored("5. End Session", 'cyan'))
            print(colored("6. Display Sessions", 'cyan'))
            print(colored("q. Quit", 'cyan'))
            choice = input(colored("Select an option: ", 'cyan'))

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.delete_user()
            elif choice == '3':
                self.display_users()
            elif choice == '4':
                self.create_session()
            elif choice == '5':
                self.delete_session()
            elif choice == '6':
                self.display_sessions()
            elif choice.lower() == 'q':
                print(colored("Exiting the application.", 'green'))
                break
            else:
                print(colored("Invalid choice. Please try again.", 'red'))
