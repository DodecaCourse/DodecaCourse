import json

# TODO: Überlegen ob man names brauch


def insert_structure(structure_file, modules_db, chapters_db, targets_db):
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
        print("modules - chapter")
        for module in data["modules"]:
            print(module['id'], module['title'])
            module_id = module['id']
            modules_db.insert({
                'module_id': module_id,
                # 'module_name': module['title']
            })
            for chapter in module["chapters"]:
                print("\t", chapter['id'], chapter['title'])
                chapters_db.insert({
                    'chapter_id': chapter['id'],
                    'module_id': module_id
                })
        print("targets")
        for target in data["targets"]:
            print(target['id'], target['chapter_id'], target['title'])
            targets_db.insert({
                'target_id': target['id'],
                'chapter_id': target['chapter_id']
            })
    return modules_db, chapters_db, targets_db

# if __name__ == "__main__":
#     read_structure("../public/structure.json")
