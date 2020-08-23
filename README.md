# Automatic Python StackOverflow

A python script that runs a python command and if it throws any runtime error,  we catch that error and then using Selenium webdriver, it automatically searches for that error on Google and opens the Stackoverflow link explaining the solution to that.  So the error can be directly resolved on the terminal itself without looking for it and finding a solution online manually.

## Steps:

1) Execute python command inside try block and catch any runtime exceptions.

2) Then use chromedriver which is a webdriver tool for automation. It automatically opens a Google Chrome tab.

3) It automatically looks for a stackoverflow link for the runtime exception thrown, opens it and also copies the answer directly on the terminal.

All above steps are automated using selenium webdriver

## Execution Instructions:

1) Download chromedriver from here: https://chromedriver.chromium.org/downloads

2) Specify path of chromedriver in driver variable(Line 11)

3) Keep the python command to execute in try block

4) Now execute python script

```
python3 stackoverflow.py
```

## Demo:

[![DEMO](https://img.youtube.com/vi/2K_ZAArRXjM/0.jpg)](https://youtu.be/2K_ZAArRXjM)

