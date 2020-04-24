#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = form.getlist('operand')
try:
    listnums = [int(_) for _ in listval]
    result = sum(listnums)
    body = f"The sum is {result}!"
except (ValueError, TypeError):
    body = "Please provide integer operands!"

print("Content-type: text/plain")
print()
print(body)
