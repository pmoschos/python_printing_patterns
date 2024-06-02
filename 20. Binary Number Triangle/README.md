# ⭐ Python Binary Number Triangle Function Demonstration ⭐

Welcome to the Python Binary Number Triangle Function Demonstration! This script showcases a function that prints a binary number triangle based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and number patterns.

## Script Overview 📘

The script includes a function called `binary_number_triangle` which takes an integer `n` and prints a binary number triangle with `n` rows. The script demonstrates how to use nested loops to generate and format the output, alternating between 0 and 1.

### :computer: Script Code

```python
def binary_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j % 2, end=" ")
        print()

def main():
    n = int(input("Please give me a integer: "))
    binary_number_triangle(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Looping Constructs**: Learn how to use nested loops to create complex patterns and shapes.
- **Number Patterns**: Understand how to generate and print binary number sequences in a structured pattern.
- **String Formatting**: Learn how to format strings to align characters and create visually appealing output.

# Console Output Example 📋
When you run the script and input 7, the console output will be:

```python
1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
1 0 1 0 1 0 
1 0 1 0 1 0 1 
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `binary_number_triangle.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `binary_number_triangle.py`.
5. Run the script with: `python binary_number_triangle.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates a binary number triangle with the specified number of rows. This will help you understand the practical applications of nested loops, formatted string output, and number patterns in Python programming.

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