"""The views module is the logic behind rendering the templates."""

from pyramid.view import view_config
import io
import os


THIS_DIR = os.path.dirname(__file__)

ENTRIES = {
    3: {"title": "Learning Journal | Day 3",
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
                Splice the main brace execution dock bilge gabion yo-ho-ho.
                Sea Legs long boat ballast keelhaul poop deck.
                No prey, no pay topsail plunder Pieces of Eight belaying pin.
                Take a caulk bowsprit splice the main brace ho transom.
                Prow lugger rutters cog Pieces of Eight shrouds coxswain.
                Capstan careen bilged on her anchor. Salmagundi splice the.
                Main brace blow the man down bucko boatswain lugsail galleon.
                Mizzen boom squiffy.
                """},
    2: {"title": "Learning Journal | Day 2",
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
    1: {"title": "Learning Journal | Day 1",
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
}


@view_config(route_name="list", renderer="templates/list.jinja2")
def list(request):
    """View for the list page."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail(request):
    """View for the detail page."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry, "id": the_id}


@view_config(route_name="create", renderer="templates/create.jinja2")
def create(request):
    """View for the create new entry page."""
    return {"entries": ENTRIES}


@view_config(route_name="edit", renderer="templates/edit.jinja2")
def edit(request):
    """View for the edit post page."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}
