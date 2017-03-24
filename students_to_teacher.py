lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total


# Add your function below!
def get_average(students):
    homework = average(students["homework"])
    quizzes = average(students["quizzes"])
    tests = average(students["tests"])
    return average(students["homework"]) * 0.1 + average(students["quizzes"]) * 0.3 + average(students["tests"]) * 0.6
    print get_letter_grade(lloyd)


def get_class_average(students):
    results = []
    for a in students:
        get_average(a)
        results.append(get_average(a))
    return average(results)


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


students = [lloyd, alice, tyler]
print "class average: ", get_class_average(students)
print "class grade: ", get_letter_grade(get_class_average(students))

