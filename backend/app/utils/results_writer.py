import json
from pathlib import Path


class ResultsWriter:

    def save(
        self,
        run_id,
        data
    ):

        results_dir = Path(
            "results"
        )

        results_dir.mkdir(
            exist_ok=True
        )

        file_path = (
            results_dir
            / f"{run_id}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

        return str(file_path)