import zipfile

path_to_zip_file = 'data/archive.zip'
directory_to_extract_to = 'data'

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)