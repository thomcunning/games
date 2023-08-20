madlib_string = """One fine day, a properNOUN headed out the front door, down the street following the the smell of pNOUN, and ran into a practicing polka
band, \'The ADJ pNOUN\' (who only played covers.)
\'SONG_TITLE\'! yelled the peckish ____ and tossed the band a sNOUN, while eyeing a nearby sNOUN salesman.
After the band finished, the tuba player was so ADJ, she started VERBing a pretzel, until every square inch of sNOUN was covered with
mustard. The aroma of beer could be VERBed as far as the nose could VERB."""

#search the string for sNOUN pNOUN propNOUN ADJ VERB SONG_TITLE; when found ask user for input. store that in list.

sNOUN_ct = madlib_string.count('sNOUN')
pNOUN_ct = madlib_string.count('pNOUN')
properNOUN_ct = madlib_string.count('properNOUN')
ADJ_ct = madlib_string.count('ADJ')
VERB_ct = madlib_string.count('VERB')
SONG_TITLE_ct = madlib_string.count('SONG_TITLE')

snoun_list = []
pnoun_list = []
propernoun_list = []
adj_list = []
verb_list = []
song_title = []


for j in range(SONG_TITLE_ct):

    song_title.append(input('Enter any song title.\n'))

for j in range(properNOUN_ct):
    
    propernoun_list.append(input('Enter a proper noun.\n'))

for j in range(sNOUN_ct):
    
    snoun_list.append(input('Enter a singular noun.\n'))

for j in range(VERB_ct):

    verb_list.append(input('Enter an infinitive verb.\n'))

for j in range(pNOUN_ct):

    pnoun_list.append(input('Enter a plural noun.\n'))

for j in range(ADJ_ct):

    adj_list.append(input('Enter an adjective.\n'))


#output string with users inputs

print("""One fine day, {0} headed out the front door, down the street following the the smell of {1}, and ran into a practicing polka
band, \'The {2} {3}\' (who only played covers.) \'{4}\'! yelled the peckish {0} and tossed the band a {5}, while eyeing a nearby {6} salesman.
After the band finished, the tuba player was so {7}, she started {8}ing a pretzel, until every square inch of {9} was covered with
mustard. The aroma of beer could be {10}ed as far as the nose could {11}.
""".format(propernoun_list[0],pnoun_list[0],adj_list[0],pnoun_list[1],song_title[0],snoun_list[0],snoun_list[1],adj_list[1],verb_list[0],snoun_list[2],verb_list[1],verb_list[2]))
