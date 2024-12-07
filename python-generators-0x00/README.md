# Python Generators Project - Task 0

## Description

This repository contains Python scripts that demonstrate the use of generators to handle large datasets efficiently. These scripts utilize generators for batch processing, lazy loading of paginated data, memory-efficient aggregation, and more.

## Introduction

This project demonstrates how to use Python generators for efficient data processing. Generators allow for lazy evaluation, meaning data is processed only when needed, without the need to load the entire dataset into memory. This makes the code ideal for handling large datasets that would otherwise overwhelm your system's memory.

## Files

- `seed.py`: Contains functions to connect to MySQL, create the database, create the table, and insert data.
- `user_data.csv`: Sample data to be inserted into the table.
- `seed.py`: Script to execute the functions and verify the database setup.

## Table of Contents

- [Introduction](#introduction)
- [File Structure](#file-structure)
- [Setup](#setup)
- [Usage](#usage)
  - [Task 1: Batch Processing Large Data](#task-1-batch-processing-large-data)
  - [Task 2: Lazy Loading Paginated Data](#task-2-lazy-loading-paginated-data)
  - [Task 3: Memory-Efficient Aggregation with Generators](#task-3-memory-efficient-aggregation-with-generators)

### Key Concepts Covered:
1. **Batch Processing**: Fetching and processing data in smaller batches.
2. **Lazy Loading**: Fetching data lazily in chunks or pages.
3. **Memory-Efficient Aggregation**: Calculating aggregates (like the average) on large datasets without loading them entirely into memory.

## File Structure

```bash
python-generators-0x00/
├── 1-batch_processing.py    # Task 1 - Batch processing of large data
├── 2-lazy_paginate.py       # Task 2 - Lazy pagination using generators
├── 3-stream_ages.py         # Task 3 - Memory-efficient average age calculation
├── seed.py                  # Database connection setup (seed data)
├── README.md                # Project documentation
├── requirements.txt         # Required packages
└── 3-main.py                # Script to run the pagination example

