import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        s = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = s.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        try:
            for part in parts:
                coords.append(float(part))
        except ValueError as e:
            print(f"Error on parameter '{part.strip()}': {e}")
            continue
        return (coords[0], coords[1], coords[2])


def distance(p1: tuple[float, float, float],
             p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return (d)


def coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    x, y, z = first
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(distance((0.0, 0.0, 0.0), first), 4)}")
    print()
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    coordinate_system()
