from uuid import uuid4

from secure import SecureHeaders

from util import context_vars

secure_headers = SecureHeaders()


def setup_middlewares(app):
    @app.middleware("security")
    async def set_secure_headers(request, response):
        secure_headers.sanic(response)

    @app.middleware("request")
    def context_args(request):
        context_vars.request_id_var.set(uuid4().hex)

    @app.middleware("response")
    def response_headers(request, response):
        response.headers.add("X-Request-ID", context_vars.request_id_var.get())
        response.headers.add("X-Marketplace-ID", context_vars.marketplace_id_var.get())
        response.headers.add("content-type", "application/json")
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
