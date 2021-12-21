import argparse
import shutil

from pathlib import Path

_template_folder = Path(__file__).parent / "templates"
TEMPLATE_FILES = {
    "problem": _template_folder / "template_problem.py",
    "input": _template_folder / "template_input.txt",
    "test": _template_folder / "template_test.py",
    "scratch": _template_folder / "template_scratch.py",
}


def _format_prob_num(prob_num: int) -> str:
    """Returns the supplied integer as a 4 character string padded with leading 0."""
    return "{:0>4d}".format(int(prob_num))


def create_files(prob_num: int, force: bool = False) -> None:
    """Creates a folder for the supplied problem number, and copies template files into it."""
    prob = _format_prob_num(prob_num)
    file_name_core = f"pe{prob}"
    destination_files = {
        "problem": f"{file_name_core}.py",
        "test": f"test_{file_name_core}.py",
        "input": f"{file_name_core}_input.txt",
        "scratch": "scratch_1.py",
    }

    prob_folder_path = Path(__file__).parent / f"pe{prob}"
    Path.mkdir(prob_folder_path, parents=True, exist_ok=force)

    for f_type, file in TEMPLATE_FILES.items():
        prob_file_path = prob_folder_path / destination_files[f_type]
        shutil.copy(file, prob_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("prob", help="The number of the problem to be set up.", type=int)
    parser.add_argument("-f", "--force", help="Overwrites files in the target folder, if they exist.", action="store_true")
    args = parser.parse_args()
    create_files(args.prob, args.force)
    print(f"\nFolder set up for problem number {args.prob}.\nGood luck!")


# Name Templates:
# ./pe0000
#  - pe0000.py
#  - test_pe0000.py
#  - pe0000_input.txt
#  - scratch.py

