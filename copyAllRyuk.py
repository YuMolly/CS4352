import os
import shutil


def create_copy_directory():
    if not os.path.exists(os.getcwd() + '\\Copied Files'):
        os.makedirs(os.getcwd() + '\\Copied Files')


def copyAll(sf, fe, cd):
    start_folder = sf
    file_extension = fe
    copy_destination = cd

    # directories to skip searching in
    exclude = ['$Recycle.Bin', 'Copied Files']

    count = 0
    for root, dirs, files in os.walk(start_folder):
        # ensures files that are in the recycling bin and copied files are not included in the search
        dirs[:] = [d for d in dirs if d not in exclude]
        for file_name in files:
            if file_name.endswith(file_extension):
                absolute_path = os.path.abspath(os.path.join(root, file_name))
                print("Copying:", absolute_path, "to", copy_destination)
                shutil.copy(absolute_path, copy_destination)
                count += 1
    print('Completed.', count, 'files copied to', copy_destination)


create_copy_directory()
copyAll('C:\\', '.ryuk', 'Copied Files')

