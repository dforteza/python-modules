from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with AC")
        if (
            self.contact_type == ContactType.physical
            and self.is_verified is False
        ):
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if (
            self.signal_strength > 7.0
            and (self.message_received is None or self.message_received == "")
        ):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return (self)


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    ac = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.now(),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Valid contact report:")
    print(f"ID: {ac.contact_id}")
    print(f"Type: {ac.contact_type.value}")
    print(f"Location: {ac.location}")
    print(f"Signal: {ac.signal_strength}/10")
    print(f"Duration: {ac.duration_minutes} minutes")
    print(f"Witnesses: {ac.witness_count}")
    print(f"Message: '{ac.message_received}'")
    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
        )
    except ValidationError as e:
        print("Expected validation error:")
        for detail in e.errors():
            print(detail["ctx"]["error"])


if __name__ == "__main__":
    main()
