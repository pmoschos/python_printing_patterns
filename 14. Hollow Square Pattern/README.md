# ⭐ Python Hollow Square Pattern Function Demonstration ⭐

Welcome to the Python Hollow Square Pattern Function Demonstration! This script showcases a function that prints a hollow square pattern of stars based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and formatted output.

## Script Overview 📘

The script includes a function called `hollow_square_pattern` which takes an integer `n` and prints a hollow square pattern with `n` rows. The script demonstrates how to use nested loops to generate and format the output.

### :computer: Script Code

```python
def hollow_square_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    n = int(input("Please give me a integer: "))
    hollow_square_pattern(n)

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
*******
*     *
*     *
*     *
*     *
*     *
*******
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `hollow_square_pattern.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `hollow_square_pattern.py`.
5. Run the script with: `python hollow_square_pattern.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates a hollow square pattern with the specified number of rows. This will help you understand the practical applications of nested loops and formatted string output in Python programming.

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