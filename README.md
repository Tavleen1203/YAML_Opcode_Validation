# YAML Opcode Validation ✅

## Introduction

I started this project by thoroughly reviewing the documentation related to opcode validation. After understanding the requirements and referring to the example code provided, I devised a simple script using functions to validate opcode definitions. Subsequently, I explored various ways to enhance and implement this code, considering different approaches to structure and handle the validation logic.

## Basic Validation with Functions

Initially, I created a basic validation script using functions to check the opcode definitions. This script ensures no overlapping bit ranges, validates that values are representable within their specified widths, and checks that all arguments used in the instructions have mappings in the provided argument lookup table. (see `eval_1.py`).

## Enhanced Validation Approaches

### 1. Object-Oriented Programming (OOP)

The validation logic was improved using Object-Oriented Programming principles to enhance code clarity and maintainability. Classes for opcodes and validators were created, structuring data and methods more logically. This approach encapsulates related data and behavior, making the code easier to understand and extend (see `eval_2.py`).

### 2. Command Line Interface (CLI)

To increase the script's user-friendliness and versatility, a Command Line Interface (CLI) was implemented. This enhancement allows users to validate different opcode files and specify argument lookup tables through command line arguments. The CLI approach improves the script's accessibility and usability for various use cases without modifying the code (see `eval_3.py`).

### 3. Pandas for Data Manipulation

The Pandas library was utilized for handling opcode data, allowing for more complex manipulation and validation tasks. By converting opcode data into a Pandas DataFrame, sophisticated data analysis and manipulation capabilities were enabled. This approach facilitated efficient handling of large datasets and streamlined the validation process (see `eval_4.py`).

## Summary

Through these different approaches, a robust and flexible validation script for opcode definitions was developed. Each method provides unique advantages, catering to various needs and preferences in coding style and project requirements.
