# imports
import os
import argparse
import Logging
from csv_actions import CsvActions


def main(source_file: str) -> None:
    OUTPUT_FOLDER: str = "output"
    CURRENT_PATH: str = os.path.dirname(__file__)
    log = Logging.Logging()
    csv_handler = CsvActions()
    
    if not os.path.isfile(f"{CURRENT_PATH}/{source_file}"):
        log.logging(text="Source file is not present")
        exit(1)

    if os.path.exists(f"{CURRENT_PATH}/{OUTPUT_FOLDER}"):
        if not os.path.isdir(f"{CURRENT_PATH}/{OUTPUT_FOLDER}"):
            os.mkdir(f"{CURRENT_PATH}/{OUTPUT_FOLDER}")
            log.logging(text="Folder output created")
        else:
            log.logging(text="Folder output is already created")
    else:
        os.mkdir(f"{CURRENT_PATH}/{OUTPUT_FOLDER}")
        log.logging(text="Folder output created")

    source_file_extension = source_file.split(".")[1].strip()
    csv_handler.get_file_names(ext=source_file_extension, output_folder=f"{CURRENT_PATH}/{OUTPUT_FOLDER}", source_file=f"{CURRENT_PATH}/{source_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-file", help="The source file from where the new files will be copied", required=True)

    args = parser.parse_args()
    
    main(source_file=args.source_file)
