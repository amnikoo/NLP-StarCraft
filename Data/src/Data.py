from bs4 import BeautifulSoup
import requests
import re
import os
def GameDialogues(url):
    HumanNameList = ["Arcturus Mengsk", "Sarah Kerrigan", "Jim Raynor",
                      "Alexei Stukov", "Gerard DuGalle", "Edmund Duke",
                      "Kerrigan", "Computer", "Mengsk",
                      "Tychus Findlay", "Raynor", "Adjutant", "Findlay",
                      "Matt Horner", "Horner", "Donny Vermillion",
                      "Female Reporter #1", "Female Reporter #2", "Female Reporter #3",
                      "Male Reporter", "Valerian Mengsk", "Valerian",
                      "Milo Kachinsky", "Rory Swann", "Swann", "Kachinsky",
                      "Horace Warfield", "Warfield", "Arcturus", "Dominion Marine",
                      "Infested Kerrigan", "Gabriel Tosh", "Keno", "Liberty",
                      "Vermillion", "Female Reporter", "Lockwell", "Tosh",
                      "Hyperion crewman", "Kate Lockwell", "Dominion Lieutenant",
                      "Stukov"]
    NotHumanNameList = ["The Overmind", "Aldaris", "Tassadar", "Zeratul",
                        "Fenix", "Samir Duran", "Protoss Preserver",
                        "Izsha", "Lasarra", "Dr. Emil Narud", "False Kerrigan",
                        "Artanis", "Archon", "Zealots", "Selendis", "Amon",
                        "Karax", "Hybrid", "Zealot",
                        "Vorazun", "Alarak", "Ma'lash", "Narud", "Ouros"]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    temp=soup.find_all("dd")
    
    Human = open("../Human.txt", 'w')
    NotHuman = open("../NotHuman.txt", 'w')
    
    for line in temp:
        if(type(line) != "NoneType"):
            MatchLine = re.match("(.+):\W(\[.+\]\W)?(.+)", line.get_text())
            if MatchLine:
                if(MatchLine.groups()[0] in HumanNameList):
                    Human.write(MatchLine.groups()[2]+"\n")
                elif(MatchLine.groups()[0] in NotHumanNameList):
                    NotHuman.write(MatchLine.groups()[2]+"\n")

    Human.close()
    NotHuman.close()

def UpdateGameDialogues(url):
    HumanNameList = ["Kerrigan", "Arcturus"]
    NotHumanNameList = ["Zeratul", "Izsha", "Zagara", "Abathur", "Brakk", "Ancient One",
                        "Zurvan", "Yagdra", "Dehaka", "Kraith", "Slivan"]

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    temp=soup.find_all("li")

    Human = open("../Human.txt", 'a')
    NotHuman = open("../NotHuman.txt", 'a')

    for line in temp:
        if(type(line) != "NoneType"):
            MatchLine = re.match("(.+):\W(\[.+\]\W)?(.+)", line.get_text())
            if MatchLine:
                if(MatchLine.groups()[0] in HumanNameList):
                    Human.write(MatchLine.groups()[2]+"\n")
                elif(MatchLine.groups()[0] in NotHumanNameList):
                    NotHuman.write(MatchLine.groups()[2]+"\n")

url="https://en.wikiquote.org/wiki/StarCraft"
GameDialogues(url)
url="https://starcraft.fandom.com/wiki/StarCraft_II:_Heart_of_the_Swarm_campaign_quotations/Zerus_Missions"
UpdateGameDialogues(url)

