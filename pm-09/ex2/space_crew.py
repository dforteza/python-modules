from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(le=80, ge=18)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(le=50, ge=0)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")
        has_captain = any(m.rank is Rank.captain for m in self.crew)
        has_commander = any(m.rank is Rank.commander for m in self.crew)
        if has_captain is False and has_commander is False:
            raise ValueError(
                "Mission must have at least one Commander or Captain")
        experience_crew = sum(1 for m in self.crew if m.years_experience >= 5)
        if (
            self.duration_days > 365
            and experience_crew < 0.5 * len(self.crew)
        ):
            raise ValueError(
                "Long missions (> 365 days) need 50% experienced crew "
                "(5+ years)"
            )
        all_active = all(m.is_active is True for m in self.crew)
        if not all_active:
            raise ValueError("All crew members must be active")
        return (self)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    sarah = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=42,
        specialization="Mission Command",
        years_experience=15,
    )
    john = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=35,
        specialization="Navigation",
        years_experience=8,
    )
    alice = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=29,
        specialization="Engineering",
        years_experience=3,
    )

    sm = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 9, 1),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {sm.mission_name}")
    print(f"ID: {sm.mission_id}")
    print(f"Destination: {sm.destination}")
    print(f"Duration: {sm.duration_days} days")
    print(f"Budget: ${sm.budget_millions}M")
    print(f"Crew size: {len(sm.crew)}")
    print("Crew members:")
    for m in sm.crew:
        print(f"- {m.member_id} ({m.name}) - {m.rank.value}")

    print()
    print("=" * 41)

    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date=datetime(2024, 12, 1),
            duration_days=30,
            crew=[john, alice],
            budget_millions=500.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for detail in e.errors():
            print(detail["ctx"]["error"])


if __name__ == "__main__":
    main()
