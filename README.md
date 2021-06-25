# Project description
It is a testing automation task from Ecwid. Tests cover searchfield functionality and sorting by asc.

## Installation
Make sure you have python 3.8+ installed on your computer as well as ChromeWebdriver corresponding to your Chrome browser version.
```bash
git clone https://github.com/Iaroslavv/ecwid_automation_task.git
pip install -r requirements.txt
```
## Running tests
To run tests with mark 'search_field' type
```bash
pytest -s -v -m search_field test_search_page.py
```
and
```bash
pytest -s -v -m sort_by_asc test_search_page.py
```
for mark 'sort_by_asc'.
