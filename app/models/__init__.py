from enum import Enum

class StatusType(Enum):
    DEFAULT = "dflag updated_at created_at".split()

class UnidadesType(Enum):
    DEFAULT = "dflag updated_at created_at".split()

class AssuntoType(Enum):
    DEFAULT = "dflag updated_at created_at".split()

class PersonsType(Enum):
    DEFAULT = "dflag updated_at created_at".split()

class AppointmentsType(Enum):
    DEFAULT = "dflag updated_at created_at id_person id_subject".split()

class Status:
    def __new__(cls, status_json, remove_keys=StatusType.DEFAULT.value):
        instance = super(Status, cls).__new__(cls)
        instance.__init__(status_json, remove_keys)
        return vars(instance)

    def __init__(self, status_json, remove_keys: list):
        status = dict(status_json)
        self.name = status.get("name")
        self.code = status.get("code")
        self.description = status.get("description")
        self.__remove_unwanted_keys(remove_keys)

    def __remove_unwanted_keys(self, keys):
        [delattr(self, key) for key in keys if hasattr(self, key)]


class Assunto:
    def __new__(cls, assunto_json, remove_keys=AssuntoType.DEFAULT.value):
        instance = super(Assunto, cls).__new__(cls)
        instance.__init__(assunto_json, remove_keys)
        return vars(instance)

    def __init__(self, assunto_json, remove_keys: list):
        assunto = dict(assunto_json)
        self.name = assunto.get("name")
        self.code = assunto.get("code")
        self.description = assunto.get("description")
        self.active = assunto.get("active")
        self.__remove_unwanted_keys(remove_keys)

    def __remove_unwanted_keys(self, keys):
        [delattr(self, key) for key in keys if hasattr(self, key)]


class Unidade:
    def __new__(cls, unidade_json, remove_keys=UnidadesType.DEFAULT.value):
        instance = super(Unidade, cls).__new__(cls)
        instance.__init__(unidade_json, remove_keys)
        return vars(instance)

    def __init__(self, unidade_json, remove_keys: list):
        unidade = dict(unidade_json)
        self.name = unidade.get("name")
        self.code = unidade.get("code")
        self.attendants_number = unidade.get("attendants_number")
        self.description = unidade.get("description")
        self.phone = unidade.get("phone")
        self.email = unidade.get("email")
        self.active = unidade.get("active")
        self.__remove_unwanted_keys(remove_keys)

    def __remove_unwanted_keys(self, keys):
        [delattr(self, key) for key in keys if hasattr(self, key)]


class Person:
    def __new__(cls, person_json, remove_keys=PersonsType.DEFAULT.value):
        instance = super(Person, cls).__new__(cls)
        instance.__init__(person_json, remove_keys)
        return vars(instance)

    def __init__(self, person_json, remove_keys: list):
        person = dict(person_json)
        self.email = person.get("email")
        self.national_registration = person.get("national_registration")
        self.__remove_unwanted_keys(remove_keys)

    def __remove_unwanted_keys(self, keys):
        [delattr(self, key) for key in keys if hasattr(self, key)]


class Appointment:
    def __new__(cls, appointments_json, remove_keys=AppointmentsType.DEFAULT.value):
        instance = super(Appointment, cls).__new__(cls)
        instance.__init__(appointments_json, remove_keys)
        return vars(instance)

    def __init__(self, appointments_json, remove_keys: list):
        appointment = dict(appointments_json)
        self.unit = appointment.get("unit")
        self.formatted_date = appointment.get("formatted_date")
        self.formatted_day = appointment.get("formatted_day")
        self.formatted_time = appointment.get("formatted_time")
        self.attendance_number = appointment.get("attendance_number")
        self.__remove_unwanted_keys(remove_keys)

    def __remove_unwanted_keys(self, keys):
        [delattr(self, key) for key in keys if hasattr(self, key)]


class Message:
    def __init__(self, message, marketplace_id, type="notification.sms", event="send.sms", resource="teste"):
        self.topic_message = {
            "type": type,
            "resource": resource,
            "description": "",
            "object": message
            }
        self.message_attributes = {
            "event": {
                "DataType": "String",
                "StringValue": event
                },
            "marketplace_id": {
                "DataType": "String",
                "StringValue": marketplace_id
                },
            "resource": {
                "DataType": "String",
                "StringValue": resource
                },
            "source": {
                "DataType": "String",
                "StringValue": "api"
                },
            "type": {
                "DataType": "String",
                "StringValue": type
                }
            }

    def __eq__(self, obj):
        return isinstance(obj, Message) and obj.topic_message == self.topic_message and \
               obj.message_attributes == self.message_attributes
