import json


def writeJSON(text):
    list = text.split('((')     #Split text to list
    length = len(list)
    list = list[1:length-1:]    #Remove first and last elements in list
    datajson = []
    with open('data.txt', 'w') as outfile:     
        for element in list:
            data = element.split("=")
            datajson.append({"Date" : data[0],
                             "Data" : data[1:]}
                            )
        json.dump(datajson, outfile)

with open("S4866130.518", encoding="latin1") as datafile:
    print("START")
    text = datafile.read()
    writeJSON(text)
    datafile.close()
    print("DONE")

