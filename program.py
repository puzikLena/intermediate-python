import argparse
import logging
import os
from collections import namedtuple


def parse_file_info(path):
    """
    Функция для сбора информации о содержимом директории.
    """

    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file_path)[0]
            extension = os.path.splitext(file_path)[1]
            is_dir = False
            parent_dir = os.path.dirname(root)
            information = namedtuple('information', ['file_name', 'extension', 'is_dir', 'parent_dir'])
            file_list.append(information(file_name, extension, is_dir, parent_dir))

        return file_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir_path", help="Путь директории для выполнения программы")
    args = parser.parse_args()
    file_info = parse_file_info(args.dir_path)
    logger = logging.getLogger()
    handler = logging.FileHandler('file_info.log')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    for info in file_info:
        logger.info("Filename: " + info.file_name + ", Extension: " + info.extension + ", Is dir:" + str(
            info.is_dir) + ", Parent dir: " + info.parent_dir)


if __name__ == '__main__':
    main()
