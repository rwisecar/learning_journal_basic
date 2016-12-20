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
    assert "entry" in response


def test_home_page_has_iterable(req):
    from .views import list
    response = list(req)
    assert hasattr(response["entry"], "__iter__")


def test_home_page_has_list(testapp):
    """Test that home page has list of entries rendered."""
    response = testapp.get("/", status=200)
    inner_html = response.html
