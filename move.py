import shutil
import os
import mimetypes

movie_list = []

for files in os.listdir("."):
    if mimetypes.guess_type(files)[0] == "text/plain":
        movie_list.append(files)

for files in movie_list:
    shutil.move(f"/workspaces/Laf/{files}", "/workspaces/Laf/【中3数学】平方根/")