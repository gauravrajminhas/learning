import statistics

## This is a module NOT a iPY notebook ! 


## FILENAME = "Darius-13-100m-Fly.txt"
## FOLDERNAME = "C:\\Users\\gaurav\\Dropbox\\Python Programming\\headfirst\\swimdata\\"

# this is a Global function as this is defined outside of a class 
# Thus, this method can be called with out a object referance

def read_swim_data (FOLDERNAME: str, FILENAME: str):

    swimmer, age, distance, stroke = FILENAME.removesuffix(".txt").split("-")

    with open(FOLDERNAME + FILENAME) as fileObject:
        allLines = fileObject.readline().strip()

    timeSTRList = allLines.split(",")
    timeINTList = []

    for times in timeSTRList:
        ## Check to see is there are Minutes in the Code
        if ":" in times:
            minutes, seconds = times.split(":")
            seconds, miliSeconds = seconds.split(".")
            timeINTList.append (int(minutes)*60 *100 +int(seconds)*100+int(miliSeconds))
            
        ## If not minutes then Process only Seconds and milliseconds 
        else:
            seconds, miliSeconds = times.split(".")
            timeINTList.append (int(seconds)*100+int(miliSeconds))

    avg = statistics.mean(timeINTList)

    minutes = int(avg//(60*100))
    seconds, miliSeconds = str(round(avg/100 ,2)).split(".")
    seconds = int(seconds) - minutes*60

    avgSTR = str(minutes) +":"+str(seconds)+ "."+ str(miliSeconds)


    #return timeSTRList,timeINTList
    return swimmer, age, distance, stroke, timeSTRList, avg, avgSTR