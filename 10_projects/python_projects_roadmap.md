# Python Project Roadmap for Data-Focused Coding Growth

## Overview

This roadmap is designed for a Python learner who works a lot with structured and semi-structured data such as JSON, YAML, CBOR, Base64, and binary/text transformations. The goal is not only to improve Python syntax, but also to strengthen algorithmic thinking, debugging ability, code organization, and engineering judgment.

These 10 projects are arranged in a progression from Python fundamentals to real-world data pipeline thinking.

---

## Learning Goals

By working through these projects, you will improve in:

- Python basics: variables, loops, conditions, functions
- Data structures: list, tuple, set, dictionary
- File handling
- Error handling
- Parsing and validation
- Transforming nested data
- Designing clean, modular code
- Thinking in steps like an engineer

---

## Recommended Learning Approach

For each project:

1. Understand the input and output clearly
2. Write the logic in plain English first
3. Break the solution into small functions
4. Test with small examples
5. Add edge cases after the basic version works

---

# Project 1 — Data Inspector CLI

## Goal
Build a small Python tool that inspects a piece of data and reports:

- its type
- its length if applicable
- nested keys or structure
- unique item count for lists

## Why it matters
This builds your foundation for understanding unknown Python objects and data structures.

## Core concepts
- variables
- `if/elif/else`
- loops
- lists
- sets
- dictionaries
- functions
- type checking

## Example input
```python
data = {
    "device": "sensor-1",
    "values": [23, 25, 23, 21],
    "active": True
}
```

## Example output
```text
Type: dict
Keys: 3
Contains:
- device: str
- values: list (length 4)
- active: bool
Unique values in 'values': 3
```

## Thinking skill gained
You learn how to inspect data instead of assuming what it looks like.

---

# Project 2 — JSON Cleaner and Formatter

## Goal
Read messy JSON and convert it into clean, readable, validated JSON.

## Features
- load JSON from file
- pretty-print it
- sort keys
- remove empty fields
- rename keys
- validate required fields

## Why it matters
JSON is one of the most common formats in backend and data-heavy Python work.

## Core concepts
- file reading
- dictionaries
- nested structures
- conditions
- loops
- `json` module
- normalization logic

## Extra challenge
Add rules such as:
- remove keys with `None`
- remove empty strings
- convert `"true"` to `True`
- convert numeric strings like `"42"` to `42`

## Thinking skill gained
You learn that parsing data is only the first step; cleaning and normalizing are just as important.

---

# Project 3 — YAML Config Loader

## Goal
Create a Python tool that loads a YAML config file and validates it before use.

## Features
- load YAML config
- verify required sections
- validate expected types
- use defaults for optional values
- print helpful error messages

## Example YAML
```yaml
app:
  name: parser-service
  version: 1.0

database:
  host: localhost
  port: 5432
  enabled: true
```

## Why it matters
Real systems often depend on configuration files. Good config handling prevents fragile applications.

## Core concepts
- YAML parsing
- nested dictionaries
- validation
- optional values
- defaults
- defensive coding

## Thinking skill gained
You learn to separate raw config from validated runtime values.

---

# Project 4 — Base64 Encoder/Decoder Toolkit

## Goal
Build a small utility tool that can:

- encode text into Base64
- decode Base64 back to text
- decode Base64 into raw bytes
- save decoded bytes to file
- detect invalid Base64 input

## Why it matters
This is directly useful in data pipelines, telemetry, and encoded message processing.

## Core concepts
- strings vs bytes
- encoding and decoding
- `try/except`
- modular functions
- file writing

## Suggested functions
- `encode_text_to_base64(text)`
- `decode_base64_to_text(encoded)`
- `decode_base64_to_bytes(encoded)`
- `save_bytes_to_file(data, path)`

## Thinking skill gained
You begin understanding that the same data can exist in multiple representations: text, bytes, hex, Base64, or structured objects.

---

# Project 5 — Nested Data Path Extractor

## Goal
Write a utility that extracts values from deeply nested data structures using paths such as:

```text
payload.sensor.values[1].temp
```

## Example data
```python
data = {
    "payload": {
        "sensor": {
            "values": [
                {"temp": 24.5},
                {"temp": 25.1}
            ]
        }
    }
}
```

## Output
```text
25.1
```

## Why it matters
Nested traversal is one of the most important skills when dealing with JSON-like data.

## Core concepts
- loops
- string parsing
- dictionaries
- lists
- indexes
- error handling
- step-by-step traversal

## Thinking skill gained
You learn how to move through complex nested structures safely and methodically.

---

# Project 6 — CBOR Payload Playground

## Goal
Build a Python program that:

- accepts a hex or Base64 payload
- converts it to bytes
- parses CBOR
- prints a readable structure
- extracts selected fields

## Why it matters
This is highly aligned with real-world data engineering and IoT payload handling.

## Core concepts
- bytes
- Base64 decoding
- hex conversion
- third-party library usage
- nested data interpretation
- formatting parsed output

## Suggested phases
1. Parse only known valid CBOR
2. Handle malformed payloads
3. Add extraction rules
4. Convert output into clean JSON

## Thinking skill gained
You learn pipeline thinking:

raw input → decode → parse → validate → transform → output

---

# Project 7 — Rule-Based Data Transformer

## Goal
Create a transformation engine that changes input data into output data using rules.

## Example input
```python
{
    "deviceId": "abc123",
    "temp_c": 22.4,
    "humidity": 54
}
```

## Example rules
- rename `deviceId` to `device_id`
- convert `temp_c` to Fahrenheit
- add `status = "ok"` if humidity is less than 70

## Example output
```python
{
    "device_id": "abc123",
    "temp_f": 72.32,
    "humidity": 54,
    "status": "ok"
}
```

## Why it matters
This project is excellent for moving from hardcoded scripts to general-purpose logic.

## Core concepts
- transformation pipelines
- dictionaries
- functions
- conditionals
- reusable logic
- modular design

## Thinking skill gained
You start designing flexible systems instead of one-off scripts.

---

# Project 8 — Log and Event Analyzer

## Goal
Build a tool that reads logs or event records and summarizes them.

## Features
- count events by type
- group records by device
- find repeated errors
- show simple time-based summaries
- export summary as JSON

## Example input
```json
[
  {"device": "a1", "event": "BOOT", "time": "2026-04-21T10:00:00"},
  {"device": "a1", "event": "ERROR", "time": "2026-04-21T10:05:00"},
  {"device": "b2", "event": "BOOT", "time": "2026-04-21T10:07:00"}
]
```

## Why it matters
This is a very practical project for understanding patterns in operational data.

## Core concepts
- counting
- grouping
- sorting
- file reading
- dictionaries
- summaries

## Thinking skill gained
You learn how code can be used to extract meaning from records, not just store them.

---

# Project 9 — Schema Validator

## Goal
Create a mini validation system for Python dictionaries.

## Example schema
```python
schema = {
    "device_id": str,
    "temperature": float,
    "active": bool
}
```

## Program behavior
- check required keys
- validate types
- print helpful error messages
- optionally support nested schemas

## Why it matters
Validation is central to building robust systems.

## Core concepts
- dictionaries
- loops
- functions
- type checking
- recursion for nested schemas
- explicit assumptions

## Thinking skill gained
You become more precise about what valid data means and how to guard your program.

---

# Project 10 — Full Data Pipeline Project

## Goal
Build a complete Python application that combines everything:

- reads input from file or string
- detects format
- decodes Base64 if needed
- parses CBOR if needed
- validates data
- transforms it
- writes final JSON output
- logs errors clearly

## Example pipeline
1. read input
2. detect format
3. extract payload
4. decode Base64
5. parse CBOR
6. validate fields
7. transform values
8. save output JSON
9. write error logs if needed

## Why it matters
This is your capstone project and mirrors the shape of real backend/data-processing systems.

## Core concepts
- modular design
- multiple parsing stages
- validation
- transformation
- file output
- error logging

## Thinking skill gained
You learn small-scale system design and how different parts of an application should work together.

---

# Python Fundamentals Covered Across the Projects

## Core syntax
- variables
- strings
- integers
- floats
- booleans
- operators
- comments

## Control flow
- `if`, `elif`, `else`
- `for`
- `while`
- `break`
- `continue`

## Collections
- list
- tuple
- set
- dictionary

## Functions
- parameters
- return values
- helper functions
- reusable logic

## File handling
- reading files
- writing files
- JSON files
- YAML files
- binary data

## Error handling
- `try/except`
- invalid input handling
- missing keys
- bad types

---

# Suggested Weekly Plan

## Weeks 1–2
- Project 1
- Project 2

Focus:
- variables
- loops
- conditions
- dicts
- lists
- JSON basics

## Weeks 3–4
- Project 3
- Project 4

Focus:
- YAML
- file handling
- Base64
- strings vs bytes
- error handling

## Weeks 5–6
- Project 5
- Project 6

Focus:
- nested traversal
- parsing logic
- CBOR
- debugging structured data

## Weeks 7–8
- Project 7
- Project 8

Focus:
- transformations
- grouping
- aggregation
- cleaner code organization

## Weeks 9–10
- Project 9
- Project 10

Focus:
- schema validation
- modular design
- full data pipeline thinking

---

# General Coding Rules for Every Project

1. Do not write one giant script.
2. Break the program into small functions.
3. Use meaningful variable names.
4. Print intermediate values while learning.
5. Start with a very small example first.
6. Add edge cases only after the basic version works.
7. Think in steps before coding.

---

# Suggested Project Template

```python
def read_input(path):
    pass

def parse_input(raw_data):
    pass

def validate_data(data):
    pass

def transform_data(data):
    pass

def save_output(data, output_path):
    pass

def main():
    raw_data = read_input("input.json")
    parsed_data = parse_input(raw_data)
    validated_data = validate_data(parsed_data)
    final_data = transform_data(validated_data)
    save_output(final_data, "output.json")

if __name__ == "__main__":
    main()
```

---

# Final Note

If you complete these 10 projects properly, you will not just improve your Python syntax. You will grow in:

- coding confidence
- debugging skill
- structured thinking
- data handling ability
- backend/data engineering mindset
- system design thinking at a small scale

The real target is to become someone who can take messy data, understand it, transform it, and build clean solutions around it.
