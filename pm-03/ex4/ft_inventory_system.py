import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    # PARSE: keep valid 'item:quantity' args, discard the rest with a message
    inventory = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, quantity = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return (inventory)


def inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    if not inventory:
        return

    # KEYS + SUM VALUES
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    # PERCENTAGE
    for name in inventory.keys():
        percent = (inventory[name] / total) * 100
        print(f"Item {name} represents {round(percent, 1)}%")

    # MOST / LEAST: start with the first item; strict < and > keep the first
    names = list(inventory.keys())
    most = names[0]
    least = names[0]
    for name in names:
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    inventory_system()
