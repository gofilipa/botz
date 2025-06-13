# Introduction to the Command Line

## Commands:

pwd
- print working directory (tells you where you are in the computer file system)

cd <folder name>
- change directory into specified folder name
- must be "above" the folder you want to move into 
- i.e. "cd Desktop" moves into Desktop (only works if you are in "home" folder aka, your username folder)

cd ..
- moves up one directory

cd ~ 
- moves to "home" folder (aka your username folder)

cd /
- moves to root folder (the first folder in your computer)

ls 
- list all files in the current directory

ls -a
- lists all files, including hidden ones, in the current directory
- the "-a" is called a "flag" or "option" to expand the ls command (in this case, to list all files, including hidden ones)

ls -l
- lists all files along with information about them (dates, permissions, owner, size, etc)

touch
- creates a file
- i.e. touch test.txt 

mkdir
- creates folder
- i.d. "mkdir class_notes"

nano <filename>
- opens command line text editor for writing files
