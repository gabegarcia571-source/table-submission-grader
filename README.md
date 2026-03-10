# submission-grader

A lightweight Python script that automatically grades student lab submissions. Built for instructors who receive `.docx`, `.pdf`, or `.txt` files and want a quick pass/fail grade based on answer completeness — no manual review needed.

---

## What It Does

- Scans a `submissions/` folder for student files
- Detects whether answers are in a **two-column table** (Question | Answer) or **numbered text** (1. ... 2. ...)
- Counts how many questions have a substantive answer (> 3 characters, not "optional")
- Assigns **1 point** if ≥ 8/10 questions are answered, **0 points** otherwise
- Exports results to `grading_results.csv`

---

## Supported File Types

| Format | Graded? |
|--------|---------|
| `.docx` | ✅ Yes |
| `.pdf` | ✅ Yes |
| `.txt` | ✅ Yes |
| `.rtf` | ✅ Yes |
| `.pages` / `.odt` | ✅ Yes (plain-text read) |
| `.xlsx`, `.pptx`, `.zip` | ⏭ Silently skipped |

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/submission-grader.git
cd submission-grader
```

**2. Install dependencies**
```bash
python setup.py
```

This installs: `pdfplumber`, `python-docx`, `pandas`

---

## Usage

**1. Drop student files into the `submissions/` folder**

```
submission-grader/
├── submissions/
│   ├── alice_lab1.docx
│   ├── bob_lab1.pdf
│   └── carol_lab1.txt
├── grade_labs.py
└── setup.py
```

**2. Run the grader**
```bash
python grade_labs.py
```

**3. Check results**

A `grading_results.csv` is created with columns:

| Student File | File Type | Questions Answered | Points (out of 1) | Status |
|---|---|---|---|---|
| alice_lab1.docx | .docx | 10 | 1 | Complete |
| bob_lab1.pdf | .pdf | 4 | 0 | Incomplete |
| carol_lab1.txt | .txt | 0 | 0 | No Submission / Empty |

---

## Configuration

Edit the constants at the top of `grade_labs.py` to customize:

```python
SUBMISSIONS_FOLDER = "submissions"   # Folder to scan
TOTAL_QUESTIONS    = 10              # Number of questions in the lab
MIN_ANSWER_LENGTH  = 3               # Min characters to count as "answered"
```

The grading rubric (in the `grade()` function) can also be adjusted — e.g., to change the completeness threshold from 8/10.

---

## Sample Submissions

The `submissions/` folder includes two sample files to test the script:

- `sample_complete.txt` — 10 answered questions → **1 point**
- `sample_incomplete.txt` — 3 answered questions → **0 points**

---

## License

MIT — free to use, modify, and share.
