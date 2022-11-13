# SamQL

> Sam's querying language.

We are going to try to build a program whose purpose is to act as an interpreter
for a little query language called SamQL. SamQL is inspired by Structured Query
Language (aka SQL); a very popular and mature query language for relational
databases. SamQL has syntax similar for picking a table, limiting columns, and
filtering records like a real query language.

The interpreter we are building will act as the translator of queries to
selected data. Our implementation of SamSQL will represent tables with Comma
Separated Value (aka CSV) files. When data is selected by a query it will be
returned in CSV format as well.

## Language

### Keywords

Keywords are magic words that are reserved by the language to take different
paths of logic. Keywords and semantics are used in SamQL to break up queries
into parsable expressions to execute against our database.

**List of all of the keywords SamQL uses**

- FROM
- READ
- ALL
- WHERE
- GREATER_THAN
- LESS_THAN
- EQUALS
- CONTAINS
- AND

### Ordering

SamQL doesn't support the ability to choose the order of the records selected.
The selected records are expected to be returned in the same natural ordering
as the table file.

### Column Limiting

Tables often store more data then is needed for each row in a query. SamQL like
most querying languages has syntax to hide some of the available columns. In
SamQL you either say in your query that you want all columns or a list of just
the columns you'd like to see.

### Record Filtering

Filters are a tool used by querying languages to allow the author of queries
decide how to cull the records returned from the complete set. SamQL supports
a few basic filters at this time.

**List of built-in filters SamQL supports**

#### GREATER_THAN

> Keeps a record if a column value is greater than a number.

`b GREATER_THAN 127`

#### LESS_THAN

> Keeps a record if a column value is less than a number.

`b LESS_THAN 127`

#### EQUALS

> Keeps a record if the column value is an exact match of another string.

`g EQUALS 255`

#### CONTAINS

> Keeps a record if the column value has another string in it.

`name CONTAINS bl`

## Examples

Check out `colors.csv` to see the entire contents of the colors table. Here are
some examples showing how that table can be reduced down to a smaller set of
records and/or columns.

### Query all columns from all color records

**IN**

```
FROM colors READ ALL
```

**OUT**

```
name,r,g,b
black,0,0,0
red,255,0,0
green,0,255,0
yellow,255,255,0
blue,0,0,255
magenta,255,0,255
cyan,0,255,255
white,255,255,255
```

### Query just the r, g, and b columns from all color records

**IN**

```
FROM colors READ r AND g AND b
```

**OUT**

```
r,g,b
0,0,0
255,0,0
0,255,0
255,255,0
0,0,255
255,0,255
0,255,255
255,255,255
```

### Query all columns from just color records where r is greater than 0

**IN**

```
FROM colors READ ALL WHERE r GREATER_THAN 0
```

**OUT**

```
name,r,g,b
red,255,0,0
yellow,255,255,0
magenta,255,0,255
white,255,255,255
```

**Query just the r, g, and b columns from just color records where name equals red**

**IN**

```
FROM colors READ r AND g AND b WHERE name EQUALS red
```

**OUT**

```
r,g,b
255,0,0
```

## Usage

A script called `samql.py` is the entry point to SamQL. It has a single required
argument which is a query to execute.

`samql.py query`

When a query is executed correctly the selected records will be written to
stdout in CSV format and an exit code of 0 will be set. Otherwise an optional
error hint will be written to stderr and an exit code of 1 will be set.

**How to launch SamQL using the system install of Python**

```sh
python samql.py 'FROM colors READ ALL'
```
