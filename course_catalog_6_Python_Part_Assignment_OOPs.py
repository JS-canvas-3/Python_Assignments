class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} Credit Hours)"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        requirement = "Required" if self.required_for_major else "Not Required"
        return f"{super().display_info()} - {requirement} for Major"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        return f"{super().display_info()} - Elective Type: {self.elective_type}"


if __name__ == "__main__":
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("ART205", "Economics", 2, "Indian financial era")

    print(core_course.display_info())
    print(elective_course.display_info())