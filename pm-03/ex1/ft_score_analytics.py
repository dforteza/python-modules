import sys


def score_analytics(av: list[str]) -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for x in av[1:]:
        try:
            scores.append(int(x))
        except ValueError:
            print(f"Invalid parameter: '{x}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    score_analytics(sys.argv)
