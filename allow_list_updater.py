
from pathlib import Path
import argparse


def read_entries(file_path):
    """Read non-empty entries from a text file."""
    return [
        line.strip()
        for line in file_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def update_allow_list(allow_list, remove_list):
    """Remove matching entries while preserving the original order."""
    entries_to_remove = set(remove_list)
    updated_list = [
        entry for entry in allow_list
        if entry not in entries_to_remove
    ]
    removed_count = len(allow_list) - len(updated_list)
    return updated_list, removed_count


def main():
    parser = argparse.ArgumentParser(
        description="Update a text allow-list."
    )
    parser.add_argument("allow_file", help="Input allow-list file")
    parser.add_argument("remove_file", help="Entries to remove")
    parser.add_argument(
        "--output",
        default="allow_list_updated.txt",
        help="Output filename"
    )
    args = parser.parse_args()

    try:
        allow_list = read_entries(Path(args.allow_file))
        remove_list = read_entries(Path(args.remove_file))

        updated_list, removed_count = update_allow_list(
            allow_list, remove_list
        )

        Path(args.output).write_text(
            "".join(entry + "\n" for entry in updated_list),
            encoding="utf-8"
        )

        print(f"Original entries: {len(allow_list)}")
        print(f"Entries removed: {removed_count}")
        print(f"Updated list saved to: {args.output}")

    except OSError as error:
        parser.error(f"File error: {error}")


if __name__ == "__main__":
    main()
