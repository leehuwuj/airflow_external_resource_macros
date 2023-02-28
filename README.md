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
```python
SnowFakeOperator(
    query="{{ macros.ext_resources.from_file('sql/a_ddl_file.sql') }}"
)
```
