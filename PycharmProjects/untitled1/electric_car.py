from car import car

class electric_car(car):
    def __init__(self,licheng,youxiang,describle,electric_licheng):
        super(electric_car,self).__init__(licheng,youxiang,describle)
        self.electric = electric_licheng

    #重写父类的方法
    def describles(self):
        print("汽车的里程为{0},续航为{1},{2}".format(self.licheng, self.electric, self.describle))
        return

    #重写父类的方法
    def xingshi(self,licheng,electric_licheng):
        self.licheng+=licheng
        self.electric -=electric_licheng



if __name__ == '__main__':
    ele = electric_car(0,100,"不怕奔驰和宝马，就怕大众带字幕",30)
    ele.xingshi(30,20)
    ele.describles()
    ele.descs()


