import pytest

from model.account import Account
from model.drivers_license import DriversLicense
from model.initialization import Initialization


@pytest.fixture()
def app(request):
    fixture = Initialization()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_drivers_license(app):
    app.session.login(Account(username="dit2015", password="mpgu2015"))
    app.pages.add_drivers_license(DriversLicense(serial_number="6666666666", date_issue="28032009"))
    app.session.logout()