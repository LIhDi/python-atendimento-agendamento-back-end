from schema import Schema, SchemaError


class SchemaValidator(Schema):

    def __init__(self, *args, **kwargs):
        self._exception = kwargs.pop("exception", None)
        self._category = kwargs.pop("category", None)
        self._location = kwargs.pop("location", None)
        super(SchemaValidator, self).__init__(*args, **kwargs)

    def validate(self, data):
        try:
            return super().validate(data)
        except SchemaError as ex:
            if self._exception:
                raise self._exception(message=ex.args[0], category=self._category)
            else:
                raise ex
