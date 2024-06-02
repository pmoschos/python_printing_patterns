# ⭐ Python Spiral Pattern Function Demonstration ⭐

Welcome to the Python Spiral Pattern Function Demonstration! This script showcases a function that prints a spiral pattern based on a given number of rows. It's an excellent resource for anyone learning Python or those teaching programming concepts related to loops, array manipulation, and pattern printing.

## Script Overview 📘

The script includes a function called `spiral_pattern` which takes an integer `n` as an argument and prints a spiral pattern with `n` rows and columns. This demonstrates the usage of nested loops and array manipulation to create interesting patterns.

### :computer: Script Code

```python
def spiral_pattern(n):
    """
    Print a spiral pattern with n rows and columns.

    Parameters:
    n (int): The number of rows and columns in the spiral pattern.
    """
    a = [[0] * n for _ in range(n)]
    val = 1
    k, l = 0, 0
    m, p = n, n
    
    while k < m and l < p:
        for i in range(l, p):
            a[k][i] = val
            val += 1
        k += 1
        for i in range(k, m):
            a[i][p - 1] = val
            val += 1
        p -= 1
        if k < m:
            for i in range(p - 1, l - 1, -1):
                a[m - 1][i] = val
                val += 1
            m -= 1
        if l < p:
            for i in range(m - 1, k - 1, -1):
                a[i][l] = val
                val += 1
            l += 1

    for row in a:
        for num in row:
            print(str(num).rjust(3), end=" ")
        print()

def main():
    n = int(input("Please give me an integer: "))
    spiral_pattern(n)

if __name__ == '__main__':
    main()
```

# Key Features 🌟
- **Nested Loops**: Learn how to use nested loops to create complex patterns, a fundamental concept in programming.
- **Array Manipulation**: Understand how to work with 2D arrays to store and manipulate data.
- **Input Handling**: See how to handle user input to dynamically adjust the output of a function.

# Console Output Example 📋
When you run the script and input 5, the console output will be:

```python
  1   2   3   4   5 
 16  17  18  19   6 
 15  24  25  20   7 
 14  23  22  21   8 
 13  12  11  10   9 
```

# Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

# Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `hollow_diamond_in_rectangle_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `hollow_diamond_in_rectangle_demo.py`.
5. Run the script with: `python hollow_diamond_in_rectangle_demo.py`.

# Usage Example 📋
Execute the script and enter an integer when prompted to see the hollow diamond pattern inside a rectangle.

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