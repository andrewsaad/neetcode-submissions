class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_deq = deque(students)
        sand_deq = deque(sandwiches)

        attempt = 0
        while len(student_deq) and attempt < len(student_deq) :
            if student_deq[0] == sand_deq [0]:
                student_deq.popleft()
                sand_deq.popleft()
                attempt = 0
            else:
                poped_student = student_deq.popleft()
                student_deq.append(poped_student)
                attempt +=1

        return len(student_deq)
