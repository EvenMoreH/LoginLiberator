# 🔓 Login Liberator

**Login Liberator** is a demo web application built using [FastHTML](https://github.com/fastai/fasthtml) to showcase a complete login flow with CAPTCHA verification and session-based authentication. Selenium and ChromeDriver are used to automate browser interaction and validate the login logic.

---

## ✨ Features

- 🖥️ CAPTCHA validation before login
- 🔐 Session-based login authentication
- 🧠 Server-rendered HTML via `FastTags`
- ⚡ HTMX-powered client interactivity
- 🎨 Styled with Tailwind CSS
- 💻 Minimal JavaScript interactivity
- 🤖 UI automation testing with Selenium + ChromeDriver

---

## 🔧 Technologies Used

- **[FastHTML](https://github.com/fastai/fasthtml)** – Backend framework
- **HTMX** – Declarative client-server communication
- **Tailwind CSS** – Utility-first CSS for layout and styling
- **Selenium** – Automation and UI testing
- **ChromeDriver** – Headless browser control for testing
- **Custom JavaScript** – CAPTCHA handling and DOM updates

---

## 📁 Project Structure
```
📦LoginLiberator
 ┣ 📂app
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂css
 ┃ ┃ ┃ ┣ 📜input.css
 ┃ ┃ ┃ ┗ 📜tailwind.css
 ┃ ┣ 📜demo.py
 ┃ ┗ 📜scripts.py
 ┣ 📂tests
 ┃ ┣ 📜chromedriver.exe
 ┃ ┗ 📜test_login.py
 ┣ 📜.gitignore
 ┣ 📜LICENSE
 ┣ 📜pytest.ini
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜tailwind.config.js
```

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the App
```bash
python demo.py
```

### 3. Run Selenium Tests
```bash
pytest tests/
```

## 🧪 Automated Test Flow
The Selenium tests validate:
1. CAPTCHA verification must occur before login.
2. Only the correct admin / admin1 credentials are accepted.
3. UI behavior for failed login attempts and session resets.

## 📜 Notes
- CAPTCHA state and login status are stored in server-side sessions.
- CAPTCHA uses checkbox interaction with minimal custom JavaScript.
- Demo app uses mock credentials and should not be used in production.
- JavaScript is embedded in scripts.py and loaded via Script() in FastHTML components.

## 👨‍💻 Author
**EvenMoreH** – Made with FastHTML for fast, declarative full-stack apps in Python.