from student_grade import calculate_average, calculate_grade
def test_average():
    assert calculate_average([90, 80, 70]) == 80

def test_grade_s():
    assert calculate_grade(95) == "S"

def test_grade_a():
    assert calculate_grade(85) == "A"

def test_grade_b():
    assert calculate_grade(70) == "B"

def test_grade_c():
    assert calculate_grade(55) == "C"


def test_grade_d():
    assert calculate_grade(45) == "D"


def test_grade_f():
    assert calculate_grade(30) == "F"


def test_grade_boundary():
    assert calculate_grade(90) == "S"
    assert calculate_grade(80) == "A"
    assert calculate_grade(65) == "B"
    assert calculate_grade(50) == "C"
    assert calculate_grade(40) == "D"