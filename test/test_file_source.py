import pytest
from ext_resources.file_source import (
    FileSource, 
    ErrorFileResourceExecption, 
    InvalidFileResourceException
)

def test_validate_extesion_true(monkeypatch):
    monkeypatch.setenv('DAG_FILE_RESOURCE_EXTESIONS', ".sql,.txt,.html")

    file_resource = FileSource(
        path="a.jav"
    )

    file_resource.validate() == False

def test_validate_extension_false(monkeypatch):
    monkeypatch.setenv('DAG_FILE_RESOURCE_EXTESIONS', ".sql,.txt,.html,.jav")

    file_resource = FileSource(
        path="a.jav"
    )
    assert file_resource.validate() == True

def test_load_file_resource(monkeypatch):
    monkeypatch.setenv('DAG_FILE_RESOURCE_EXTESIONS', ".sql,.txt,.html")
    monkeypatch.setenv('DAG_FILE_RESOURCE_PATH', "test")

    content = FileSource(
        path="example/abc.sql"
    ).load()
    assert content == "ABC"

@pytest.mark.xfail(raises=InvalidFileResourceException)
def test_invalid_file_resource(monkeypatch):
    monkeypatch.setenv('DAG_FILE_RESOURCE_EXTESIONS', ".sql,.txt,.html")
    monkeypatch.setenv('DAG_FILE_RESOURCE_PATH', "test")

    file_resource = FileSource(
        path="a.jav"
    )
    file_resource.load()

@pytest.mark.xfail(raises=ErrorFileResourceExecption)
def test_load_file_resource_false(monkeypatch):
    monkeypatch.setenv('DAG_FILE_RESOURCE_EXTESIONS', ".sql,.txt,.html")
    monkeypatch.setenv('DAG_FILE_RESOURCE_PATH', "test")

    content = FileSource(
        path="example/not_found.sql"
    )
    content.load()


    
