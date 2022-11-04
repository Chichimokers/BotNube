# import multivolumefile
# import py7zr

# def makezip(target, name, size):
#     path = f"./{target}"
#     with multivolumefile.open("./archivos/"+name, mode="wb", volume=int(size) * 1024 * 1024) as file:
#         with py7zr.SevenZipFile(file, "w") as archive:
#             archive.writeall(path, target)

from os import unlink
import shutil
import py7zr
from pathlib import Path

def compress(fpath: str, part_size: int):
    fpath: Path = Path(fpath)
    filters = [{"id": py7zr.FILTER_COPY}]
    file_list = []

    with py7zr.SevenZipFile(
        f"{fpath}.7z",
        "w",
        filters=filters,
    ) as f:
        f.write(fpath, fpath.name)
    unlink(fpath)

    with open(f"{fpath}.7z", "rb") as zip_file:
        file_count = 1
        eof = False
        while True:
            with open(f"{fpath}.7z.{file_count:03d}", "wb") as file_part:
                wrote_data = 0
                while wrote_data < (part_size * 1024 * 1024):
                    data = zip_file.read(1024 * 1024)
                    if not data:
                        eof = True
                        break
                    else:
                        file_part.write(data)
                        wrote_data += len(data)

            file_list.append(f"{fpath}.7z.{file_count:03d}")

            if eof:
                break
            file_count += 1

    unlink(f"{fpath}.7z")
    
    # for d in file_list:
    #     shutil.move(d, './downloads/')
    return file_list