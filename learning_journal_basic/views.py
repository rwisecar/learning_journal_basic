"""The views module is the logic behind rendering the templates."""

from pyramid.response import Response
import io
import os


THIS_DIR = os.path.dirname(__file__)


def list(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "index.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "detail.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def create(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "create.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def edit(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "edit.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """Includeme config files for each page and path."""
    config.add_view(list,
                    route_name="list")
    config.add_view(detail,
                    route_name="detail")
    config.add_view(create,
                    route_name="create")
    config.add_view(edit,
                    route_name="edit")
