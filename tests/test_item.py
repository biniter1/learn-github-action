from app.routes.items import get_item_name

def test_get_item_name_valid():
    assert get_item_name(1) == "Apple"

def test_get_item_name_invalid():
    assert get_item_name(999) == "Unknown"