Day 66 -> Shutil module in python


Shutil:
shutil (short for shell utilities) is used for file and directory operations like copying, moving, or deleting — at a higher level than the basic os module.

Commonly Used Functions:
shutil.copy(original_file, target_file) – Copies a file from original_file to target_file.
shutil.copy2(original_file, target_file) – Same as copy, but preserves metadata (timestamps, etc.).
shutil.copytree(source_folder, backup_folder) – Recursively copies source_folder to backup_folder.
shutil.move(file_to_move, new_location) – Moves or renames file_to_move to new_location.
shutil.rmtree(folder_to_delete) – Deletes folder_to_delete and all its contents.
