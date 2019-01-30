

# Usage
## Quick start

## Mocker
### BasicMocker
### TableMocker


## Data Type
### basic
#### boolean
Generate `count` boolean value randomly

##### input

* count - int, optional, default 1

* true_ratio - float,  range 0 to 1,  optional, default 0.5

##### output
* data - array

##### example
```python

```
    
#### char 
Choose `count` character from `selection` randomly

##### input:
* count - int, optional, default 1
* selection - array, optional, default \['a' ~ 'z', 'A' ~ 'Z' \]

##### output
    data - array
    
#### float 
Generate `count` float value between `min` and `max` randomly
##### input
* count - int, optional, default 1
* min - number, optional, default 0
* max - number, optional, default 1

##### output
* data - array 
    
##### example 
```pyton

```

#### int 
Generate `count` integer value between `min` and `max` randomly
##### input
* count - int, optional, default 1
* min - number, optional, default 0
* max - number, optional, default 10

##### output
* data - array 
    
##### example 
```pyton

```

#### string 
choose `count` string from `selection` or generate `count`
string with `fix_len` or `max_len` using `charset`
##### input
* count - int, optional, default 1
* selection - array of string
* max_len - int or array of int, 
* fixed_len - int or array of int,
* charset - array, optional, default \['a' ~ 'z', 'A' ~ 'Z' \]

##### output
* data - array of string
    
##### example 
```pyton

```

