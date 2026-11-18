from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    ss = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
    )
    print("Valid station created:")
    print(f"ID: {ss.station_id}")
    print(f"Name: {ss.name}")
    print(f"Crew: {ss.crew_size} people")
    print(f"Power: {ss.power_level}%")
    print(f"Oxygen: {ss.oxygen_level}%")
    print(
        f"Status: {'Operational' if ss.is_operational else 'Non-operational'}"
    )
    print("=" * 40)

    try:
        SpaceStation(
            station_id="ISS002",
            name="Invalid Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
