print"Enter the number for the program you want to run\n"
option=int(raw_input("press 1 for student to teacher\npress 2 for battleship\npress 3 for exam statistics\n"))
if option==1:
    import students_to_teacher #to import student to teacher script
elif option==2:
    import battleship        #to import battleship script
elif option==3:
    import exam_stats           #to import exam statistics script
else:
    print "invalid choice"

