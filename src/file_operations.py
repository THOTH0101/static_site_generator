import os
import shutil


def copy_contents_to_public(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        print(f"Deleting destination: {dest_dir}")
        shutil.rmtree(dest_dir)

    print(f"Creating destination: {dest_dir}")
    os.mkdir(dest_dir)
    copy_from_src_to_dest(src_dir, dest_dir)


def copy_from_src_to_dest(src, dest):
    if not os.path.exists(src):
        raise Exception("Error: invalid source directory")

    contents = os.listdir(src)
    for content in contents:
        src_path = os.path.join(src, content)
        dest_path = os.path.join(dest, content)
        if os.path.isfile(src_path):
            print(f"File: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            print(f"Directory: {dest_path}")
            os.mkdir(dest_path)
            copy_from_src_to_dest(src_path, dest_path)
