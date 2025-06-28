# AI-for-Software-Engineering
Building Intelligent Software Solutions
# Automated Login Testing with Selenium

 Project Overview:
This project automates login functionality testing using Selenium WebDriver in Python. It tests both valid and invalid login scenarios on a sample login page at [Practice Test Automation](https://practicetestautomation.com/practice-test-login/).

The test case uses user input to simulate real-world behavior and verifies whether login attempts succeed or fail as expected.

---

 Features:
- Accepts manual input for both valid and invalid credentials
- Automatically launches and controls the browser
- Waits for elements to load using explicit waits
- Provides terminal output for pass/fail results
- Keeps browser open until the user closes it

---

  Files Included
| File | Description |
|------|-------------|
| `login_test.py` | The main Python script using Selenium WebDriver |
| `login_test_results.png` | Screenshot of successful test run showing both pass/fail results |
| `summary.txt` or `.docx` | 150-word explanation of how AI improves test coverage |
| `README.md` | This file, explaining the project |

---

 Test Credentials (for demo site)
- ✅ Valid:  
  - Username: `student`  
  - Password: `Password123`

- ❌ Invalid:  
  - Username: `wrongUser`  
  - Password: `wrongPass`

---

 How to Run
1. Open the terminal in VS Code
2. Run the script:
   ```bash
   python login_test.py
