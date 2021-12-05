# Passwort Generator

This Passwort Generator generates a password which uses random figures retrieved with an API of random.org so the numbers are not produced in a deterministic way.
To avoid sending the password throught the internet and putting it at risk for an interception the generator is using the random figures to create the password based on string list created by the string.printable methode.
