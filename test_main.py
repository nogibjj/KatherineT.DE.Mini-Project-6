"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout

def test_delete_record():
    """tests delete_record"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM birthDB WHERE year = 2000",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_read_data()
    test_delete_record()
    test_general_query()
