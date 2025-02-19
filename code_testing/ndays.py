# calculate number of days
def numOfDays(date1, date2):
  #check which date is greater to avoid days output in -ve number
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days

