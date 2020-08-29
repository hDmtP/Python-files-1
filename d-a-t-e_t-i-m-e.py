import datetime
x = datetime.datetime.now()

print(x.year)                                
                                                         # %a -----> Sat
                                                         # %A -----> Saturday
                                                         # %b -----> Aug
                                                         # %B -----> August
                                                         # %m -----> <month as number> 08
                                                         # %W -----> <week day as number per year> 30 !!!!!! 
                                                         # %w -----> <week day as number> 06 [Saturday]
                                                         # %d -----> <day of month> 01
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%W"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x)
# print(now.day)
# print(now.hour)
# print(now.year)




                                                         # %a -----> Sat
                                                         # %A -----> Saturday
                                                         # %b -----> Aug
                                                         # %B -----> August
                                                         # %m -----> <month as number> 02
                                                         # %W -----> <week of Year> 08
                                                         # %w -----> <week day as number>
                                                         # %d -----> <day of month>