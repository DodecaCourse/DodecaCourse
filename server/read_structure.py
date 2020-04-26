"""
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz,
Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
"""
import json


def insert_structure(structure_file, modules_db, chapters_db, targets_db,
                     output=False):
    """
    Reads the structure of modules, chapters and levels contained in
    a structure file(e. g. public/structure.json)

    Args:
        str: url of the file to read

    Raises:
        FileNotFoundError: file at url was not found is or invalid
    """
    with open(structure_file) as json_file:
        data = json.load(json_file)
        if(output):
            print("modules - chapter")
        for module in data["modules"]:
            if(output):
                print(module['id'], module['title'])
            module_id = module['id']
            modules_db.insert({
                'module_id': module_id,
                # 'module_name': module['title']
            })
            for chapter in module["chapters"]:
                if(output):
                    print("\t", chapter['id'], chapter['title'])
                chapters_db.insert({
                    'chapter_id': chapter['id'],
                    'module_id': module_id
                })
        if(output):
            print("targets")
        for target in data["targets"]:
            if(output):
                print(target['id'], target['chapter_id'], target['title'])
            targets_db.insert({
                'target_id': target['id'],
                'chapter_id': target['chapter_id']
            })
    # return modules_db, chapters_db, targets_db

# if __name__ == "__main__":
#     read_structure("../public/structure.json")
