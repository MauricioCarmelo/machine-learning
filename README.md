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

**How to use KNN() within a program***
```python
point = [0.3, 0.7]
kTests = [1, 3, 5, 7] # different tests with different K numbers
results = KNN('input.csv', point, kTests)
print results
```