# Passwort Generator in the Terminal

This Passwort Generator generates a password which uses random figures retrieved with an API from random.org so the numbers are not produced in a deterministic way.
To avoid sending the password throught the internet and putting it at risk for an interception the generator is using the random figures to create the password based on string list created by the string.printable methode.

The first part of the program checks is a quota check. The Quota Checker allows you to examine your quota at any point in time. The quota system works on the basis of IP addresses. Each IP address has a base quota of 1,000,000 bits. When your client makes a request for random numbers (or strings, etc.), the server deducts the number of bits it took to satisfy your request from the quota associated with your client's IP address.

The second part establishes the list with stings and retrieves the random numbers from random.org.

Last but not at least, the last part is building the password based on the length the user desired which is a combination of random numbers and random characters.
