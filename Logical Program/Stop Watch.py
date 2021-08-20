"""
*Author : Guruprasanth
*Date   : 20-08-2021
*Time   : 4-15 PM
*Title  :Stop watch Hour : Min : Sec
"""
import time

class StopWatch:
  @staticmethod
  def timeConvert(Sec):
    Mins = Sec // 60
    Sec = Sec % 60
    Hours = Mins // 60
    Mins = Mins % 60
    print("Time Lapsed - Hour({0}):Min({1}):Sec({2})".format(int(Hours), int(Mins), Sec))

input("Enter The Start Time:")
start_time = time.time()
input("Enter The Stop Time:")
end_time = time.time()
time_lapsed = end_time - start_time
stopWatch = StopWatch()
stopWatch.timeConvert(time_lapsed)