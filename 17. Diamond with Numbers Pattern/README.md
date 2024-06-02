# ⭐ Python Diamond with Numbers Pattern Function Demonstration ⭐

Welcome to the Python Diamond with Numbers Pattern Function Demonstration! This script showcases a function that prints a diamond pattern of numbers based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and formatted output.

## Script Overview 📘

The script includes a function called `diamond_with_numbers_pattern` which takes an integer `n` and prints a diamond pattern with `n` rows. The script demonstrates how to use nested loops to generate and format the output for both the upper and lower parts of the diamond.

### :computer: Script Code

```python
def diamond_with_numbers_pattern(n):
    # Upper part
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
    # Lower part
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

def main():
    n = int(input("Please give me a integer: "))
    diamond_with_numbers_pattern(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Looping Constructs**: Learn how to use nested loops to create complex patterns and shapes.
- **String Formatting**: Understand how to format strings to align characters and create visually appealing output.
- **Conditional Logic**: Discover how to implement conditional checks within loops to handle different scenarios effectively.

# Console Output Example 📋
When you run the script and input 7, the console output will be:

```python
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321
 12345654321
  123454321
   1234321
    12321
     121
      1
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `diamond_with_numbers_pattern.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `diamond_with_numbers_pattern.py`.
5. Run the script with: `python diamond_with_numbers_pattern.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates a diamond pattern with the specified number of rows. This will help you understand the practical applications of nested loops and formatted string output in Python programming.

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