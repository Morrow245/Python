import time
class TrafficLight:
    __color: str = ['Red', 'Yellow', 'Green']

    def running(self):
        if TrafficLight.__color[0] == 'Red' and TrafficLight.__color[1] == 'Yellow' and TrafficLight.__color[2] == 'Green':
            i = 0
            while i < 3:
                print(TrafficLight.__color[i])
                if i == 0:
                    time.sleep(7)
                elif i == 1:
                    time.sleep(2)
                elif i == 2:
                    time.sleep(5)
                i += 1
        else:
            print("Порядок переключения режимов светофора нарушен!")
trafficlight = TrafficLight()
trafficlight.running()