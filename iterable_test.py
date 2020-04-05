from datetime import timedelta, date

class DateRangeIterable:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

for day in DateRangeIterable(date(2020, 1, 1), date(2020, 1, 5)):
    print(day) 

r = DateRangeIterable(date(2020, 1, 1), date(2020, 1, 5))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
# print(next(r))

print(r[1]) #error