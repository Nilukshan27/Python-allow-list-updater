# Python-allow-list-updater
A python project demonstrating file handling and allow-list updates through a guided coursework inspired implementation. 
Python Allow-List Updater

A Python project demonstrating file handling, list processing, and allow-list updates through a coursework-inspired implementation.

Project Overview

This project reads an allow-list from a text file, identifies entries that should be removed using a separate removal list, and writes the updated entries to an output file.

It demonstrates fundamental Python programming concepts relevant to cybersecurity workflows.

Files

- "allow_list_updater.py" — Main Python script.
- "allow_list.txt" — Sample input containing the original allowed entries.
- "remove_list.txt" — Entries that should be removed.
- "README.md" — Project documentation.

Technologies

- Python
- File handling with "pathlib"
- Lists, sets, and iteration
- Command-line arguments

Example

Original allow-list:

192.0.2.10
192.0.2.11
192.0.2.12
192.0.2.13

Removal list:

192.0.2.11
192.0.2.13

Expected updated list:

192.0.2.10
192.0.2.12

Learning Objectives

- Read and process text files in Python.
- Filter list entries using a separate removal list.
- Write updated data to an output file.
- Understand how simple automation can support access-list maintenance.

Project Status

The source code and sample files have been added to this repository. The expected output above is based on the program's logic; execution and testing still need to be verified.

This is an independent portfolio implementation inspired by a Google Cybersecurity coursework activity. It is not represented as the original graded submission.

The sample IP addresses are reserved for documentation and are not intended for real network access control.
