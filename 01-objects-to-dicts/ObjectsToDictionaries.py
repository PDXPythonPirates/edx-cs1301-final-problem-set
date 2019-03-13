# To help streamline certain development activities, ISO
# (the International Organization for Standardization) provides
# a table of codes, short abbreviations, and long abbreviations
# for every nation in the world. We have created a class called
# Nation to structure this information. The Nation class
# contains 6 attributes:
#
# - short_name: The short, common form of a country's name,
#   such as "Albania".
# - long_name: The long, official form of a country's name,
#   such as "Republic of Albania".
# - iso_code: The numeric code corresponding to the nation,
#   such as 8.
# - iso_short: The short abbreviation corresponding to the
#   nation, such as AL.
# - iso_long: The long abbreviation corresponding to the
#   nation, such as ALB.
# - capital: The capital city, such as Tirana.
#
# To let you debug, we've provided you the class here. Your
# code will have access to this.


class Nation:
    def __init__(self, short_name, long_name, iso_code, iso_short, iso_long, capital):
        self.short_name = short_name
        self.long_name = long_name
        self.iso_code = iso_code
        self.iso_short = iso_short
        self.iso_long = iso_long
        self.capital = capital

# Write a function called to_dictionaries that will take as
# input a list of instances of this class. It should return a
# dictionary of dictionaries. The keys for the dictionaries
# should be the short names of the nations. The values should
# be additional dictionaries, each with five keys: long_name,
# iso_code, iso_short, iso_long, and capital.
#
# For example, if we created two instances of Nation like this:
#new_nation_1 = Nation("Albania", "Republic of Albania", 8, "AL", "ALB", "Tirana")
#new_nation_2 = Nation("Angola", "Republic of Angola", 24, "AO", "AGO", "Luanda")
#
# ...then made them into a list like this:
#nation_list = [new_nation_1, new_nation_2]
#
# ...then called the function:
#new_dict = to_dictionaries(nation_list)
#
# ...then we would get this dictionary in return:
# {"Albania": {"long_name": "Republic of Albania", "iso_code": 8, "iso_short": "AL", "iso_long": "ALB", "capital": "Tirana"},
# "Angola": {"long_name": "Republic of Angola", "iso_code": 24, "iso_short": "AO", "iso_long": "AGO", "capital": "Luanda"}}
#
# HINT: This problem looks long, but don't overcomplicate
# it. Each part is something you've done lots of times:
# iterate through a list of instances, get the key, create
# a new dictionary, add the other key-values one-by-one,
# and return the overall dictionary.


# Add your code here!


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary) the
# sample dictionaries shown in the directions.
new_nation_1 = Nation("Albania", "Republic of Albania",
                      8, "AL", "ALB", "Tirana")
new_nation_2 = Nation("Angola", "Republic of Angola",
                      24, "AO", "AGO", "Luanda")
nation_list = [new_nation_1, new_nation_2]
print(to_dictionaries(nation_list))
