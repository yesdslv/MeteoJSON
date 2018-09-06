import json
import re




def meteoToList(informationBlock):
    meteo = {}
    ib = informationBlock.split(",")
    dateBlock = ib[0]
    ib = ib[1:]                                                     #Remove data block, leave meteo blocks
    if dateBlock == "01":
        if len(ib) == 10:                                           #First data block should contain 
            descriptionList = ["VV", "NO","NB", "CH",               # 10 meteo data for mountain stations
                               "CM", "Ch", "c12",                   # 9 for regular stations
                               "c13", "H", "A"]
            meteo = dict(zip(descriptionList, ib))
        elif len(ib) > 10:
            print("More data")
        elif len(ib) < 10:
            print("Less data")   
           

    return meteo
    
    
#Generates JSON file based on text from climatological file
def writeJSON(text, mYY):
    datajson = []
    text = re.sub('\n', '', text)                                   #Remove special character '\n' from Meteo text
    observations = text.split('((')                                 #Split text to observations
    length = len(observations)
    observations = observations[1:length-1:]                        #Remove first and last elements in observations
                                                                    #first element is attribute element
#    print(observations[2])
    
    for ob in observations:
        informationBlocks = ob.split("=")
        dateBlock = informationBlocks[0]                        #Get date from the first block ((ДД, tt
        print(dateBlock)
        informationBlocks = informationBlocks[1:]
#        print(informationBlocks)
        header = {"Date" : dateBlock,
                  "CodedData" : informationBlocks[0:]}
        for ib in informationBlocks:
            #print(ib.split(","))
            datablock = meteoToList(ib)
            z = header.copy()                                   #Operations for 
            header.update(datablock)                            #merging header dict and decoded data dict
        datajson.append(header)
        
    with open('data.txt', 'w') as outfile:
        json.dump(datajson, outfile, indent=4)     



with open("S4866130.518", encoding="latin1") as datafile:
    print("START")
    text = datafile.read()
    writeJSON(text, "518")
    datafile.close()
    print("DONE")

