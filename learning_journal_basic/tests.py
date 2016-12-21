import pytest
from pyramid import testing


@pytest.fixture
def req():
    """Set up a request object by instantiating from the DummyRequest class."""
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture
def testapp():
    """Create an instance of our app for testing."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_page_has_the_right_variable(req):
    """Test that the home page view returns data."""
    from .views import list
    response = list(req)
    assert "entries" in response


def test_home_page_has_iterable(req):
    from .views import list
    response = list(req)
    assert hasattr(response["entries"], "__iter__")


def test_home_page_has_list(testapp):
    """Test that home page has list of entries rendered."""
    response = testapp.get("/", status=200)
    inner_html = response.html
    assert "Today I learned how to set up a blog." in inner_html.find("body").text


def test_detail_page_has_detail(testapp):
    """Test that detail page has list of entry rendered."""
    response = testapp.get("/journal/3", status=200)
    inner_html = response.html
    assert "Now time for some pirate ipsum." in inner_html.find("body").text


def test_create_page_has_data(testapp):
    """Test that detail page has data."""
    response = testapp.get("/journal/new-entry", status=200)
    inner_html = response.html
    assert "Create a Post" in inner_html.find("main").text


def test_edit_page_has_data(testapp):
    """Test that the edit page has data."""
    response = testapp.get("/journal/2/edit-entry")
    inner_html = response.html
    assert "Title:" in inner_html.find("article").text
