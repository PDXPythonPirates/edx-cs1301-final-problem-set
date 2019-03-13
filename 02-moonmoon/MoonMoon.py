# A common meme on social media is the name generator. These
# are usually images where they map letters, months, days,
# etc. to parts of fictional names, and then based on your
# own name, birthday, etc., you determine your own.
#
# For example, here's one such image for "What's your
# superhero name?": https://i.imgur.com/TogK8id.png
#
# Write a function called generate_name. generate_name should
# have two parameters, both strings. The first string will
# represent a filename from which to read name parts. The
# second string will represent an individual person's name,
# which will always be a first and last name separate by a
# space.
#
# The file with always contain 52 lines. The first 26 lines
# are the words that map to the letters A through Z in order
# for the person's first name, and the last 26 lines are the
# words that map to the letters A through Z in order for the
# person's last name.
#
# Your function should return the person's name according to
# the names in the file.
#
# For example, take a look at the names in heronames.txt
# (look in the drop-down in the top left). If we were to call
# generate_name("heronames.txt", "Addison Zook"), then the
# function would return "Captain Hawk": Line 1 would map to
# "A", which is the first letter of Addison's first name, and
# line 52 would map to "Z", which is the first letter of
# Addison's last name. The contents of those lines are
# "Captain" and "Hawk", so the function returns "Captain Hawk".
#
# You should assume the contents of the file will change when
# the autograder runs your code. You should NOT assume
# that every name will appear only once. You may assume that
# both the first and last name will always be capitalized.
#
# HINT: Use chr() to convert an integer to a character.
# chr(65) returns "A", chr(90) returns "Z".


# Add your code here!


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
# each on their own line.
print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))
print(generate_name("heronames.txt", "Matt Phillips"))
print(generate_name("heronames.txt", "David Mev"))
print(generate_name("heronames.txt", "Chris Thom"))
