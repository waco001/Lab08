# SY402 Lab 08

This Python file 'hash.py' allows users to record and monitor changes in the file structure.

How To Use:
- Download 'hash.py' into a folder for use.
- Store the initial hash with the following command. This will scrape all the filenames and hashes associated inside that folder and store them in a timestamped log file such as **131023-27Mar2021.SY402Log**

        python3 hash.py -s ~/Desktop/important_folder
- You can now use that folder normally, adding, deleted, and editing files within that **important_folder**. 
- When you want to monitor the additions, modifications, and removals of files in that folder, use the following command.
 
        python3 hash.py -c 131023-27Mar2021.SY402Log ~/Desktop/important_folder
- This will create a resultant log file that states the files which have been added, modified, or removed. For example:

        FOUND: []
        MODIFIED: ["~/Desktop/important_folder/file1.txt"]
        DELETED: []
        ADDED: ["~/Desktop/important_folder/file2.txt"]
- Moreover, the console will print an output that states the numbers of changes.

        >> Found: 0 Old Files
        >> Found: 0 Modified Files
        >> Found: 1 Deleted Files
        >> Found: 1 New Files