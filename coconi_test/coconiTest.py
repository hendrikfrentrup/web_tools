class coconiTest(object):
    
    def __init__(self):
        self.htmlString=""
        
    def setHTMLstring(self, textString):
        self.htmlString=textString

    def parseExtString(text = ""):
        import time as tm
        time=[]
        bpm=[]
        speed=[]
        if text:
            lines=text.split("\n")
            for line in lines:
                temp=line.split("             ")
                time.append(tm.strptime(temp[0][:5], "%M:%S"))
                bpm.append(int(temp[1]))
                speed.append(float(temp[2]))
        return time, bpm, speed
    
    def parseSelf(self):
        import time as tm
        time=[]
        bpm=[]
        speed=[]
        if self.htmlString:
            lines=self.htmlString.split("\n")
            for line in lines:
                temp=line.split("             ")
                time.append(tm.strptime(temp[0][:5], "%M:%S"))
                bpm.append(int(temp[1]))
                speed.append(float(temp[2]))
        self.time=time
        self.bpm=bpm
        self.speed=speed
        
    def analysis(self):
        import scipy.polyval, scipy.polyfit
