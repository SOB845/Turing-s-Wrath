# Turing's Wrath: the password generator
![Version](https://img.shields.io/badge/version-1.1.2-green.svg)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

With the daily rise of Web 2.0, we find ourselves in need of more user accounts and more secure passwords. However, keeping these account information is always a pain in the butt. You may want to write your account information on a sheet of paper (which might be better than digital storage in some cases) but that's not the only problem. **How do you make sure your password is as strong as it should be?** If you're not sure, then it doesn't matter where you keep it. Your password is the heart of your web immunity and **Turing's Wrath** is built to protect it.

# FAQs
### What is Turing's Wrath?
**Turing's Wrath** is an open-source random password generator developed for day-to-day or business usage. It uses the Secure Hashing Algorithm (SHA) and other third-party APIs to ensure the generated passwords (although impossible) do not collide with *pwned* ones.

### What does it mean for a password to be "pwned"?
It means that the password has been compromised in a data breach; AKA it's not safe at all. See [Definition of Pwned](https://www.urbandictionary.com/define.php?term=pwned). With the newest release (v.0.1), you can check if your own passwords are pwned or not with lookup_pwned_api.
**Turing's Wrath** uses this API to verify that the generated password has not been pwend. If a specific password turns out to be pwned, the program throws an error and terminates the running process.

### How do I use it?
**Turing's Wrath** comes in two versions: **CLI** (command line interface) and **GUI** (graphical user interface).
CLI version is suitable for users experienced with Unix-Linux based systems and I believe they don't need any further instructions.
GUI on the other hand, is built for everyday use cases.

### Why should my password length be more than 6 characters?
***TL;DR**: It's much safer this way
\
The answer lies in basic discrete mathematics. **Turing's Wrath** constructs random passwords by permutations of 90 characters (26 lower case + 26 upper case + 28 symbols + 10 digits). Let's assume that you want to generate a password of length 3, here is a visualization of the problem:
The multiplication principle of combinatorics states that if you want to arrange _n_ things in _m_ possible way while repetition is allowed, there are _n^m_ ways to do so. Thus there will be 90^3 = 729,000 possible permutations for a password of length 3. Assuming a brute force attack guesses 1 permutation in 1 second, it will take 729000 seconds (202.5 hours) until it guesses the correct permutation. 
\
The number of permutations grows exponentially with length. For length = 4, we have 90^4 = 65,610,000 and for length = 5, we will have 5,904,900,000 permutations.
Thus for the minimum length (i.e. 6), the number of possible permutations will be 531,441,000,000. That's a pretty long number but considering that modern computers are able to handle millions if not billions of computations in milliseconds, 531,441,000,000 is still a fragile number. The most common way an attacker could crack a password is a "Dictionary Attack"; in which a computer program runs over a database of commonly used phrases and replaces some letters with numbers/symbols until the correct password is guessed. This replacement in letters makes `helloworld` and `h3llow@rld` pretty much the same. However, this does not work smoothly in random passwords but if you use the same one for every platform and it gets pwned in one of them, that'll also be added to the attacker's database.

### Can I save these random passwords?
As of V1.0.0 users are able to store their passwords in a database. Press `SAVE PASSWORD` button in the main app and enter the name of the service and its corresponding password you want to save. This information will be stored in a local database. Please note that we have not yet developed an encryption system for the database, so the .db file must be encrypted manually by the users.

### Do you accept donations?
With pleasure!!! Since I regularly change my crypto wallet addresses, users willing to tip may send me an email (sobhan464@gmail.com) so I can provide them the latest addresses.
