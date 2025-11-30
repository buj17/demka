import os

import config.settings


def convert_all_xml_to_py():
    xml_source_path = config.settings.BASE_DIR / 'gui' / 'ui' / 'xml'
    dest_path = config.settings.BASE_DIR / 'gui' / 'ui'
    for xml_file in xml_source_path.iterdir():
        res_filename = f'{xml_file.stem}_ui.py'
        command = f'pyside6-uic "{xml_file}" -o "{dest_path / res_filename}"'
        os.system(command)
        print(f'Converted {xml_file.name} to {res_filename}')


if __name__ == '__main__':
    convert_all_xml_to_py()
