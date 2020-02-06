# SHARPEN
With the daily rise of the Web 2.0, we find ourselves in need of new user accounts and more secure passwords. However, keeping these accounts information is always a pain in the ass. You might want to write your account information on a paper (which is way better than digital storages) but that's not the only problem. **How do you make sure your password is as strong as possible?** if you're not sure, then it doesn't matter how you keep it safe. Your password is the heart of your web immunity and SHARPEN is build to protect it.

# FAQs
### What is it?
SHARPEN is an open-source app developed for generating random passwords. It uses Secure Hashing Algorithm (SHA) and other third-party APIs to make sure the generated passwords (although impossible) doesn't collide with _pwned_ passwords.

### How do I use it?
SHARPEN comes in two versions: **CLI** (command line interface) and **GUI** (graphical user interface).
CLI version is suitable for users experienced with Unix-Linux based system and I believe they don't need any further instructions.
GUI on the other hand, is built for everyday use cases.

### What does it mean for a password to be "pwned"?
It means that the password has been compromised in a data breach; aka it's not safe at all. Here is the definition of *pwned* for boomers: https://www.urbandictionary.com/define.php?term=pwned

SHARPEN uses pwnedpasswords's lookup_pwned_api to verify that the generated password has not been pwend before. If a specific password turns out to be pwned, the program throws an error and terminates the running process.

### Why can't I copy and paste the generated passwords in GUI version?
Every time you copy a piece of text, your computer saves it on a memory block, this has its own risks and vulnerabilities. The desktop application is designed that way to prevent any malicious attacks targeting random access memory.

### Why should my password length be more than 6 characters?
