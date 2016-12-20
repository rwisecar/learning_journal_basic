"""The views module is the logic behind rendering the templates."""

from pyramid.response import Response
from pyramid.view import view_config
import io
import os


THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Learning Journal | Day 3",
        "id": 3,
        "creation_date": "December 20, 2016",
        "body": """Today I learned how to set up a blog.
                Now time for some pirate ipsum.
                Loaded to the gunwalls gibbet bucko dead men tell no tales.
                Pressgang grapple careen Sail ho gally bilged on her anchor.
                Run a shot across the bow doubloon log gunwalls pillage.
                Maroon sloop heave to careen boom handsomely Blimey port sheet.
                Skysail shrouds aye Sail ho ye blow the man down.
                Shiver me timbers belaying pin provost carouser knave haul.
                Wind hands main sheet holystone Gold Road pirate booty.
                Buccaneer measured fer yer chains red ensign.
                Mizzenmast careen Jolly Roger gally long clothes pillage swab.
                Blimey grapple galleon keel coxswain lee bowsprit quarterdeck
                """},
    {"title": "Learning Journal | Day 2",
        "id": 2,
        "creation_date": "December 17, 2016",
        "body": """This is an entry that has been backdated.
                Now time for some pirate ipsum.
                Loaded to the gunwalls gibbet bucko dead men tell no tales.
                Pressgang grapple careen Sail ho gally bilged on her anchor.
                Run a shot across the bow doubloon log gunwalls pillage.
                Maroon sloop heave to careen boom handsomely Blimey port sheet.
                Skysail shrouds aye Sail ho ye blow the man down.
                Shiver me timbers belaying pin provost carouser knave haul.
                Wind hands main sheet holystone Gold Road pirate booty.
                Buccaneer measured fer yer chains red ensign.
                Mizzenmast careen Jolly Roger gally long clothes pillage swab.
                Blimey grapple galleon keel coxswain lee bowsprit quarterdeck
                """},
    {"title": "Learning Journal | Day 1",
        "id": 1,
        "creation_date": "December 10, 2016",
        "body": """This is another entry that has been backdated.
                It should be the first entry.
                Now time for some pirate ipsum.
                Loaded to the gunwalls gibbet bucko dead men tell no tales.
                Pressgang grapple careen Sail ho gally bilged on her anchor.
                Run a shot across the bow doubloon log gunwalls pillage.
                Maroon sloop heave to careen boom handsomely Blimey port sheet.
                Skysail shrouds aye Sail ho ye blow the man down.
                Shiver me timbers belaying pin provost carouser knave haul.
                Wind hands main sheet holystone Gold Road pirate booty.
                Buccaneer measured fer yer chains red ensign.
                Mizzenmast careen Jolly Roger gally long clothes pillage swab.
                Blimey grapple galleon keel coxswain lee bowsprit quarterdeck
                """},
]


@view_config(route_name="list", renderer="templates/list.jinja2")
def list(request):
    """View for the home page."""
    # Key in dict must match up with naming in jinja2 template
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail(request):
    """View for the home page."""
    # the_id = int(request.matchdict["id"])
    # entry = ENTRIES[the_id]
    # return {"entry": entry}
    pass


@view_config(route_name="create", renderer="string")
def create(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "create.html")
    file_data = io.open(file_path).read()
    return file_data


@view_config(route_name="edit", renderer="string")
def edit(request):
    """View for the home page."""
    file_path = os.path.join(THIS_DIR, "templates", "edit.html")
    file_data = io.open(file_path).read()
    return file_data
