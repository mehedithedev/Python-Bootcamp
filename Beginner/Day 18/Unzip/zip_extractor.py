import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


# Test the backend below:

if __name__ == "__main__":
    extract_archive("compressed.zip",
                    "/directory")