from app.main import read_item

def test_read_item():
    assert read_item(2) == "Banana"