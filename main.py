from pathlib import Path

our_files = Path('/Users/dawid/Desktop/Codes/PDF')

for file in our_files.iterdir():
    if file.is_file() and file.stem != ".DS_Store":

        file_name = file.stem
        extension = file.suffix

        article, cust_art, batch, measur = file_name.split(' - ')
        #print(file_name)
        new_path = our_files.joinpath(article, batch)
        new_file_name = f'{file_name}{extension}'
        #print(new_file_name)

        if not new_path.exists():
            new_path.mkdir(parents=True)

        new_file_path = new_path.joinpath(new_file_name)

        #print(new_file_path)
        file.replace(new_file_path)
