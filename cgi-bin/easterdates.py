#!/usr/bin/python3

import datetime
import cgi

# Enable CGI error reporting
cgitb.enable()

# Get form data from user
form = cgi.FieldStorage() 
Format_Date = form.getvalue("datefilter")
year = form.getvalue("year")

# Define function to format date according to user's chosen format
def dates(Format_Date, date):
    if Format_Date == 'numerical':
        return date.strftime('<span class="date-answer-title">%d/%m/%Y </span>')
    elif Format_Date == 'words':
        return date.strftime('<span class="date-answer-title">' + superscript(date.day)+'&nbsp;%B %Y </span>')
    else:
        return date.strftime('<span class="date-answer-title">%d/%m/%Y  </span> <span class="date-answer-title"> or </span> <span class="date-answer-title">' + superscript(date.day)+'&nbsp;%B %Y</span>' )

# Define function to format the day of the month as superscript
def superscript(d):
    if d == 21 or d ==1 or d== 31:
        return str(d) + " <sup>st</sup>"
    elif d == 22 or d ==2:
        return str(d) + "<sup>nd</sup>"
    elif d ==23 or d ==3:
        return str(d) + "<sup>rd</sup>"
    else:
        return str(d) + " <sup>th</sup> "

# Calculate Easter date based on user's chosen year
def Easter(year):
    a = int(year) % 19
    b = int(year) // 100
    c = int(year) % 100
    d = b // 4
    e=b%4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k=c%4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return datetime.datetime(day=p, month=n, year=int(year))

# Output an HTML document with the results of the Easter date calculation
print("Content-Type: text/html; charset=utf-8")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<link rel='stylesheet' type='text/css' href='../style.css'/>")
print("<title>Python Script for Easter</title>")
print("</head>")
print("<body>")
print("<div class='container'>")
print("<div class='title'>Easter Date Calculator</div>")
print("<br/>")
print("<div class='detailss'>The date of easter for year " + year + " is</div>")
print("<div class='content'>")
print("<div class='date-details'>")
print(dates(Format_Date, Easter(year)))
print("</div>")
print("</div>")
print("</div>")
print("</body>")
print("</html>")
