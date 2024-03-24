#!/usr/bin/python3
"""
Custom script that tests all .py files in the current directory
for pycodestyle compliance
"""


import os
import pycodestyle


def test_pycodestyle(directory="."):
    """List all .py file in current directory """
    python_files = [file for file in os.listdir(directory)
                    if file.endswith(".py")]
    style_guide = pycodestyle.StyleGuide()
    report = style_guide.check_files(python_files)

    if report.total_errors == 0:
        print("All Python files comply with pycodestyle")
    else:
        print("There are {} errors found".format(report.total_errors))
        for file_path, error in report._file_errors.items():
            print("File: {}".format(file_path))
            for code, line_number, _ in error:
                print("  Line {}: {}".format(line_number, code))


if __name__ == "__main__":
    test_pycodestyle()
