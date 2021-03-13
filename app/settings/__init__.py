from importlib import import_module
import os
import warnings


__all__ = ("settings",)


try:
    settings_file = os.getenv("APP_SETTINGS", "local")
except KeyError:
    warnings.warn(
        """\n\nA variável de ambiente deve ser definida APP_SETTINGS.\nValores possíveis:  test, local, production ou staging\n\n"""
    )
    raise SystemExit

settings = import_module(f"settings.{settings_file}", package="settings")
