# Don’t Panic!

## Problem to Solve

You’re a trained “pentester.” After your success in an earlier operation, a new company has hired you to perform a penetration test and report the vulnerabilities in their data system. This time, you suspect you can do better by writing a program in Python that automates your hack.

To succeed in this covert operation, you’ll need to…

- Connect, via Python, to a SQLite database.
- Alter, within your Python program, the administrator’s password.
If you don’t have experience with Python, not to worry! This problem will walk you through each step along the way.

## Specification
In hack.py, write a Python program to achieve the following:

- Connect, via Python, to a SQLite database.
- Alter, within your Python program, the administrator’s password.
When your program in hack.py is run on a new instance of the database, it should produce the above results.

Clock’s ticking!

## Walkthrough

### Python

When you download the distribution code for this problem, you should notice a file named `hack.py`. You can tell this program is a Python program because it ends with `.py`. The `.py` extension identifies files as Python files much like how the `.sql` extension identifies files as a set of SQL statements.

At first, `hack.py` should only include a single line of Python code:

```python
print("Hacked!")
```

To run this Python program, ensure that—when you type `ls`—you see `hack.py` among the files in your current directory. Then, execute the below in your terminal:

```bash
python hack.py
```

You should see “Hacked!” in your terminal window. Not quite a hack, but you’re on your way!

### Connecting to a Database

Now that you’re able to run your Python program, the next step is to connect your program to `dont-panic.db`. To do so, you’ll need to make use of CS50’s library for Python. A library is a collection of code that someone else has written to solve a problem (and, importantly, which you can use in your own program!). In this case, one of the problems the CS50 library for Python helps you solve is the process of connecting to a SQLite database.

To use the CS50 library’s SQL functionality in your own program, replace `print("Hacked!")` with the below:

```python
from cs50 import SQL
```

This line of Python code says that your program should grab (“import”) tools related to SQL from the CS50 library, called `cs50`.

With this library now included in your program, establishing a connection to `dont-panic.db` is as simple as one line of Python code:

```python
from cs50 import SQL

db = SQL("sqlite:///dont-panic.db")
```

### Executing SQL Statements with Python

The CS50 library for Python’s SQL functionality comes with a method called `execute`. A method receives an input and produces an output. For instance, a method might take a SQL statement as input, execute that SQL statement on a database, and return to you the results of the SQL statement. In fact, that’s exactly what the `execute` method does!

```python
from cs50 import SQL

db = SQL("sqlite:///dont-panic.db")
db.execute(
    """
    UPDATE "users"
    SET "password" = 'hacked!'
    WHERE "username" = 'admin';       
    """
)
```

### Prepared Statements

Imagine you wanted a user to determine the new administrative password as your Python program runs.

Recall from lecture that a prepared statement is a SQL query with placeholders for values that are inserted (“interpolated”) later. Using a prepared statement, then, can help!

The CS50 library for Python supports using prepared statements. First, modify your program to take input from the user:

```python
from cs50 import SQL

db = SQL("sqlite:///dont-panic.db")
password = input("Enter a password: ")
db.execute(
    """
    UPDATE "users"
    SET "password" = ?
    WHERE "username" = 'admin';       
    """,
    password
)
```

Now, try running your program and viewing the changes in `dont-panic.db`!
