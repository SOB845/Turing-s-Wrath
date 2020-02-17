# Turing's Wrath: the password generator
With the daily rise of the Web 2.0, we find ourselves in need of new user accounts and more secure passwords. However, keeping these accounts information is always a pain in the ass. You might want to write your account information on a paper (which is way better than digital storages) but that's not the only problem. **How do you make sure your password is as strong as possible?** if you're not sure, then it doesn't matter how you keep it safe. Your password is the heart of your web immunity and **Turing's Wrath** is build to protect it.

# FAQs
### What is Turing's Wrath?
**Turing's Wrath** is an open-source app developed for generating random passwords. It uses Secure Hashing Algorithm (SHA) and other third-party APIs to make sure the generated passwords (although impossible) doesn't collide with _pwned_ passwords.

### How do I use it?
**Turing's Wrath** comes in two versions: **CLI** (command line interface) and **GUI** (graphical user interface).
CLI version is suitable for users experienced with Unix-Linux based system and I believe they don't need any further instructions.
GUI on the other hand, is built for everyday use cases.

### What does it mean for a password to be "pwned"?
It means that the password has been compromised in a data breach; aka it's not safe at all. See [Definition of Pwned](https://www.urbandictionary.com/define.php?term=pwned)

**Turing's Wrath** uses pwnedpasswords's lookup_pwned_api to verify that the generated password has not been pwend before. If a specific password turns out to be pwned, the program throws an error and terminates the running process.

### Why should my password length be more than 6 characters?
***TL;DR**: It's much safer this way
\
The answers lies is in discrete mathematics. **Turing's Wrath** random passwords are constructed by permutations of 87 characters: 26 lower case + 26 upper case + 25 symbols + 10 digits. Let's assume that you want to generate a password of length 3, here is a visualizations of the problem:
![87cubed](https://user-images.githubusercontent.com/39483396/73982598-c7b21b00-4949-11ea-9c97-fbd5ac4942a0.png)
Multiplication principle of combinatorics states that if you want to arrange n things in m possible way while repetition is allowed, there are _n^m_ ways to do so. Thus there will be 87^3 = 658,503 possible permutations for a password of length 3. If a brute force attack guesses 1 permutation in 1 second, it will take 658,503 seconds untill it finds the correct permutation. 
\
However, the number of permutations grow exponentially with length. Let's see how many possible permutations are there for a length = 4:
![87quadred](https://user-images.githubusercontent.com/39483396/73984259-8885c900-494d-11ea-945b-70dc3b612574.png)
Thus for the minimum length (6), number of possible permutations will be 433,626,201,009. That's a pretty long number but considering that computers are able to perform millions of computations in milliseconds, that's still weak. Most common way an attacker would use to crack a password is to use a "Dictionary Attack"; in which a computer program runs over pwned passwords in a database. This may not work smoothly in random passwords but if you use the same one for every platform and it gets pwned in one of them, that'll be added to the database, too.
