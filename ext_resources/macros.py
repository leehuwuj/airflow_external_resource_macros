from os import path
from airflow.plugins_manager import AirflowPlugin

from ext_sources.file_source import FileResource


def from_file(path: str):
    resource = FileResource(
        path=path
    )
    resource.load()

class ExternalResource(AirflowPlugin):
    name = "ext_resources"
    macros = [from_file]
