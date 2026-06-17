from pathlib import Path

from app.utils.llm_client import LLMClient
from app.utils.validator import validate_python_code


class FixGenerator:

    def __init__(self):
        self.llm = LLMClient()
    
    
    def apply_fix(self, error):

        file_path = Path(error["file"])

        if not file_path.exists():
            print(f"Skipping invalid file: {file_path}")
            return False
        
        if not file_path.is_file():
            print(f"Not a file: {file_path}")
            return False

        original = file_path.read_text(
            encoding="utf-8"
        )

        fixed = self.llm.generate_fix(
            error["description"],
            original
        )

        if not fixed:
            return False

        if not validate_python_code(fixed):
            return False

        backup_path = file_path.with_suffix(
            file_path.suffix + ".bak"
        )

        backup_path.write_text(
            original,
            encoding="utf-8"
        )

        file_path.write_text(
            fixed,
            encoding="utf-8"
        )

        return True