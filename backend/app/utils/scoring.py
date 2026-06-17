from datetime import datetime


def calculate_score(
    start_time,
    end_time,
    commit_count,
    all_tests_pass
):

    base = 100

    duration = (
        end_time - start_time
    ).total_seconds() / 60

    speed_bonus = (
        10 if duration < 5
        else 0
    )

    efficiency_penalty = max(
        0,
        (commit_count - 20) * 2
    )

    total = (
        base
        + speed_bonus
        - efficiency_penalty
    )

    if not all_tests_pass:
        total = max(
            0,
            total - 50
        )

    return {
        "base": base,
        "speed_bonus": speed_bonus,
        "efficiency_penalty":
            efficiency_penalty,
        "total": total
    }