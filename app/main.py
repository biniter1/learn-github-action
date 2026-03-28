from app.routes.items import get_item_name

def read_item(item_id: int) -> str:
    return get_item_name(item_id)


if __name__ == "__main__":
    print(read_item(1))