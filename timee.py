class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hr=hour
        self.min=minute
        self.sec=second
    def __add__(self,other):
        secs=(self.sec+other.sec)%60
        sec_balance=(self.sec+other.sec)//60

        mins=(sec_balance+(self.min+other.min))%60
        min_balance=(self.min+other.min)//60

        hours=(min_balance+(self.hr+other.hr))
        time2=time(hours,mins,secs)

        return time2
    def gettime(self):
        timeformat=lambda x: str(x) if x>9 else "0"+str(x) if x>0 else "00"
        print(f"{timeformat(self.hr)}:{timeformat(self.min)}:{timeformat(self.sec)}")

t1=time(23,10,30)
t2=time(13,45,30)
t3=t1+t2
t3.gettime()