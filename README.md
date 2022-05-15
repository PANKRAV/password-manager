A password manager that supports many users and stores hashes for its user's key.
WARNING!:
The script uses verified cryptography like sha512, 2048 byte rsa keys... but I cannot guarantee that it is absolutely safe to use
(The rsa keys are stored locally encrypted with its user's key,
in other words if someone manages to break a user's hash (salted) with a little more effort they will have access to the user's password data).
I also want to add a decorator to prevent timing attacks.

P.S.
This was basically my first big project. It really helped me understand how to structure a huge project like for example how many python files would I need to create or how to structure my classes and the relations between them. I know I made so many mistakes along the way in the aspect of the structuring and organizing but I learned from those and next time I will try to organize my project clearly in well defined boundaries making only useful classes and files(and not trying to fit everything in one place). But overall I liked the outcome.

P.S.S.
The code is not that readable (:
