# Networks Lab 2
Jesse Shellabarger & Tayler How

## How to use

Run server.py. It will prompt the user for it's port. Then run the client. It will prompt the user for the server's IP and port. Commands can then be given to the client to be run on the server. `iWant <filename>` will request a file from the server (in its store directory) and place it in the client's received directory. `uTake <filename>` will send the file to the server (from the received directory), which will place it in its store directory.

All commands are verified to be well formed on the server.  