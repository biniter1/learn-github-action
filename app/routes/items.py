def get_item_name(item_id: int) -> str:
    items = {1: "Apple", 2: "Banana", 3: "Orange"}
    return items.get(item_id, "Unknown")
