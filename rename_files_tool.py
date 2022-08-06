"""File name replacer tool"""
import argparse
import os


def _get_argparse() -> argparse.ArgumentParser:
    module_description = 'Rename multiple files in a folder recursively.'

    ap = argparse.ArgumentParser(  # pylint: disable=invalid-name
        description=module_description,
        formatter_class=argparse.RawTextHelpFormatter
    )
    ap.add_argument(
        '-p',
        '--path',
        required=True,
        help='The folder path of the files you want to rename'
    )
    ap.add_argument(
        '-o',
        '--old',
        required=True,
        help='The old name common to all files you want to rename.'
    )
    ap.add_argument(
        '-n',
        '--new',
        required=False,
        help='The new common files name.'
    )

    return ap


if __name__ == '__main__':
    parser = _get_argparse()
    args = parser.parse_args()

    p_old = args.old
    p_path = args.path
    p_new = args.new

    print('Renaming files...')
    for path, subdirs, files in os.walk(p_path):
        for file in files:
            new_name = p_new if p_new else ''
            if p_old.lower() in file.lower():
                file_path = os.path.join(path, file)
                new_file_path = os.path.join(
                    path,
                    file.replace(p_old, new_name)
                )

                print(f'Renaming [{file_path}] ---to---> [{new_file_path}]')
                os.rename(file_path, new_file_path)

    print('Finished.')
