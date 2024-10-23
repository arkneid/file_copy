# imports
import csv
import Logging
import shutil


class CsvActions:
    def __init__(self) -> None:
        self.__database_csv_file = "database_names.csv"
        self.__log = Logging.Logging()

    def get_file_names(self, ext: str, output_folder: str, source_file: str) -> None:
        row_number: int = 0
        with open(self.__database_csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for value in csv_reader:
                if row_number != 0:
                    self.__log.logging(text=f"### Copying {source_file} to {value[0]}.{ext}")
                    shutil.copyfile(src=source_file, dst=f"{output_folder}/{value[0]}.{ext}")
                row_number += 1
