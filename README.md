A password manager that supports many users and stores hashes for its user's key.
WARNING!:
The script uses verified cryptography like sha512, 2048 byte rsa keys... but I cannot guarantee that it is absolutely safe to use
(The rsa keys are stored locally encrypted with its user's key,
in other words if someone manages to break a user's hash (salted) with a little more effort they will have access to the user's password data)
