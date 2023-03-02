from flask import current_app

from indico.core.plugins import IndicoPlugin


class CanonicalLoginPlugin(IndicoPlugin):
    def __init__(self, *args, **kwargs):
        super().init(*args, **kwargs)
        current_app.config["MULTIPASS_LOGIN_SELECTOR_TEMPLATE"] = "canonical_login:canonical_login_selector"