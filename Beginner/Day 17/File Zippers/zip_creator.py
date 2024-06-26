import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":   ## use this method to test it in the backend
    make_archive(filepaths=
                 ["zip.txt", "zip1.txt"],
                 dest_dir="dest"
                 )