# For Loop
for i in range(1, 6)
    print((i))
# The range is 1 to n-1 which is 6-1 or 5, This will print 1 2 3 4 5

#---------------------------------------------------------------------------

# While Loop
i = 1
while (i<6):
    print(i)
    i += 1
# This will print 1 to 5

#----------------------------------------------------------------------------
# Break
i = 1
while (i<6):
    print(i)
    i += 1
    if i == 3:
        break
# This will stop executing at 2 so it will only print 1 2
#-----------------------------------------------------------------------------

# Continue
i = 1
while (i<10):
    i += 1
    if i == 5:
        continue
    print(i)
# In this print statement is after the condition and continue will avoide the process after the continue
# so it will print 1 to 8 and will ignore 5
