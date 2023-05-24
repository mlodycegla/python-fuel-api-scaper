import sys

sys.path.append("../flaskr")
from __init__ import app


# testing /api/europe route
def test_get_api():
    client = app.test_client()
    url = "/api/europe"

    response = client.get(url)
    # decoding response so there is no need to use 'b' prefix later
    decoded_response = response.get_data().decode("utf-8")

    assert "country" in decoded_response
    assert "dieselprice" in decoded_response
    assert "gasolineprice" in decoded_response
    assert "lpgprice" in decoded_response
