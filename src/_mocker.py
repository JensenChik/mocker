class BasicMocker:
    def __init__(self):
        pass

    def mock(self, data_type, count=1, **kwargs):
        return None


class TableMocker:
    def __init__(self, row_count):
        self.count = row_count
        self.columns = []
        self.headers = []
        self.mocker = BasicMocker()

    def mock_column(self, data_type, name=None, **kwargs):
        self.columns.append(self.mocker.mock(data_type, self.count, kwargs))
        name = name or "col_{}".format(len(self.columns))
        self.headers.append(name)
        return self

    def append_column(self, column, name=None):
        self.columns.append(column)
        name = name or "col_{}".format(len(self.columns))
        self.headers.append(name)
        return self

    def save_as_csv(self, path, header=True):
        pass
