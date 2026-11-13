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

    def get_values(self) -> list[tuple[int, str]]:
        return (self._values)

    def get_count(self) -> int:
        return (self._count)


class NumericProcessor(DataProcessor):
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


class DataStream():
    def __init__(self) -> None:
        self._processor_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processor_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for e in stream:
            flag: bool = False
            for processor in self._processor_list:
                if processor.validate(e) == True:
                    processor.ingest(e)
                    flag = True
                    break
            if flag == False:
                print(
                    f"DataStream error - Can't process element in stream: {e}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processor_list:
            print("No processor found, no data")
        else:
            for processor in self._processor_list:
                name = type(processor).__name__
                total = processor.get_count()
                remaining = len(processor.get_values())
                print(
                    f"{name}: total {total} items processed, "
                    f"remaining {remaining} on processor"
                )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    # INIT
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print()

    # FIRST BATCH: only Numeric
    print("Registering Numeric Processor")
    numeric_processor = NumericProcessor()
    data_stream.register_processor(numeric_processor)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    print()
    data_stream.print_processors_stats()
    print()

    # SECOND BATCH: all processors
    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print("Send the same batch again")
    data_stream.process_stream(batch)
    print()
    data_stream.print_processors_stats()

    # CONSUME
    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric_processor.output()
    for _ in range(2):
        text_processor.output()
    log_processor.output()
    print()
    data_stream.print_processors_stats()
    print()


if __name__ == "__main__":
    main()
