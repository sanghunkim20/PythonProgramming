from tkinter import *
import tkinter.ttk
from tkinter import messagebox

# 학번을 저장할 집합 (중복 체크용)
student_ids = set()

class Student:
    def __init__(self, id, major, name, k_score, e_score, m_score):
        self.id = id
        self.major = major
        self.name = name
        self.k_score = k_score
        self.e_score = e_score
        self.m_score = m_score

        self.sum = self.k_score + self.e_score + self.m_score
        self.avg = self.sum / 3.0
    
    def get(self):
        return [self.id, self.major, self.name, self.k_score, self.e_score, self.m_score, self.sum, self.avg]
    
# 학생 생성 함수
def add_student(tree, id, name, major, kor, eng, mat):
     # 학번이 집합에 있는지 확인
    if id.get() in student_ids:
        messagebox.showerror("에러", "이미 존재하는 학번입니다.")
        return
    
    new_student = Student(id.get(), major.get(), name.get(), int(kor.get()), int(eng.get()), int(mat.get())) # 학생 객체 생성
    tree.insert('', 'end', values=new_student.get()) # 트리 뷰에 추가
    student_ids.add(id.get())  # 집합에 학번 추가   

    # 입력창 초기화
    id.delete(0, tkinter.END)
    name.delete(0, tkinter.END)
    major.delete(0, tkinter.END)
    kor.delete(0, tkinter.END)
    eng.delete(0, tkinter.END)
    mat.delete(0, tkinter.END)
    
# 학생 삭제 함수
def delete_student(tree, del_id):
    student_id = del_id.get() # 삭제할 학생의 학번을 가져옴

    # 학번이 집합에 없으면 오류 메시지 출력
    if student_id not in student_ids:
        messagebox.showerror("에러", "존재하지 않는 학번입니다.")
        return
    
    # 삭제 확인 메시지 출력
    if messagebox.askyesno("경고", "정말 삭제하시겠습니까?"):
        for item in tree.get_children(): # 트리 뷰에서 학생을 찾아서 삭제
            if tree.item(item, 'values')[0] == student_id: # 학번이 일치하면 삭제
                tree.delete(item) # 트리 뷰에서 삭제
                student_ids.remove(student_id) # 집합에서 삭제
                del_id.delete(0, tkinter.END) # 입력창 초기화
                return

# GUI 생성
root = Tk()
root.title("학생 정보 관리")

# 학생 데이터 트리 뷰
tree = tkinter.ttk.Treeview(root, columns=("학번", "학과", "이름", "국어", "영어", "수학", "총점", "평균"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=70, anchor='center')

tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 학생 등록 폼
register_frame = tkinter.LabelFrame(root, text="신규 학생 등록")
register_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

tkinter.Label(register_frame, text="학번:").grid(row=0, column=0, sticky="e")
id = tkinter.Entry(register_frame)
id.grid(row=0, column=1)

tkinter.Label(register_frame, text="이름:").grid(row=1, column=0, sticky="e")
name = tkinter.Entry(register_frame)
name.grid(row=1, column=1)

tkinter.Label(register_frame, text="학과:").grid(row=2, column=0, sticky="e")
major = tkinter.Entry(register_frame)
major.grid(row=2, column=1)

tkinter.Label(register_frame, text="국어 성적:").grid(row=3, column=0, sticky="e")
kor = tkinter.Entry(register_frame)
kor.grid(row=3, column=1)

tkinter.Label(register_frame, text="영어 성적:").grid(row=4, column=0, sticky="e")
eng = tkinter.Entry(register_frame)
eng.grid(row=4, column=1)

tkinter.Label(register_frame, text="수학 성적:").grid(row=5, column=0, sticky="e")
mat = tkinter.Entry(register_frame)
mat.grid(row=5, column=1)

tkinter.Button(register_frame, text="입력", command=lambda: add_student(tree, id, name, major, kor, eng, mat)).grid(row=0, rowspan=6, column=3, sticky="nsew")

# 학생 삭제 폼
delete_frame = tkinter.LabelFrame(root, text="학생 정보 삭제")
delete_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

tkinter.Label(delete_frame, text="학번:").grid(row=0, column=0, sticky="e")
del_id = tkinter.Entry(delete_frame)
del_id.grid(row=0, column=1)

tkinter.Button(delete_frame, text="삭제", command=lambda: delete_student(tree, del_id)).grid(row=0, rowspan=2, column=3, sticky="nsew")

# 프로그램 종료 버튼
tkinter.Button(root, text="프로그램 종료", command=root.quit, bg="pink").grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.mainloop()