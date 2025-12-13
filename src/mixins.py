class CreationLogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self.__class__.__name__} created with {self!r}")
