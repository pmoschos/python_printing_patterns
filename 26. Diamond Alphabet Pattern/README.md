# ⭐ Python Alphabet Diamond Function Demonstration ⭐

Welcome to the Python Alphabet Diamond Function Demonstration! This script showcases a function that prints an alphabet diamond pattern based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, ASCII values, and pattern printing.

## Script Overview 📘

The script includes a function called `diamond_alphabet_pattern` which takes an integer `n` as an argument and prints a diamond of alphabets with `n` rows. This demonstrates the usage of nested loops and ASCII value manipulation to create interesting patterns.

### :computer: Script Code

```python
def diamond_alphabet_pattern(n):
    """
    Print an alphabet diamond pattern with n rows.

    Parameters:
    n (int): The number of rows in the diamond's half (excluding the middle row).
    """
    alphabet = 65
    # Upper part
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print(chr(alphabet + j), end="")
        print()
    # Lower part
    for i in range(n - 2, -1, -1):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print(chr(alphabet + j), end="")
        print()

def main():
    n = int(input("Please give me an integer: "))
    diamond_alphabet_pattern(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Nested Loops**: Learn how to use nested loops to create complex patterns, a fundamental concept in programming.
- **ASCII Value Manipulation**: Understand how to work with ASCII values to print alphabet characters in sequence.
- **Input Handling**: See how to handle user input to dynamically adjust the output of a function.

# Console Output Example 📋
When you run the script and input 5, the console output will be:

```python
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
 ABCDEFG
  ABCDE
   ABC
    A
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `alphabet_diamond_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `alphabet_diamond_demo.py`.
5. Run the script with: `python alphabet_diamond_demo.py`.

# Usage Example 📋
Execute the script and enter an integer when prompted to see the alphabet diamond pattern.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
