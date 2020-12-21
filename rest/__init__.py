from .urls import API_ENDPOINTS


def initialize_app(app):
    for path, func_meta in API_ENDPOINTS.items():
        handler, methods = func_meta
        app.add_url_rule(path, handler.__name__, handler, methods=methods)
