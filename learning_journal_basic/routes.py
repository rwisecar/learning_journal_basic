"""The routes defines the paths for the different pages."""


def includeme(config):
    """Add routes for the configuration to find."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("list", "/")
    config.add_route("create", "/journal/new-entry")
    config.add_route("detail", "/journal/{id:\d+}")
    config.add_route("edit", "/journal/{id:\d+}/edit-entry")
