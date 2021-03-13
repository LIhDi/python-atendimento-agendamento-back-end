from sanic_openapi import doc
from util.decorator import composed


class Unit:
    name = doc.String()
    code = doc.String()
    description = doc.String()
    email = doc.String()
    phone = doc.String()
    active = doc.Boolean()


class Subject:
    name = doc.String()
    code = doc.String()
    description = doc.String()
    active = doc.Boolean()


class Error:
    category = doc.String()
    message = doc.String()
    status_code = doc.String()
    type = doc.String()
    status = doc.String()


class ErrorResponse:
    error = doc.Object(Error)


error_response = [doc.response(401, ErrorResponse, description="No permission to access this URI."),
                  doc.response(400, ErrorResponse, description="Missing parameter key."),
                  doc.response(500, ErrorResponse, description="Server got itself in trouble.")]

unit_sucess = doc.response(200, Unit, description="Success")
subject_sucess = doc.response(200, Unit, description="Success")

save_unit_api = composed(
    doc.consumes(doc.JsonBody({
        "name": doc.String(),
        "description": doc.String(),
        "code": doc.String(),
        "email": doc.String(),
        "phone": doc.String(),
        "active": doc.Boolean()
        }), location="body", content_type="application/json"),
    unit_sucess,
    *error_response
)

get_all_unit_api = composed(
    doc.consumes(doc.Boolean(name="active"), location="query", required=False),
    unit_sucess,
    doc.response(401, ErrorResponse, description="No permission to access this URI"),
    doc.response(500, ErrorResponse, description="Server got itself in trouble.")
)

get_unit_by_code_api = composed(
    doc.consumes(doc.String(name="code_unidade"), location="path", required=False),
    unit_sucess,
    doc.response(404, ErrorResponse, description="Nothing matches the given URI."),
    doc.response(401, ErrorResponse, description="No permission to access this URI"),
    doc.response(500, ErrorResponse, description="Server got itself in trouble.")
)

save_subject_api = composed(
        doc.consumes(doc.JsonBody({
            "name": doc.String(),
            "description": doc.String(),
            "code": doc.String(),
            "active": doc.Boolean()
            }), location="body", content_type="application/json"),
    subject_sucess,
    *error_response
)

get_all_subject_api = composed(
    doc.consumes(doc.Boolean(name="active"), location="query", required=False),
    subject_sucess,
    doc.response(401, ErrorResponse, description="No permission to access this URI"),
    doc.response(500, ErrorResponse, description="Server got itself in trouble.")
)

get_subject_by_code_api = composed(
    doc.consumes(doc.String(name="code_assunto"), location="path", required=False),
    subject_sucess,
    doc.response(404, ErrorResponse, description="Nothing matches the given URI."),
    doc.response(401, ErrorResponse, description="No permission to access this URI"),
    doc.response(500, ErrorResponse, description="Server got itself in trouble.")
)
