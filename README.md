- Airflow custom macros to render task content from external sources (file, http,...)
- This plugin help user manage DAG file easier by separate DAG logic file and its resources.

## How to integrate:
Approach 1:
- Copy `ext_resources` into your airflow plugins folder.
- Install packages from `requirements.txt`

Approach 2:
- Build this plugin your own python package.
- Install the packge in your airflow environment


*Please make sure the environment for each resource type (file, http,...) are set.*

## Example:
- Instead of putting long SQL like this:
```python
SnowFakeOperator(
    query="""
    SELECT i, j
    FROM
         table1 AS t1 SAMPLE (25) 
             INNER JOIN
         table2 AS t2 SAMPLE (50)
    WHERE t2.j = t1.i
    ;
    """
)
```

- You can split the query content into dedicate .sql file, let say `a_file.sql`.

- Now you can better using the macros syntax: `macros.ext_resources.from_file` that point to the sql file:
```python
SnowFakeOperator(
    query="{{ macros.ext_resources.from_file('a_file.sql') }}"
)
```
