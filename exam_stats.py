grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# to print grades
def print_grades(grades):
    for grade in grades:
        print grade

#function to find sum of grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


#function to find average of grades
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average


#function to find variance of grades
def grades_variance(scores):
    variance = 0
    average = grades_average(scores)
    for score in scores:
        variance += (score - average) ** 2
    variance = variance / float(len(scores))
    return variance


#function to find standard deviation of grades
def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)

print "grades are: \n", print_grades(grades)
print "sum of grades:", grades_sum(grades)
print "avrage of grades:", grades_average(grades)
print "grade variancee:", grades_variance(grades)
print "standard deviation: ", grades_std_deviation(variance)
