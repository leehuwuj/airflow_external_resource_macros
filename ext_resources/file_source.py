
import os
from airflow.exceptions import AirflowException
from airflow.utils.log.logging_mixin import LoggingMixin
from .resource import DagResource

logger = LoggingMixin().log



class FileSource(DagResource):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path = path

        self.DAG_FILE_RESOURCE_PATH = os.environ.get("DAG_FILE_RESOURCE_PATH")
        if self.DAG_FILE_RESOURCE_PATH is None:
            logger.warning(
                "Environment `DAG_FILE_RESOURCE_PATH` was not set!"
                ".The FileResource will using user defined absolute path!"
            )
        extensions = os.environ.get("DAG_FILE_RESOURCE_EXTESIONS")
        if extensions is None:
            logger.info(
                "Environment `DAG_FILE_RESOURCE_EXTESIONS` was not set!"
                ". Airflow will skip validate file extension"
            )
        else:
            self.DAG_FILE_RESOURCE_EXTESIONS = tuple(extensions.split(","))

    def validate(self) -> bool:
        if self.DAG_FILE_RESOURCE_EXTESIONS is not None:
            if self.path.endswith(self.DAG_FILE_RESOURCE_EXTESIONS):
                return True
            else:
                return False
        else:
            return True
    
    def load(self):
        if self.validate():
            if self.DAG_FILE_RESOURCE_PATH is not None:
                resource_path = os.path.join(
                    self.DAG_FILE_RESOURCE_PATH,
                    self.path
                )
            else:
                resource_path = self.path
            try:
                with open(resource_path, 'r') as f:
                    return f.read()
            except Exception as e:
                raise ErrorFileResourceExecption(
                    f"Can not read file resource!"
                    f"{e}"
                )
        else:
            raise InvalidFileResourceException()
        
        
class InvalidFileResourceException(AirflowException):
    "Your resource file is invalid!"

class ErrorFileResourceExecption(AirflowException):
    ""
