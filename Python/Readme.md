# 🐍 Python Learning Journal

## 📌 1. `print()` – Built-in Function

The `print()` function is used to display output on the screen.

### 🔹 Syntax:
```python
print(*objects, sep=' ', end='\n')
🔹 Special Characters:
\n – New line
Example:

python
Copy
Edit
print("Hello\nWorld")
# Output:
# Hello
# World
🔹 sep (Separator):
Specifies what goes between items.

python
Copy
Edit
print("2025", "07", "16", sep='-')
# Output: 2025-07-16
🔹 end:
Specifies what appears at the end of the line.

python
Copy
Edit
print("Hello", end=" ")
print("World!")
# Output: Hello World!
Literals:
Integers – without fraction (200,100023,-90,1_000_000)
Octal Number – 0o123
<img width="1313" height="636" alt="Screenshot 2025-07-16 160913" src="https://github.com/user-attachments/assets/86ca0ed7-96aa-475e-98c6-b86d5b336833" />


Operators:
Arithmetic operators -7:
<img width="1263" height="463" alt="Screenshot 2025-07-16 161556" src="https://github.com/user-attachments/assets/f1191a02-f5ed-42af-b0c4-67197350a859" />

Exponentials - ** (2**3)
Modulo – 5%2 =1 (provides reminder after division)
Unary and Binary operators:
 <img width="1259" height="746" alt="Screenshot 2025-07-16 162342" src="https://github.com/user-attachments/assets/60fc32de-4679-4997-89e7-9396ad0fdd2f" />



📌 2. Variables in Python
✅ What is a Variable?
A name used to store a value in memory.

Python is dynamically typed – no need to specify data type.

✅ Examples:
python
Copy
Edit
name = "Alice"       # string
age = 25             # integer
height = 5.6         # float
is_active = True     # boolean
✅ Rules for Naming:
Must begin with a letter or underscore.

Can contain letters, numbers, and underscores.

Cannot start with a number or use Python keywords.

Valid:

python
Copy
Edit
user_name = "John"
age2 = 30
_height = 5.9
Invalid:

python
Copy
Edit
2name = "Anna"     # ❌ starts with number
for = 10           # ❌ keyword
✅ Reassignment:
python
Copy
Edit
x = 10
x = 20  # Now x is 20
✅ Multiple Assignments:
python
Copy
Edit
a, b, c = 1, 2, 3
x = y = z = 100
✅ Type Checking:
python
Copy
Edit
print(type(age))  # <class 'int'>
