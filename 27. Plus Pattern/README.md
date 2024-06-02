# ⭐ Python Plus Pattern Function Demonstration ⭐

Welcome to the Python Plus Pattern Function Demonstration! This script showcases a function that prints a plus pattern based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional statements, and pattern printing.

## Script Overview 📘

The script includes a function called `plus_pattern` which takes an integer `n` as an argument and prints a plus pattern with `n` rows. This demonstrates the usage of nested loops and conditional statements to create interesting patterns.

### :computer: Script Code

```python
def plus_pattern(n):
    """
    Print a plus pattern with n rows.

    Parameters:
    n (int): The number of rows in the plus pattern.
    """
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():
    n = int(input("Please give me an integer: "))
    plus_pattern(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Nested Loops**: Learn how to use nested loops to create complex patterns, a fundamental concept in programming.
- **Conditional Statements**: Understand how to use conditional statements to print characters based on specific conditions.
- **Input Handling**: See how to handle user input to dynamically adjust the output of a function.

# Console Output Example 📋
When you run the script and input 7, the console output will be:

```python
   *   
   *   
   *   
*******
   *   
   *   
   *  
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `plus_pattern_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `plus_pattern_demo.py`.
5. Run the script with: `python plus_pattern_demo.py`.

# Usage Example 📋
Execute the script and enter an integer when prompted to see the plus pattern.

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
