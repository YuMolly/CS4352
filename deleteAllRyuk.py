import os


def deleteAll(sf, fe):
    start_folder = sf
    file_extension = fe
    # directories to skip searching in
    exclude = ['$Recycle.Bin', 'Copied Files']

    count = 0
    for root, dirs, files in os.walk(start_folder):
        # ensures files that are in the recycling bin and copied files are not included in the search
        dirs[:] = [d for d in dirs if d not in exclude]
        for file_name in files:
            if file_name.endswith(file_extension):
                absolute_path = os.path.abspath(os.path.join(root, file_name))
                print("Deleting:", absolute_path)
                os.remove(absolute_path)
                count += 1
    print('Completed.', count, 'files deleted.')


deleteAll('C:\\', '.ryuk')

