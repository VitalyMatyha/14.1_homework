class CreationLogMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__(*args, **kwargs)

    def __repr__(self):
        params = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({params})"
