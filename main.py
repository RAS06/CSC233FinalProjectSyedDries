import tkinter
from tkinter import ttk
from tkinter.commondialog import Dialog
from tkinter.dialog import Dialog
from tkinter import simpledialog
import sqlite3


class dialogIn: #https://stackoverflow.com/questions/10057672/correct-way-to-implement-a-custom-popup-tkinter-dialog-box

    def __init__(self, root):
        top = self.top = tkinter.Toplevel(root)
        self.top.geometry("500x400")

        self.labelStudent = tkinter.Label(top, text="Add name")
        self.labelStudent.pack()

        self.top.studentEntryBox = tkinter.Entry(top)
        self.top.studentEntryBox.pack()

        self.labelHW1 = tkinter.Label(top, text="Add HW1")
        self.labelHW1.pack()

        self.top.HW1EntryBox = tkinter.Entry(top)
        self.top.HW1EntryBox.pack()

        self.labelHW2 = tkinter.Label(top, text="Add HW2")
        self.labelHW2.pack()

        self.top.HW2EntryBox = tkinter.Entry(top)
        self.top.HW2EntryBox.pack()

        self.labelHW3 = tkinter.Label(top, text="Add HW3")
        self.labelHW3.pack()

        self.top.HW3EntryBox = tkinter.Entry(top)
        self.top.HW3EntryBox.pack()

        self.labelQuiz1 = tkinter.Label(top, text="Add Quiz 1")
        self.labelQuiz1.pack()

        self.top.Quiz1EntryBox = tkinter.Entry(top)
        self.top.Quiz1EntryBox.pack()

        self.labelQuiz2 = tkinter.Label(top, text="Add Quiz 2")
        self.labelQuiz2.pack()

        self.top.Quiz2EntryBox = tkinter.Entry(top)
        self.top.Quiz2EntryBox.pack()

        self.labelQuiz3 = tkinter.Label(top, text="Add Quiz 3")
        self.labelQuiz3.pack()

        self.top.Quiz3EntryBox = tkinter.Entry(top)
        self.top.Quiz3EntryBox.pack()

        self.submit = tkinter.Button(top, text='Submit', command=self.send)
        self.submit.pack()

    def send(self):
        data = []
        for element in self.top.children.values():
            if isinstance(element, tkinter.Entry):
                data.append(element.get())

        conn = sqlite3.connect('identifier.sqlite')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                                id TEXT PRIMARY KEY,
                                HW1 INTEGER,
                                HW2 INTEGER,
                                HW3 INTEGER,
                                Quiz1 INTEGER,
                                Quiz2 INTEGER,
                                Quiz3 INTEGER
                            )''')

        cursor.execute("INSERT INTO student (id, HW1, HW2, HW3, Quiz1, Quiz2, Quiz3) VALUES (?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

        conn.commit()

        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()
        for row in results:
            print(row)

        conn.close()
        self.top.destroy()



def handle(root):
    inputDialog = dialogIn(root)


def handle2(root):
    txt = simpledialog.askstring("ADD STUDENT", "Please enter a student.")

    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                        id TEXT PRIMARY KEY,
                        HW1 INTEGER,
                        HW2 INTEGER,
                        HW3 INTEGER,
                        Quiz1 INTEGER,
                        Quiz2 INTEGER,
                        Quiz3 INTEGER
                    )''')

    cursor.execute("INSERT INTO student (id, HW1, Quiz1) VALUES (?, ?, ?)", (txt, 100, 100))

    conn.commit()

    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.close()

def displayWindow():
    displayWindow = tkinter.Tk()
    displayWindow.geometry("900x500")
    displayWindow.title("Grades")

    tree = ttk.Treeview(displayWindow, columns=("ID", "HW1", "HW2", "HW3", "Quiz1", "Quiz2", "Quiz3", "Average"), show='headings')
    tree.heading("ID", text="Student ID")
    tree.column("ID", minwidth=0, width = 100, stretch=False)
    tree.heading("HW1", text="HW1")
    tree.column("HW1", minwidth=0, width = 100, stretch=False)
    tree.heading("HW2", text="HW2")
    tree.column("HW2", minwidth=0, width = 100, stretch=False)
    tree.heading("HW3", text="HW3")
    tree.column("HW3", minwidth=0, width = 100, stretch=False)
    tree.heading("Quiz1", text="Quiz1")
    tree.column("Quiz1", minwidth=0, width = 100, stretch=False)
    tree.heading("Quiz2", text="Quiz2")
    tree.column("Quiz2", minwidth=0, width = 100, stretch=False)
    tree.heading("Quiz3", text="Quiz3")
    tree.column("Quiz3", minwidth=0, width = 100, stretch=False)
    tree.heading("Average", text="Average")
    tree.column("Average", minwidth=0, width = 100, stretch=False)
    tree.pack(fill=tkinter.BOTH, expand=True)

    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT id, HW1, HW2, HW3, Quiz1, Quiz2, Quiz3, (HW1 + HW2 + HW3 + Quiz1 + Quiz2 + Quiz3)/6 
                   as Average FROM student 
                   where NOT (
                   HW1 is null or
                   HW2 is null or
                   HW3 is null or
                   Quiz1 is null or
                   Quiz2 is null or
                   Quiz3 is null
                   )''')
    results = cursor.fetchall()
    cursor.execute("SELECT AVG(HW1), AVG(HW2), AVG(HW3), AVG(Quiz1), AVG(Quiz2), AVG(Quiz3)FROM student")
    avg = cursor.fetchall()
    conn.close()

    for row in results:
        tree.insert("", "end", values=row)

    avg = avg[0]
    avg2 = ["Average:"]
    for i in avg:
        i = round(i)
        avg2.append(i)
    avg = (avg2[0],avg2[1],avg2[2],avg2[3],avg2[4],avg2[5],avg2[6])
    tree.insert("", "end", values = avg)
    
    displayWindow.mainloop()

def main():
    student_data = []
    assignments_list = []
    # Create main window
    window = tkinter.Tk()
    window.geometry("900x500")
    window.title("Final Project")

    # Create a label
    label = tkinter.Label(window, text="Welcome to Student Grading System.")
    label.grid(column=0, row=0)

    # Create a button
    button = tkinter.Button(window, text="Add Student", command=lambda: handle(window))
    button.grid(column = 0, row = 1)

    # Create a button
    button2 = tkinter.Button(window, text="Display Grades", command=lambda: displayWindow())
    button2.grid(column = 0, row = 2)

# Start the GUI
    window.mainloop()

main()

