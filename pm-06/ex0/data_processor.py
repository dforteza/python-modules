from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._values: list[tuple[int, str]] = []
        self._count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._values:
            raise ValueError("No data to output")
        return (self._values.pop(0))

    def _save_value(self, value: str) -> None:
        self._values.append((self._count, value))
        self._count += 1


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return (True)
        elif (isinstance(data, list)):
            for i in data:
                if not (isinstance(i, int) or isinstance(i, float)):
                    return (False)
            return (True)
        else:
            return (False)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for value in data:
                self._save_value(str(value))
        else:
            self._save_value(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return (True)
        elif (isinstance(data, list)):
            for i in data:
                if not (isinstance(i, str)):
                    return (False)
            return (True)
        else:
            return (False)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for value in data:
                self._save_value(value)
        else:
            self._save_value(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not (isinstance(key, str) and isinstance(value, str)):
                    return (False)
            return (True)
        elif isinstance(data, list):
            for log in data:
                if not isinstance(log, dict):
                    return (False)
                for key, value in log.items():
                    if not (isinstance(key, str) and isinstance(value, str)):
                        return (False)
            return (True)
        else:
            return (False)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for log in data:
                self._save_value(
                    f"{log['log_level']}: {log['log_message']}"
                )
        else:
            self._save_value(
                f"{data['log_level']}: {data['log_message']}"
            )


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    # NUMERIC
    print("Testing Numeric Processor...")
    # - Validate
    numeric_processor = NumericProcessor()
    for data in [42, "Hello"]:
        print(f" Trying to validate input '{data}': "
              f"{numeric_processor.validate(data)}")

    # - Ingest
    print()
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f" Processing data: {numbers}")
    numeric_processor.ingest(numbers)

    # - Output
    print(" Extracting 3 values...")
    for _ in range(3):
        index, value = numeric_processor.output()
        print(f" Numeric value {index}: {value}")

    # TEXT
    print()
    print("Testing Text Processor...")
    # - Validate
    text_processor = TextProcessor()
    data = 42
    print(f" Trying to validate input '{data}': "
          f"{text_processor.validate(data)}")

    # - Ingest
    texts = ["Hello", "Nexus", "World"]
    print(f" Processing data: {texts}")
    text_processor.ingest(texts)

    # - Output
    print(" Extracting 1 value...")
    index, value = text_processor.output()
    print(f" Text value {index}: {value}")

    # LOG
    print()
    print("Testing Log Processor...")
    # - Validate
    log_processor = LogProcessor()
    data = "Hello"
    print(f" Trying to validate input '{data}': "
          f"{log_processor.validate(data)}")

    # - Ingest
    logs = [
        {"log_level": "NOTICE", "log_message": 1},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    try:
        print(f" Processing data: {logs}")
        log_processor.ingest(logs)

        # - Output
        print(" Extracting 2 values...")
        for _ in range(2):
            index, value = log_processor.output()
            print(f" Log entry {index}: {value}")
    except ValueError as e:
        print(f" Got exception: {e}")


if __name__ == "__main__":
    main()
