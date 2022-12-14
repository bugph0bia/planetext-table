# planetext-table

![Software Version](http://img.shields.io/badge/Version-v0.1.0-green.svg?style=flat)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

<!-- [Japanese page](./README.ja.md)   -->

## Overview
planetext table gengerator.

## Example

```py
import datetime as dt
import planetext_table as pt

data = [
    ['file name', 'update date', 'size'],
    ['foo.txt', dt.date(2022, 1, 1), 12000],
    ['bar.txt', dt.date(2022, 2, 3), 500],
    ['ＡＢＣ.txt', dt.date(2022, 11, 12), 2554500],
]
print(pt.to_ascii(data))

# +------------+-------------+---------+
# | file name  | update date | size    |
# +------------+-------------+---------+
# | foo.txt    | 2022-01-01  | 12000   |
# | bar.txt    | 2022-02-03  | 500     |
# | ＡＢＣ.txt | 2022-11-12  | 2554500 |
# +------------+-------------+---------+
```

## Reference
### `to_ascii`
Generate ascii table.

```
+------------+-------------+---------+
| file name  | update date | size    |
+------------+-------------+---------+
| foo.txt    | 2022-01-01  | 12000   |
| bar.txt    | 2022-02-03  | 500     |
| ＡＢＣ.txt | 2022-11-12  | 2554500 |
+------------+-------------+---------+
```

#### arguments
- data (list[list[Any]])
    - input list data
- newline (str)
    - newline character at end of line
    - Default: `'\n'`
- internal_newline (str)
    - newline character at inside element
    - Default: `'\n'`
- aligns (list[Align])
    - text alignment of each column (see below for details)
    - Default: `None`
- converters (list[tuple[Union[Type, tuple[Type]], Callable[[Any], str]]])
    - list of type and converter pairs (see below for details)
    - Default: `None`

### `to_csv`
Generate CSV table.

```
"file name","update date","size"
"foo.txt","2022-01-01","12000"
"bar.txt","2022-02-03","500"
"ＡＢＣ.txt","2022-11-12","2554500"
```

#### arguments
- data (list[list[Any]])
    - input list data
- delimiter (str):
    - delimiter between elements
    - Default: `','`
- quotechar (str):
    - quote character at both ends of element
    - Default: `'"'`
- newline (str)
    - newline character at end of line
    - Default: `'\n'`
- internal_newline (str)
    - newline character at inside element
    - Default: `'\n'`
- converters (list[tuple[Union[Type, tuple[Type]], Callable[[Any], str]]])
    - list of type and converter pairs (see below for details)
    - Default: `None`

### `to_markdown`
Generate markdown table.

```
| file name  | update date | size    |
|------------|-------------|---------|
| foo.txt    | 2022-01-01  | 12000   |
| bar.txt    | 2022-02-03  | 500     |
| ＡＢＣ.txt | 2022-11-12  | 2554500 |
```

#### arguments
- data (list[list[Any]])
    - input list data
- newline (str)
    - newline character at end of line
    - Default: `'\n'`
- internal_newline (str)
    - newline character at inside element
    - Default: `'\n'`
- aligns (list[Align])
    - text alignment of each column (see below for details)
    - Default: `None`
- converters (list[tuple[Union[Type, tuple[Type]], Callable[[Any], str]]])
    - list of type and converter pairs (see below for details)
    - Default: `None`

## Note
### About `aligns` argument
Type: `List[Any]`  

Liner list for specifying the alignment of each column. Inside values should be the `planetext_table.Align` enumeration.  

If `to_ascii`, it affects alignment with space padding.
If `to_markdown`, the alignment is specified according to the markdown notation.

The value of the `planetext_table.Align` is as follows:

- `Align.NONE`
- `Align.LEFT`
- `Align.CENTER`
- `Align.RIGHT`

`NONE` will mean `LEFT`, but the markdown will no longer use `:` on the second line.

### About `converter` argument
Type: `list[tuple[Union[Type, tuple[Type]], Callable[[Any], str]]]`  

By default, built-in function `str` is used to convert the value of each element to a string, but this argument allows any conversion function to be used.

Type information with indent:  
```
list[
    tuple[
        Union[Type, tuple[Type]],  # One or more Type (e.g.: int, bytes, ...)
        Callable[[Any], str]       # Function (Callable object) with one argument and one return value
    ]
]
```

To pass liner list of pairs (tuples) of target element types and conversion functions.
It is possible to specify multiple types by making a tuple of element types. (As used in built-in function `isinstance`)

Example:  

```py
import datetime as dt

def int2str(x):
    return f'{x:,}'

def date2str(x):
    return dt.datetime.strftime(x, r'%Y/%m/%d %H:%M:%S.%f')

converter = [
    (int, int2str),
    ((dt.date, dt.datetime), date2str),
]

data = [[10, dt.date(2022, 1, 2)]]
to_ascii(data, converter=converter)
```

### full-width character handling
The character width of full-width characters is determined according to the character type classified by [East Asian Width](https://www.unicode.org/reports/tr11/tr11-40.html) as follows:

| character type | width |
|----------------|-------|
| Fullwidth (F)  | 2     |
| Halfwidth (H)  | 1     |
| Wide (W)       | 2     |
| Narrow (Na)    | 1     |
| Ambiguous (A)  | 2     |
| Neutral (N)    | 2     |

The function `unicodedata.east_asian_width` from the standard library is used.
Some combinations of characters and fonts, such as some symbols and emojis, may not appear to be aligned nicely.
