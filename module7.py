# inititial data containing room numbers for courses
# Key: Course number, Value: Room Number
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# inititial data containing instructors for courses
# Key: Course number, Value: Instructor
course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# inititial data containing course times for courses
# Key: Course number, Value: Course time
course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Returns tuple of room#, instructor, time for a given course_number
def get_course_info(course_number):
    return (
        course_rooms[course_number],
        course_instructors[course_number],
        course_times[course_number],
    )

# This program requests a course number from the user 
# and prints the room number, instructor, and time information
# for that course
def main():

    # Request course information
    course_number = input("Please enter course number to view: ")
    try:
        # Try to print course information, error is thrown if
        # course number is invalid
        room, instructor, time = get_course_info(course_number)
        print(f"\nCourse Information for course {course_number}")
        print(f"Room Number: {room}")
        print(f"Room Number: {instructor}")
        print(f"Room Number: {time}")

    # Handle the case where course number is invalid
    except Exception as error:
        print(f"You entered an invalid or non-existant course number ({course_number}). {error}")
    
   
if __name__ == "__main__":
    main()

