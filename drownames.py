#!/usr/bin/python2

import random

# Prefix format is (Female, Male, Common). Should be an adjective or verb.
given_prefixes = [
        ("Akor","Alak", "Beloved"),
        ("Alaun","Alton", "Lightning"),
        ("Aly","Kel", "Singing"),
        ("Ang","Adin", "Beastly"),
        ("Ardul","Amal", "Blessed"),
        ("Aun", "Ant", "Crypt"),
        ("Bae", "Bar", "Fated"),
        ("Bal", "Bel", "Burning"),
        ("Belar", "Bruh", "Dart"),
        ("Briz", "Berg", "Graceful"),
        ("Chal", "Chasz", "Earth"),
        ("Char", "Kron", "Sickened"),
        ("Chess", "Cal", "Noble"),
        ("Dhaun", "Dhaun", "Infested"),
        ("Dil", "Dur", "Cold"),
        ("Dirz", "Div", "Dream"),
        ("Dris", "Riz", "Ashen"),
        ("Eclave", "Elk", "Mad"),
        ("Elvan", "Kalin", "Elven"),
        ("Elv", "Elaug", "Drow"),
        ("Erel", "Rhyl", "Eye"),
        ("Ethe", "Erth", "Mithril"),
        ("Faer", "Selds", "Forsworn"),
        ("Felyn", "Fil", "Pale"),
        ("Filf", "Phar", "Treacherous"),
        ("Gauss", "Orgoll", "Dreaded"),
        ("G'eld", "G'eld", "Friendly"),
        ("Ghaun", "Ghaun", "Accursed"),
        ("Gin", "Din", "Beserk"),
        ("Grey", "Gul", "Ghostly"),
        ("Hael", "Hatch", "Marked"),
        ("Hal", "Sol", "Nimble"),
        ("Houn", "Rik", "Magical"),
        ("Iliv", "Dip", "Warrior"),
        ("Ilm", "Ilm", "Living"),
        ("Illiam", "Im", "Devoted"),
        ("In", "Sorn", "Enchanted"),
        ("Ilph", "Ilph", "Emerald"),
        ("Irae", "Ilzt", "Mystic"),
        ("Irr", "Izz", "Masked"),
        ("Iym", "Ist", "Immortal"),
        ("Jhan", "Duag", "Shielded"),
        ("Jhael", "Gel", "Ambitious"),
        ("Jys", "Driz", "Steel"),
        ("Lael", "Llt", "Iron"),
        ("Lar", "Les", "Bound"),
        ("Lineer", "Mourn", "Legendary"),
        ("Lird", "Ryld", "Slave")]

#format is (female, male, common). Should be a noun.
given_suffixes = [
        ("Lua", "Lyme", "Crystal"),
        ("Mal", "Malag", "Secret"),
        ("May", "Mas", "Beauty"),
        ("Micar", "Micar", "Poison"),
        ("Min", "Ran", "Second"),
        ("Mol", "Go", "Storm"),
        ("Myr", "Nym", "Skeleton"),
        ("Nath", "Mer", "Doom"),
        ("Ned", "Nad", "Mind"),
        ("Nihil", "Nal", "Horror"),
        ("Neer", "Neer", "Core"),
        ("Null", "Nil", "Tear"),
        ("Olor", "Omar", "Tattoo"),
        ("Pellan", "Relon", "North"),
        ("Phaer", "Vorn", "Honour"),
        ("Phyr", "Phyx", "Blessing"),
        ("Qualn", "Quil", "Ocean"),
        ("Quar", "Quar", "Time"),
        ("Quav", "Quev", "Friend"),
        ("Qil", "Quil", "Foe"),
        ("Rauv", "Welv", "Cave"),
        ("Ril", "Ryl", "Omen"),
        ("Sabal", "Szor", "Amber"),
        ("Sab", "Tsab", "Void"),
        ("Shi'n", "Kren", "Fool"),
        ("Shri", "Ssz", "Silk"),
        ("Shur", "Shar", "Dagger"),
        ("Shynt", "Shynt", "Invisible"),
        ("Sin", "Szin", "Festival"),
        ("Ssap", "That", "Night"),
        ("Susp", "Spir", "Wisdom"),
        ("Talab", "Tluth", "Fire"),
        ("Tal", "Tar", "Love"),
        ("Triel", "Taz", "Bat"),
        ("T'riss", "Teb", "Sword"),
        ("Ulviir", "Uhls", "Treasure"),
        ("Umrae", "Hurz", "Truth"),
        ("Vas", "Vesz", "Body"),
        ("Vic", "Vic", "Abyss"),
        ("Vier", "Val", "Darkness"),
        ("Vlon", "Wod", "Hero"),
        ("Waer", "Wehl", "Depths"),
        ("Wuyon", "Wruz", "Abased"),
        ("Xull", "Url", "Ruby"),
        ("Xun", "Xun", "Fiend"),
        ("Yas", "Yaz", "Riddle"),
        ("Zar", "Zakn", "Shadow"),
        ("Zes", "Zez", "Ancient"),
        ("Zilv", "Vuz", "Forgotten")]

def add_given_prefix(female, male, common, prng):
    (female2, male2, common2) = prng.choice(given_prefixes)
    female.append(female2.lower())
    male.append(male2.lower())
    common.append(common2)

def add_given_suffix(female, male, common, prng):
    (female2, male2, common2) = prng.choice(given_suffixes)
    female.append(female2.lower())
    male.append(male2.lower())
    common.append(common2)


def given_name(prng=random.Random() ):
    n = prng.randint(1,10)
    
    male = []
    female = []
    common = []

    if n < 10:
        add_given_prefix(female, male, common, prng)
        common.append("-")
        add_given_suffix(female, male, common, prng)
    else:
        add_given_suffix(female, male, common, prng)
        common.append("-")
        add_given_prefix(female, male, common, prng)

    if n < 4:
        return (female, male, common)

    if n < 6:
        common.append("-")
        add_given_suffix(female, male, common, prng)
        return (female, male, common)

    if n < 8:
        common.append("-")
        female.append("'")
        male.append("'")
        add_given_suffix(female, male, common, prng)
        return (female, male, common)

    if n < 10:
        common.append(" ")
        female.append(" ")
        male.append(" ")
        (female2, male2, common2) = given_name(prng)
        female.extend(female2)
        male.extend(male2)
        common.extend(common2)
        return (female, male, common)

    else:
        common.append("-")
        add_given_prefix(female, male, common, prng)
        return (female, male, common)

house_prefix = [
        ("Alean", "The noble line of"),
        ("Ale", "Traders in"),
        ("Arab", "Daughters of"),
        ("Arken", "Mages of"),
        ("Auvry", "Blood of the"),
        ("Baen", "Blessed by"),
        ("Barri", "Spawn of"),
        ("Cladd", "Warriors from"),
        ("Desp", "Victors of"),
        ("De", "Champions of"),
        ("Do'", "Walkers in"),
        ("Eils", "Lands of"),
        ("Everh", "The cavern of"),
        ("Fre", "Friends to"),
        ("Gode", "Clan of"),
        ("Helvi", "Those above"),
        ("Hla", "Seers of"),
        ("Hun", "The sisterhood of"),
        ("Ken", "Sworn to"),
        ("Kil", "People of"),
        ("Mae", "Raiders from"),
        ("Mel", "Mothers of"),
        ("My", "Honoured of"),
        ("Noqu", "Sacred to"),
        ("Orly", "Guild of"),
        ("Ouss", "Heirs to"),
        ("Rilyn", "House of"),
        ("Teken'", "Delvers in"),
        ("Tor", "Mistresses of"),
        ("Zau", "Children of")]

house_suffix = [
        ("afin", "The Web"),
        ("ana", "The night"),
        ("ani", "The widow"),
        ("ar", "Poison"),
        ("arn", "Fire"),
        ("ate", "The way"),
        ("ath", "the dragons"),
        ("duis", "the whip"),
        ("ervs", "the depths"),
        ("ep", "the underdark"),
        ("ett", "magic"),
        ("ghym", "the forgotten ways"),
        ("iryn", "history"),
        ("lyl", "the blade"),
        ("mtor", "the abyss"),
        ("ndar", "black hearts"),
        ("neld", "the arcane"),
        ("rae", "fell powers"),
        ("rahel", "the gods"),
        ("rret", "the void"),
        ("sek", "adamantium"),
        ("th", "challenges"),
        ("tlar", "mysteries"),
        ("t'tar", "victory"),
        ("tyl", "the pits"),
        ("und", "the spider's kiss"),
        ("urden", "the darkness"),
        ("val", "silken weaver"),
        ("virr", "dominance"),
        ("zynge", "the ruins")]

def house_name(prng=random.Random() ):
    drowb = []
    commonb = []

    (drow, common) = prng.choice(house_prefix)
    drowb.append(drow)
    commonb.append(common)

    (drow, common) = prng.choice(house_suffix)
    drowb.append(drow.lower())
    commonb.append(" "+common)

    return (drowb, commonb)

def full_name(prng=random.Random() ):
    (first_female, first_male, first_common) = given_name(prng)
    (house_drow, house_common) = house_name(prng)

    return flatten(first_female).title() + " (male: "+flatten(first_male).title() + ") "+ flatten(house_drow).title() + ", "+ flatten(first_common).title() + " of " + flatten(house_common).title()

def flatten(l):
    return ''.join(l)

# Check there are 3 elements to every tuple in the list.
def verify(l):
    for k in l:
        try:
            assert len(k) == 3
        except AssertionError:
            print "Invalid element:"+str(k)


if __name__ == '__main__':
    verify(given_prefixes)
    verify(given_suffixes)
    for _ in range (20):
        print full_name()

