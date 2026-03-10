"""
setup.py — Install dependencies for grade_labs.py
Run this once before using the grading script.
"""

import subprocess
import sys

# pdfplumber — extracts text and tables from PDF submissions
# python-docx — reads Word document (.docx) submissions
# pandas      — builds and exports the grading results CSV

packages = ["pdfplumber", "python-docx", "pandas"]

for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("\nAll dependencies installed. You're ready to run grade_labs.py.")
