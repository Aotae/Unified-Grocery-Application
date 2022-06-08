# UGA (Unified Grocery Application)

# Installation
## MongoDB Server

## How to Install MongoDB for Mac OS (without brew.)
The following gives a thorough explanation on how to install MongoDB without homebrew.
https://gist.github.com/Sydney-o9/9a6d4a017539cb8610a5695ae505bb61

## How to Install MongoDB

## 1. Download latest MongoDB distro
DOWNLOAD LINK for Community Edition: https://www.mongodb.com/try/download/community
SELECT On-premises -> <Newest Version> -> <Your OS> -> <Your Prefered Arhiving format>

## 2. MongoDB Installation
### a. If you are on Windows.
Simply follow the installation wizard and mark install as a service to be true.
### b. If you are on Mac and have Homebrew installed:
  #### 1.
    Go to the terminal and extract MongoDB from your archive that we downloaded (by default this should be your downloads folder)
  #### 2.
    Move the extracted folder to your local binary storage do this using sudo mv <folder_name> /usr/local/mongodb, this will ask for a password
    To check if we succesfully moved the folder simply go to your local binary store and use 'ls'
    Change directories to /usr/local/mongodb using 'cd'
  #### 3.
    Create the data/db folder, this is where Mongodb will store its data that we insert.
    We can do this using sudo 'mkdir' with option -p call the folder /data/db
    Check if it was created using 'cd'
    ```sh
    sudo chown <user-name> /data/db
    ```
  #### 4.
    Next we will change the permissions of the directory using 'chown'
    ```sh
    sudo chown <user-name> /data/db
    ```
  
  
  
