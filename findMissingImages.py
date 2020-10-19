#!/usr/bin/python3
import sys
import os
import glob
import re

characterName=['Alma','Anna','April','Ashley','Candice','Chris','Cindy','Donald','Erin','Fair','Hillary','Hope','Iida''','Jillian','Kayla','Main','Megan','Melina','Michelle','Mike','Miya','Nelson','Nicole','Olivian','Reina','Sakajou','Shreya','Taylor','Trista','Vanessa','Will','Zoey','Amber','Aprika','Arelia','Betty','Chastity','Ciel','Dilbert','Eliza','Ermach','Fwoman','Hoover','Howard','Jaina','Jennifer','Karyn','Kenichi','Martha','Megumi','Melody','Mika','Misc','Mother','Nick','Nurse','Peter','Ruby','Sean','Silease','Tim','Tristen','Waitress','Yukina']
storyName="E:/download/stuff/Games/Press-Switch/Press-Switch-Stitch/.5c/game/story/ElizaPath.rpy"
missingImage="E:/download/stuff/Games/Press-Switch/Press-Switch-Stitch/.5c/game/story/missing.txt"
imageDirectory="E:/download/stuff/Games/Press-Switch/Press-Switch-Stitch/.5c/game/Characters/"

def compareCharacterDirectory(characterName):
    
    storyNameOpen = open(storyName, "r", errors='ignore')
    storyNameLine = storyNameOpen.readlines()
    for i in storyNameLine:
        #print(str(storyNameLine.index(i)+1) + " " + i)

        for j in characterName:
            pattern = r'^.*show ' + str.lower(j) + '.[0-9].$'
            #print(pattern)
            findCharacter = re.search(pattern, i)
            if findCharacter:
                print(i)
                if os.path.exists(imageDirectory + j + i):
                    print(i + " exists")


def main(argv):
    compareCharacterDirectory(characterName)

if __name__ == "__main__":
  main(sys.argv[1:])