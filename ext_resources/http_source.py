from ext_sources.resource import DagResource


class HttpSource(DagResource):
    def __init__(self) -> None:
        super().__init__()

    def load() -> str:
        NotImplemented
    
    def validate() -> str:
        NotImplemented
