# -*- coding: utf-8 -*-


from pattern.de import gender, MALE, FEMALE, NEUTRAL, parse, split
from pattern.vector import Document
print ("Gender Katze="+gender('Katze'))

s = parse('Die Katze liegt auf der Matte.')
print(s)
for sentence in split(s):
	print (sentence)

for word in sentence.words:
	print (word.part_of_speech+" : "+word.string)

from pattern.vector import Document

s = '''
	The shuttle Discovery, already delayed three times by technical problems 
	and bad weather, was grounded again Friday, this time by a potentially 
	dangerous gaseous hydrogen leak in a vent line attached to the shipʼs 
    external tank. The Discovery was initially scheduled to make its 39th 
	and final flight last Monday, bearing fresh supplies and an intelligent 
    robot for the International Space Station. But complications delayed the 
    flight from Monday to Friday,  when the hydrogen leak led NASA to conclude 
    that the shuttle would not be ready to launch before its flight window 
    closed this Monday.
'''
d = Document(s, threshold=1)
print(d.keywords(top=6))