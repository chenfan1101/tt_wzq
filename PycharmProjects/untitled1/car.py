
class car():
    def __init__(self,licheng,youxiang,describle):
        self.licheng = licheng
        self.youxiang = youxiang
        self.describle = describle


    def describles(self):

        print("汽车的里程为{0},续航为{1},{2}".format(self.licheng,self.youxiang,self.describle))


    def xingshi(self,licheng,youxiang):
        self.licheng +=licheng
        if self.youxiang>youxiang:
            self.youxiang -=youxiang

    def descs(self):
        print("汽车的里程为{0},续航为{1},{2}".format(self.licheng, self.youxiang, self.describle))






