# AI Test Case Generator

Generate structured manual QA test cases from software requirements using Google's Gemini AI and export them to Excel.

## Features

* Generate manual functional test cases from natural language requirements
* Powered by Gemini AI
* Export results to Excel (.xlsx)
* Structured output with:

  * Test Case ID
  * Title
  * Preconditions
  * Test Steps
  * Expected Result
  * Priority

## Tech Stack

* Python
* Gemini API
* OpenPyXL
* python-dotenv

## Project Structure

```text
AI-TestCase-Generator/
│
├── app.py
├── excel_generator.py
├── .env
└── README.md
```

## Installation

```bash
pip install google-genai openpyxl python-dotenv
```

## Configuration

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Usage

Run the application:

```bash
python app.py
```

Enter a software requirement:

```text
User must log in using email and password.
```

The application will generate manual test cases and export them as an Excel file.

## Example Output

| Test Case ID | Title                        | Priority |
| ------------ | ---------------------------- | -------- |
| TC001        | Login with valid credentials | High     |
| TC002        | Login with invalid password  | High     |
| TC003        | Empty email                  | Medium   |

## Roadmap

* Excel formatting
* Requirement traceability
* Multiple requirement support
* Security test case generation
* Boundary value analysis
* Equivalence partitioning
* Export to CSV
* Export to PDF
