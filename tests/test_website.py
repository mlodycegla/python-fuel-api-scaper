import sys

sys.path.append("../flaskr")
from __init__ import app


# testing /europe route
def test_get_api():
    client = app.test_client()
    url = "europe"

    response = client.get(url)

    assert response.status_code == 200
