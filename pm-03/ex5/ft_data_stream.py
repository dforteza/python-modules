import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release",
           "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    # ENDLESS: pick a random player and action, yield them as a tuple
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    # UNTIL EMPTY: pick a random event, remove it, then yield it
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    # STREAM: create the generator once, ask next() 1000 times
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    # LIST: 10 more events from the same generator
    events = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")

    # CONSUME: the for asks consume_event until the list is empty
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    data_stream()
