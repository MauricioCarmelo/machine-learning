# toolkit.py
Toolkit of useful functions to be used in everyday programs

## Usage

**How to use loadCSV() within a program**

```python
  sheet, attributes, instances = loadCSV('input.csv')

  print 'Loaded sheet within a dictionary:'
  for key in sheet.keys():
    print sheet[key]
```
