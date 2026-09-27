# Selenium Python Automation Framework

A simple, beginner-friendly Selenium Automation Framework built for college submissions and viva presentations.

It automates **Login** and **Product Search** on [TutorialsNinja](https://tutorialsninja.com/demo/) using **Page Object Model (POM)**.

---

## 📁 Simple Flattened Structure

```text
selenium-project/
├── pages/                      # Page Object Model (locators + UI actions)
│   ├── base_page.py            # Common helper methods (click, enter_text, get_text)
│   ├── login_page.py           # Login page actions
│   └── search_page.py          # Search page actions
├── data/                       # Test Data files
│   ├── login_data.csv          # Login test scenarios
│   └── search_data.csv         # Product search test scenarios
├── tests/                      # Test cases
│   ├── conftest.py             # Setup, teardown & screenshot on failure
│   ├── test_login.py           # PyTest Login tests (data-driven with CSV)
│   ├── test_search.py          # PyTest Search tests (data-driven with CSV)
│   └── test_unittest.py        # Unittest test cases (using unittest.TestCase)
├── utils.py                    # Reusable helper functions (driver, config, CSV)
├── config.ini                  # Settings (URL, headless mode)
├── pytest.ini                  # PyTest configuration
├── requirements.txt            # Python packages (installed via pip)
└── README.md
```

---

## ⚡ Quick Setup & Run (3 Steps)

### Step 1: Create and activate virtual environment
**On Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
**On Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the tests

**Run all tests and generate HTML report:**
```bash
pytest
```
*(Report is generated at `reports/report.html`)*

**Run with Python's built-in `unittest`:**
```bash
python -m unittest tests/test_unittest.py
```

---

## 🎓 Easy Explanation for College Viva / Review

| Component | What it does | Why it is used |
| :--- | :--- | :--- |
| **Page Object Model (`pages/`)** | Separates HTML locators from test logic. | If a button ID changes on the website, we only update the page file, not every test file. |
| **Test Data (`data/*.csv`)** | Contains test inputs in CSV format. | Allows testing multiple valid/invalid cases using a single test function (`@pytest.mark.parametrize`). |
| **Utility Helper (`utils.py`)** | Common helpers for browser setup, CSV reading, and config. | Keeps code DRY (Don't Repeat Yourself) in a single clean file. |
| **Configuration (`config.ini`)** | Stores `base_url` and `headless` mode. | Allows switching URLs or test settings without changing Python code. |
| **Screenshots on Failure (`conftest.py`)** | Takes a screenshot if any test fails. | Helps in debugging failed test runs. |
| **HTML Reporting (`pytest-html`)** | Creates `reports/report.html`. | Visual dashboard showing passed/failed tests and execution time. |
