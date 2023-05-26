import requests
import data
import configuration
from untils.orders import create_order

# Гоголадзе Эксел 4-я когорта Дипломная работа, финальный спринт
def test_track_response() -> None:
    """Test track response."""
    # Create an order and ger a track identifier.
    order = create_order(body=data.order_body)
    track = order.get('track')
    assert track is not None, "Created order hasn't a track identifier."

    # Check track response.
    params = {'t': track}
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.ORDER_TRACK_PATH}", params=params)
    assert response.status_code == 200, f"Invalid status code, track id={track}."
