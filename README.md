# 🏧 ATM Web Application using Flask & MySQL

A simple ATM simulation web app built with **Python (Flask)**, **HTML**, and **MySQL** using **PyMySQL**. It includes functionalities like Withdraw, Deposit, Mini Statement, and PIN Generation.

---

## 🚀 Features

- ✅ Home Page
- 💳 Withdraw Money (with PIN validation)
- 💰 Deposit Money
- 📄 Mini Statement (view account details)
- 🔐 PIN Generation

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- PyMySQL
- HTML/CSS
- MySQL (as the database)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/atm-web-app.git
cd atm-web-app
2. Install Dependencies
Make sure you have Python and pip installed. Then install Flask and PyMySQL:

bash
Copy
Edit
pip install Flask PyMySQL
3. MySQL Database Setup
Open MySQL and create a database named atm.

Create a table named ACCOUNTS with the following structure:

sql
Copy
Edit
CREATE TABLE ACCOUNTS (
    USER_ID INT PRIMARY KEY AUTO_INCREMENT,
    USER_NAME VARCHAR(100),
    USER_EMAIL VARCHAR(100),
    USER_ACCNO VARCHAR(20) UNIQUE,
    USER_PIN INT,
    USER_BALANCE INT
);
Insert some sample data for testing:

sql
Copy
Edit
INSERT INTO ACCOUNTS (USER_NAME, USER_EMAIL, USER_ACCNO, USER_PIN, USER_BALANCE)
VALUES ('John Doe', 'john@example.com', '1234567890', 1234, 10000);
4. Run the Application
bash
Copy
Edit
python app.py
By default, the app runs on: http://localhost:5016

🌐 Routes Overview
Route	Method	Description
/ or /home	GET	Home page
/withdraw1	GET	Enter account and PIN
/withdraw2	POST	Validate PIN and proceed
/withdraw3	POST	Perform withdrawal
/deposit1	GET	Deposit form
/deposit2	POST	Deposit money
/ministatement1	GET	Enter details to view statement
/ministatement2	POST	Display mini statement
/pingeneration1	GET	Enter account number
/pingeneration2	POST	Check PIN availability
/pingeneration3	POST	Set a new PIN

⚠️ Notes
Ensure MySQL is running and credentials in db_config are correct.

Error handling is done via messages on rendered templates.

This project is for learning purposes and not meant for production use.

📷 Screenshots
(Add screenshots of the UI if available)

📬 Contact
Developer: [Your Name]
Email: your.email@example.com
GitHub: https://github.com/your-username

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

Let me know if you want me to generate a `requirements.txt`, folder structure, or HTML templates too.






You said:
it is to upload in github so give accordingly


ChatGPT said:
Great! Here's a GitHub-ready README.md file for your Flask-based ATM Web App project. It includes a clean structure, badges, and sections typically expected in open-source projects.

markdown
Copy
Edit
# 🏧 ATM Web Application (Flask + MySQL)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8.x-blue?logo=mysql)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A simple and functional ATM simulation web app built using **Flask**, **PyMySQL**, **HTML/CSS**, and **MySQL**. Users can withdraw and deposit money, view mini statements, and generate PINs.

---

## 🔥 Features

- 🏠 Home Page
- 💳 Withdraw (with account and PIN validation)
- 💰 Deposit to Account
- 📄 Mini Statement (Account Info)
- 🔐 PIN Generation

---

## 📂 Project Structure

atm-web-app/
│
├── templates/
│ ├── home.html
│ ├── withdraw1.html
│ ├── withdraw2.html
│ ├── deposit1.html
│ ├── ministatement1.html
│ ├── ministatement2.html
│ ├── pingeneration1.html
│ └── pingeneration2.html
│
├── app.py
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

### 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/atm-web-app.git
cd atm-web-app
Install dependencies

bash
Copy
Edit
pip install Flask PyMySQL
Set up MySQL database

Open your MySQL client and run:

sql
Copy
Edit
CREATE DATABASE atm;

USE atm;

CREATE TABLE ACCOUNTS (
    USER_ID INT PRIMARY KEY AUTO_INCREMENT,
    USER_NAME VARCHAR(100),
    USER_EMAIL VARCHAR(100),
    USER_ACCNO VARCHAR(20) UNIQUE,
    USER_PIN INT,
    USER_BALANCE INT
);
Insert sample data:

sql
Copy
Edit
INSERT INTO ACCOUNTS (USER_NAME, USER_EMAIL, USER_ACCNO, USER_PIN, USER_BALANCE)
VALUES ('Alice Smith', 'alice@example.com', '9876543210', 1234, 15000);
Run the application

bash
Copy
Edit
python app.py
App runs on: http://localhost:5016

🌐 Available Routes
Route	Method	Description
/ or /home	GET	Home page
/withdraw1	GET	Enter account number and PIN
/withdraw2	POST	Validate credentials
/withdraw3	POST	Withdraw money
/deposit1	GET	Deposit form
/deposit2	POST	Deposit money to account
/ministatement1	GET	Mini statement input form
/ministatement2	POST	Display account details
/pingeneration1	GET	Enter account number
/pingeneration2	POST	Check PIN availability
/pingeneration3	POST	Generate new PIN

🧪 Testing
Try various scenarios like wrong PIN, no account found, insufficient balance, etc.

Debug logs are printed in the terminal (via print(data) statements).

🛡️ Disclaimer
This app is built for educational/demo purposes only and should not be used for real banking transactions.

🤝 Contributing
Contributions are welcome!
Feel free to open issues or submit pull requests.

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Shashi Kumar K
🔗 GitHub
🔗 LinkedIn
