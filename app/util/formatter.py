import logging
from util import context_vars


class Formatter(logging.Formatter):
    def formatMessage(self, record):
        record.rid = context_vars.request_id_var.get()
        record.mid = context_vars.marketplace_id_var.get()
        return super().formatMessage(record)
