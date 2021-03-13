from util.status import HTTPStatus


def test_status_internal_server_error_when_missing():
    status = HTTPStatus("None")
    assert status == HTTPStatus.INTERNAL_SERVER_ERROR
