"""
from tkinter import *
import tkinter.ttk
from tkinter import messagebox

class Student:
    def __init__(self, num, major, name, k_score, e_score, m_score):
        self.num = num
        self.major = major
        self.name = name
        self.k_score = k_score
        self.e_score = e_score
        self.m_score = m_score

        self.sum = self.k_score + self.e_score + self.m_score
        self.avg = self.sum / 3.0

    def get(self):
        return [self.num, self.major, self.name, self.k_score, self.e_score, self.m_score, self.sum, self.avg]
    
    def add(self):
        treeview.insert('', 'end', values=self.get())

def add_student():
    num = entry_num.get()
    major = entry_major.get()
    name = entry_name.get()
    try:
        k_score = int(entry_k_score.get())
        e_score = int(entry_e_score.get())
        m_score = int(entry_m_score.get())
    except ValueError:
        messagebox.showerror("입력 오류", "성적에는 숫자만 입력해야 합니다.")
        return
    
    # 중복 학번 체크
    for item in treeview.get_children():
        if treeview.item(item)['values'][0] == num:
            messagebox.showerror("중복 오류", "이미 존재하는 학번입니다.")
            return
    
    new_student = Student(num, major, name, k_score, e_score, m_score)
    new_student.add()
    
    entry_num.delete(0, END)
    entry_major.delete(0, END)
    entry_name.delete(0, END)
    entry_k_score.delete(0, END)
    entry_e_score.delete(0, END)
    entry_m_score.delete(0, END)

def delete_student():
    num = entry_delete_num.get()
    items = treeview.get_children()
    found = False
    for item in items:
        if treeview.item(item)['values'][0] == num:
            if messagebox.askyesno("삭제 확인", "정말로 삭제하시겠습니까?"):
                treeview.delete(item)
                found = True
                break
    if not found:
        messagebox.showerror("삭제 오류", "해당 학번을 찾을 수 없습니다.")
    entry_delete_num.delete(0, END)

def close_program():
    root.destroy()

root = Tk()
root.title("학생 성적 관리 프로그램")
root.geometry("800x700")

label_table = Label(root, text="학생정보열람")
label_table.pack(side="top")
treeview = tkinter.ttk.Treeview(root, columns=["num", "major", "name", "k_score", "e_score", "m_score", "sum", "avg"],
                                 displaycolumns=["num", "major", "name", "k_score", "e_score", "m_score", "sum", "avg"])

treeview.column("#0", width=0)
treeview.heading("#0", text="")

treeview.column("num", width=100)
treeview.heading("num", text="학번")
treeview.column("major", width=80)
treeview.heading("major", text="학과")
treeview.column("name", width=60)
treeview.heading("name", text="이름")
treeview.column("k_score", width=45)
treeview.heading("k_score", text="국어")
treeview.column("e_score", width=45)
treeview.heading("e_score", text="영어")
treeview.column("m_score", width=45)
treeview.heading("m_score", text="수학")
treeview.column("sum", width=45)
treeview.heading("sum", text="총점")
treeview.column("avg", width=55)
treeview.heading("avg", text="평균")

treeview.pack(fill="x")

# 왼쪽 밑 칸 - 신규 학생 등록
frame_left = LabelFrame(root, text="신규 학생 등록")
frame_left.pack(side="left", padx=10, pady=10, fill="y")

Label(frame_left, text="학번").grid(row=0, column=0, padx=5, pady=5)
entry_num = Entry(frame_left)
entry_num.grid(row=0, column=1, padx=5, pady=5)

Label(frame_left, text="학과").grid(row=1, column=0, padx=5, pady=5)
entry_major = Entry(frame_left)
entry_major.grid(row=1, column=1, padx=5, pady=5)

Label(frame_left, text="이름").grid(row=2, column=0, padx=5, pady=5)
entry_name = Entry(frame_left)
entry_name.grid(row=2, column=1, padx=5, pady=5)

Label(frame_left, text="국어 성적").grid(row=3, column=0, padx=5, pady=5)
entry_k_score = Entry(frame_left)
entry_k_score.grid(row=3, column=1, padx=5, pady=5)

Label(frame_left, text="영어 성적").grid(row=4, column=0, padx=5, pady=5)
entry_e_score = Entry(frame_left)
entry_e_score.grid(row=4, column=1, padx=5, pady=5)

Label(frame_left, text="수학 성적").grid(row=5, column=0, padx=5, pady=5)
entry_m_score = Entry(frame_left)
entry_m_score.grid(row=5, column=1, padx=5, pady=5)

Button(frame_left, text="입력", command=add_student, bg="pink").grid(row=6, columnspan=2, pady=10)

# 오른쪽 밑 칸 - 학생 정보 삭제
frame_right = LabelFrame(root, text="학생 정보 삭제")
frame_right.pack(side="right", padx=10, pady=10, fill="y")

Label(frame_right, text="학번").grid(row=0, column=0, padx=5, pady=5)
entry_delete_num = Entry(frame_right)
entry_delete_num.grid(row=0, column=1, padx=5, pady=5)

Button(frame_right, text="삭제", command=delete_student, bg="pink").grid(row=1, columnspan=2, pady=10)

# 프로그램 종료 버튼
Button(root, text="프로그램 종료", command=close_program, bg="pink").pack(side="bottom", fill="x")

root.mainloop()

"""

import tkinter as tk
from tkinter import ttk

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("학생 정보 관리")

        # Treeview for student data
        self.tree = ttk.Treeview(root, columns=("학번", "학과", "이름", "국어", "영어", "수학", "총점", "평균"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=70, anchor='center')

        self.tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Add sample data
        students = [
            ("2021000001", "소프트웨어", "홍길동", 98, 97, 89),
            ("2021000002", "소프트웨어", "유재석", 83, 23, 93),
            ("2021000003", "화학공학과", "마동석", 11, 47, 113),
            ("2021299040", "PLC학과", "JooIn", 35, 76, 34)
        ]
        for student in students:
            self.add_student_to_tree(student)

        # New student registration frame
        register_frame = tk.LabelFrame(root, text="신규 학생 등록")
        register_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(register_frame, text="학번:").grid(row=0, column=0, sticky="e")
        self.new_id = tk.Entry(register_frame)
        self.new_id.grid(row=0, column=1)

        tk.Label(register_frame, text="이름:").grid(row=1, column=0, sticky="e")
        self.new_name = tk.Entry(register_frame)
        self.new_name.grid(row=1, column=1)

        tk.Label(register_frame, text="학과:").grid(row=2, column=0, sticky="e")
        self.new_dept = tk.Entry(register_frame)
        self.new_dept.grid(row=2, column=1)

        tk.Label(register_frame, text="국어 성적:").grid(row=3, column=0, sticky="e")
        self.new_korean = tk.Entry(register_frame)
        self.new_korean.grid(row=3, column=1)

        tk.Label(register_frame, text="영어 성적:").grid(row=4, column=0, sticky="e")
        self.new_english = tk.Entry(register_frame)
        self.new_english.grid(row=4, column=1)

        tk.Label(register_frame, text="수학 성적:").grid(row=5, column=0, sticky="e")
        self.new_math = tk.Entry(register_frame)
        self.new_math.grid(row=5, column=1)

        tk.Button(register_frame, text="입력", command=self.add_student).grid(row=6, column=1, sticky="e")

        # Delete student frame
        delete_frame = tk.LabelFrame(root, text="학생 정보 삭제")
        delete_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(delete_frame, text="학번:").grid(row=0, column=0, sticky="e")
        self.del_id = tk.Entry(delete_frame)
        self.del_id.grid(row=0, column=1)

        tk.Button(delete_frame, text="삭제", command=self.delete_student).grid(row=1, column=1, sticky="e")

        # Exit button
        tk.Button(root, text="프로그램 종료", command=root.quit, bg="pink").grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

    def add_student_to_tree(self, student):
        student_id, dept, name, korean, english, math = student
        total = korean + english + math
        average = round(total / 3, 1)
        self.tree.insert("", "end", values=(student_id, dept, name, korean, english, math, total, average))

    def add_student(self):
        student_id = self.new_id.get()
        dept = self.new_dept.get()
        name = self.new_name.get()
        korean = int(self.new_korean.get())
        english = int(self.new_english.get())
        math = int(self.new_math.get())
        self.add_student_to_tree((student_id, dept, name, korean, english, math))
        
        # Clear the entry boxes
        self.new_id.delete(0, tk.END)
        self.new_dept.delete(0, tk.END)
        self.new_name.delete(0, tk.END)
        self.new_korean.delete(0, tk.END)
        self.new_english.delete(0, tk.END)
        self.new_math.delete(0, tk.END)

    def delete_student(self):
        student_id = self.del_id.get()
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == student_id:
                self.tree.delete(item)
                break
        self.del_id.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
