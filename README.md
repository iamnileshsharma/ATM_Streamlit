# ATM App

A simple ATM simulation web application built with Python and Streamlit. Users can register, log in, deposit, withdraw, and reset their password. Data is stored in a local SQLite database.

## Features

- User registration and login
- Account dashboard with balance display
- Deposit and withdraw money
- Password reset functionality
- Session management

## Project Structure

```
.
├── main.py
├── registration.py
├── login.py
├── dashboard.py
├── utils.py
├── database.py
├── atm.db
├── .gitignore
└── __pycache__/
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [SQLite3](https://www.sqlite.org/index.html) (bundled with Python)

### Installation

1. Clone the repository:
    ```sh
    git clone <your-repo-url>
    cd ATM
    ```

2. Install dependencies:
    ```sh
    pip install streamlit
    ```

### Running the App

Start the Streamlit app with:
```sh
streamlit run main.py
```

The app will open in your browser.

## Usage

- **Register:** Create a new account with a unique username.
- **Login:** Access your dashboard after logging in.
- **Deposit/Withdraw:** Manage your account balance.
- **Reset Password:** Change your password securely.

## License

This project