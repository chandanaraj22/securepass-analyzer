# 🛡️ SecurePass Analyzer

> **Enterprise Password Security Assessment Platform**

SecurePass Analyzer is a Flask-based cybersecurity tool that evaluates password strength using multiple security metrics instead of relying solely on basic complexity rules. The application combines entropy estimation, enterprise password policy validation, weak pattern detection, offline breached-password detection, and actionable security recommendations to provide users with a comprehensive password security assessment.

The project follows a modular architecture, making it easy to extend with additional password analysis techniques and security features.

---

## 📸 Application Preview

### Home Page

<img width="798" height="803" alt="Screenshot 2026-07-16 at 3 44 02 PM" src="https://github.com/user-attachments/assets/f90960cc-950f-4218-94b0-94f66df32146" />


`assets/screenshots/home.png`

---



### Password Analysis Dashboard

<img width="1136" height="359" alt="Screenshot 2026-07-16 at 8 15 12 PM" src="https://github.com/user-attachments/assets/8543757c-5ef5-4986-99b1-fe0d469b63a2" />
<img width="1440" height="900" alt="Screenshot 2026-07-16 at 8 03 31 PM" src="https://github.com/user-attachments/assets/3b233ff3-8e98-4118-956c-fb2f9cbc365b" />

`assets/screenshots/analysis.png`

---

# ✨ Features

- 🔐 Password complexity analysis
- 📊 Password entropy estimation
- 🛡 Enterprise password policy validation
- ⚠ Detection of weak password patterns
- 🔎 Offline breached-password detection using a curated dataset of 10,000 commonly compromised passwords
- 💡 Personalized password improvement recommendations
- 📈 Security score (0–100)
- 🚦 Password risk classification
- 👁 Show/Hide password functionality
- 🌙 Modern cybersecurity-inspired dashboard
- 📱 Responsive web interface

---

# 🔒 Security Checks Performed

SecurePass Analyzer evaluates passwords using the following security criteria:

- Minimum password length
- Uppercase letters
- Lowercase letters
- Numeric digits
- Special characters
- Password entropy calculation
- Common keyboard sequence detection
- Repeated character detection
- Enterprise password policy compliance
- Offline breached-password detection

---

# 🏗️ System Architecture

```
                    User Password
                          │
                          ▼
                  Flask Web Application
                          │
     ┌──────────────┬──────────────┬──────────────┐
     ▼              ▼              ▼
Complexity      Entropy      Policy Validation
     │              │              │
     └──────────────┼──────────────┘
                    ▼
          Weak Pattern Detection
                    │
                    ▼
     Offline Breached Password Check
                    │
                    ▼
      Recommendation & Risk Assessment
                    │
                    ▼
         Security Analysis Dashboard
```

---

# 📂 Project Structure

```
securepass-analyzer/

├── analyzer/
│   ├── __init__.py
│   ├── breach_check.py
│   ├── complexity.py
│   ├── entropy.py
│   ├── patterns.py
│   ├── policy.py
│   └── recommendations.py
│
├── datasets/
│   └── common_passwords.txt
│
├── static/
│   ├── favicon.svg
│   ├── logo.svg
│   └── style.css
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_passwords.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Icons | Bootstrap Icons |
| Styling | Custom CSS |
| Version Control | Git & GitHub |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/chandanaraj22/securepass-analyzer.git
```

Navigate to the project directory

```bash
cd securepass-analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py / flask run
```

Open the application in your browser

```
http://127.0.0.1:5000
```

---

# 📊 Sample Analysis

| Metric | Example |
|---------|---------|
| Security Score | 88 / 100 |
| Risk Level | Low Risk |
| Entropy | 74.3 bits |
| Complexity | Passed |
| Enterprise Policy | Passed |
| Breach Detection | Not Found |
| Recommendations | Password is considered secure |

---

# 💡 Future Improvements

- Integration with the Have I Been Pwned API
- NIST SP 800-63B password compliance
- Password generation utility
- Password cracking time estimation
- Multi-language support
- Password history analysis
- Exportable PDF security reports
- Light/Dark theme support

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python application development
- Flask web development
- Modular software architecture
- Password security principles
- Information security fundamentals
- Secure user interface design
- Git version control
- Responsive web development

---

# 👩‍💻 Author

**R. Chandana**

GitHub: https://github.com/chandanaraj22

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!
