from unittest.mock import Mock,patch
from api_service import get_user

# api_service.requests.get
#         ↓
#     temporarily replaced
#         ↓
#       Mock
#         ↓
#     mock_get
@patch("api_service.requests.get")
def test_get_user(mock_get):
    mock_response = Mock()     # This represents the fake HTTP response.
    mock_response.json.return_value = {        # When the fake response's .json() is called, return this dictionary
        "name":"kesha"
    }
    mock_get.return_value = mock_response       #When the fake requests.get() is called, return my fake response.
    result = get_user()

    assert result == "kesha"
