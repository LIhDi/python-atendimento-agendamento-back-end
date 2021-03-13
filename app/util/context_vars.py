from contextvars import ContextVar

request_id_var = ContextVar("request_id", default="")
marketplace_id_var = ContextVar("marketplace_id", default="")
seller_id_var = ContextVar("seller_id", default="")
application_id_var = ContextVar("application_id", default="")
