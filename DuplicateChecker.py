# Generate MD5 checksum for all files placed under a folder

import hashlib
import os

# set home folder- where do you want to write the information?
# don't forget to make a txt file called "dupl.txt"
home_folder = ""
src_folder = input("path: ")


def generate_md5(fname, chunk_size=4096):
   
    # Function which takes a file name and returns md5 checksum of the file
   
    hash = hashlib.md5()
    
    with open(fname, "rb") as f:
            # Read the 1st block of the file
            chunk = f.read(chunk_size)
            # Keep reading the file until the end and update hash
            while chunk:
                hash.update(chunk)
                chunk = f.read(chunk_size)
                
    f.close()
        # Return the hex checksum
    return hash.hexdigest()


if __name__ == "__main__":
   
    # Starting block of the script
    
    md5_list = dict()

    # Iterate through all files under source folder
    for root, dirs, files in os.walk(src_folder):
        
        for file_name in files:
                # walk through each file in the directory, return path as key, name and md5 hash as value to dict
                md5_list[os.path.join(root,file_name)]= (
                [(generate_md5(os.path.join(root, file_name))),
                 file_name]
                )
    # write dict to txt file in format "path: hash, filename"
    #  mode set to append, change to "w" to set to overwrite file
    with open(os.path.join(home_folder, "dupl.txt"), "a") as f:
        for  key, value in md5_list.items():
            f.write("{} : {} \n".format(key, value))
            print("{} : {}".format(key, value))
    f.close()