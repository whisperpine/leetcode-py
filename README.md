# LeetCode Python

An ongoing list of LeetCode problem solutions in Python.

## NeetCode Roadmap

Refer to [NeetCode Roadmap](https://neetcode.io/roadmap).

## Get Started

Solutions for LeetCode problems are written in files under [./tests](./tests/)
respectively. This means that pytest can run test cases for a specific LeetCode
problem. But for comprehensive tests, you should copy the code to LeetCode live
editor and submit. See [LeetCode problem set](https://leetcode.com/problemset/).

There are several ways to run tests:

```sh
# Run all test cases.
pytest
# Run test cases in a given file.
pytest path/to/test_file.py
# Run a specific test case in a given file.
pytest path/to/test_file.py::test_function_name
```

## Table of Problems

### Array & Hash

| Problem | Difficulty | Solution |
| - | - | - |
| 1. Two Sum | Easy | [1_two_sum.py](./tests/1_two_sum.py) |
