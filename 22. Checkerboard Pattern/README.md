# ⭐ Python Checkerboard Pattern Function Demonstration ⭐

Welcome to the Python Checkerboard Pattern Function Demonstration! This script showcases a function that prints a checkerboard pattern of stars based on a given number of rows and columns. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, conditional logic, and pattern generation.

## Script Overview 📘

The script includes a function called `checkerboard_pattern` which takes an integer `n` and prints a checkerboard pattern with `n` rows and `n` columns. The script demonstrates how to use nested loops to generate and format the output in a checkerboard manner.

### :computer: Script Code

```python
def checkerboard_pattern(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    n = int(input("Please give me a integer: "))
    checkerboard_pattern(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Looping Constructs**: Learn how to use nested loops to create complex patterns and shapes.
- **Conditional Logic**: Understand how to implement conditional checks within loops to handle different scenarios effectively.
- **Pattern Generation**: Learn how to generate and print structured patterns in a checkerboard manner.

# Console Output Example 📋
When you run the script and input 7, the console output will be:

```python
*   *   *   *  
  *   *   *   
*   *   *   *  
  *   *   *   
*   *   *   *  
  *   *   *   
*   *   *   *
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `checkerboard_pattern.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `checkerboard_pattern.py`.
5. Run the script with: `python checkerboard_pattern.py`.

# Usage Example 📋
Execute the script, input an integer value when prompted, and see how the function generates a checkerboard pattern with the specified number of rows and columns. This will help you understand the practical applications of nested loops, formatted string output, and pattern generation in Python programming.

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