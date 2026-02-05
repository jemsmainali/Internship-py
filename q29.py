"""
 Create a class Time with three instance variables hours, minutes, and seconds. Add instance
methods display() to display the time in hh:mm:ss format and add() to add two time objects.
Use this class to add and display two different time objects.
"""

#Answer
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        tot1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        tot2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        total = tot1 + tot2

        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = total  % 60

        return Time(hours, minutes, seconds)


if __name__ == "__main__":
   h1 = int(input("Enter hours for time1: "))
   m1 = int(input("Enter minutes for time1: "))
   s1 = int(input("Enter seconds for time1: "))
   time1 = Time(h1, m1, s1)
   print("Time1: ", end="")
   time1.display()

   h2 = int(input("Enter hours for time2: "))
   m2 = int(input("Enter minutes for time2: "))
   s2 = int(input("Enter seconds for time2: "))
   time2 = Time(h2, m2, s2)
   print("Time2: ", end="")
   time2.display()

   sum_of_times = time1.add(time2)
   print("Sum of times: ", end="")
   sum_of_times.display()





