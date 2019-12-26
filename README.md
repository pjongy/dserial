# DSerial

## 0. Introduction
DSerial is dictionary serializer with type checking methodology by declared type hinting

## 1. Requirements
python 3.7 +

## 2. Quick start

### 2.1. Default type
```json
{
  "int_variable": 1234,
  "string_variable": "string_value"
}
```
For serialize above dictionary, data class can be below code
```python
class DefaultData(TypeCheckingDictSerializer):
    int_variable: int
    string_variable: str
```
and usage:
```python
>>> dictionary = {
  'int_variable': 1234,
  'string_variable': 'string_value'
}
>>> data = DefaultData(dictionary)
>>> data.int_variable
1234
>>> data.string_variable
string_value
```

### 2.2. Nested type
```json
{
  "int_variable": 1234,
  "string_variable": "string_value",
  "nested": {
    "int_variable": 4321
  }
}
```
For serialize above dictionary, data class can be below code
```python
class NestedData(TypeCheckingDictSerializer):
    int_variable: int

class DefaultData(TypeCheckingDictSerializer):
    int_variable: int
    string_variable: str
    nested: NestedData
```
and usage:
```python
>>> dictionary = {
    'int_variable': 1234,
    'string_variable': 'string_value',
    'nested': {
        'int_variable': 4321
    }
}
>>> data = DefaultData(dictionary)
>>> data.int_variable
1234
>>> data.string_variable
string_value
>>> data.nested.int_variable
4321
```

### 2.3. Repeated type
```json
{
  "int_variable": 1234,
  "string_variable": "string_value",
  "nested": {
    "int_variable": 4321
  },
  "repeated": [1, 2, 3]
}
```
For serialize above dictionary, data class can be below code
```python
class RepeatedData(TypeAnnotatedList):
    @staticmethod
    def get_type():
        return int

class NestedData(TypeCheckingDictSerializer):
    int_variable: int

class DefaultData(TypeCheckingDictSerializer):
    int_variable: int
    string_variable: str
    nested: NestedData
    repeated: RepeatedData
```
and usage:
```python
>>> dictionary = {
    'int_variable': 1234,
    'string_variable': 'string_value',
    'nested': {
        'int_variable': 4321
    },
    'repeated': [1, 2, 3]
}
>>> data = DefaultData(dictionary)
>>> data.int_variable
1234
>>> data.string_variable
string_value
>>> data.nested.int_variable
4321
>>> len(data.repeated)
3
>>> data.repeated[0]
1
```

### 2.4. More complex
```json
{
  "int_variable": 1234,
  "string_variable": "string_value",
  "repeated_nested": [{
    "int_variable": 3133
  }, {
    "int_variable": 1337
  }]
}
```
For serialize above dictionary, data class can be below code
```python
class NestedData(TypeCheckingDictSerializer):
    int_variable: int

class RepeatedData(TypeAnnotatedList):
    @staticmethod
    def get_type():
        return NestedData

class DefaultData(TypeCheckingDictSerializer):
    int_variable: int
    string_variable: str
    repeated_nested: RepeatedData
```
and usage:
```python
>>> dictionary = {
    'int_variable': 1234,
    'string_variable': 'string_value',
    'repeated_nested': [{
        'int_variable': 3133
    }, {
        'int_variable': 1337
    }]
}
>>> data = DefaultData(dictionary)
>>> data.int_variable
1234
>>> data.string_variable
string_value
>>> len(data.repeated_nested)
3
>>> data.repeated[0].int_variable
3133
```


## 3. Test
```shell script
> dserial$ python3 -m tests
```