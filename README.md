# USSD App

This is a simple USSD application simulation that runs on the command line.

## Features

- Create User
- Delete User
- Display Users
- Start Session
- End Session
- Display Sessions
- Check Balance
- Recharge
- View Transaction History

## How to Run

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install pipenv && pipenv install`
5. Run the application: `python ussd_app.py`

## Project Structure

- `ussd_app.py`: Main script to run the application.
- `models.py`: Contains the data model classes.
- `cli.py`: Contains the CLI logic.
- `Pipfile`: Manages dependencies.
- `README.md`: Project description.
