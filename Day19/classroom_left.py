class Classroom:
    classroom=["a","b","c"]
    @staticmethod 
    def search_classroom(class_room):
        classroom=classroom.lower()
        if(classroom in Classroom.classroom):
            return "Found" 
        else:
            return -1 
print(Classroom.search_classroom("a"))
