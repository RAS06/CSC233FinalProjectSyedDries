import tkinter
from tkinter.commondialog import Dialog
from tkinter.dialog import Dialog
from tkinter import simpledialog
import sqlite3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing


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

        self.submit = tkinter.Button(top, text='Submit', command= self.send)
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









def getTableStyle():
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.slategrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTSIZE', (1, 1), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.whitesmoke),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, -2), (-1, -2), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (1, 1), (-1, -1), colors.ghostwhite),
        ('LINEBEFORE', (2,1), (-2, -1), 1, colors.slategrey),
        ('LINEABOVE', (1,2), (-1, -1), 1, colors.slategrey),
        ('LINEBEFORE', (1, 1), (1, -1), 2, colors.black),
        ('LINEBEFORE', (-3, 0), (-3, -1), 2, colors.black),
        ('LINEBEFORE', (-1, 0), (-1, -1), 2, colors.black),
        ('LINEABOVE', (1, 1), (-1, 1), 2, colors.black),
        ('LINEABOVE', (0, -1), (-1, -1), 2, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ])
def getLetGradeTableStyle():
    return TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.slategrey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (3, 1), (-1, -1), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (2, -1), colors.whitesmoke),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (3, 1), (-2, -1), colors.ghostwhite),
        ('LINEBEFORE', (4,1), (-2, -1), 1, colors.slategrey),
        ('LINEBEFORE', (3,1), (3,1), 2, colors.black),
        ('LINEBEFORE', (-1,-1), (-1,-1), 2, colors.black),
        ('LINEABOVE', (3, 1), (-2, 1), 2, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black)
    ])
def getParagraphStyles():
    styles = getSampleStyleSheet()
    pageheaderstyle = ParagraphStyle(
        "pageHeader", parent=styles["Title"], fontName='Helvetica-Bold', fontSize=30
    )
    return pageheaderstyle
def createBarChart(data, categories):
    drawing = Drawing(480, 200)
    barChart = VerticalBarChart()
    barChart.data = [data]
    barChart.categoryAxis.categoryNames = categories
    barChart.valueAxis.valueMin = min(data) - 5
    barChart.valueAxis.valueMax = max(data) + 5
    barChart.valueAxis.valueStep = int((max(data)-min(data))/2.5)
    barChart.categoryAxis.categoryNames = categories
    barChart.width = 480
    barChart.height = 120
    barChart.bars[0].fillColor = colors.slategrey
    drawing.add(barChart)
    return drawing

def createPdf(tableData, letGradeData, className, headers, footers):
    pageHeaderStyle = getParagraphStyles()
    studentTable = Table(tableData)
    letGradeTable = Table(letGradeData)
    studentTable.setStyle(getTableStyle())
    letGradeTable.setStyle(getLetGradeTableStyle())

    fileName = 'StudentGradeReport.pdf'
    pdf = SimpleDocTemplate(fileName, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    title = Paragraph(f"Student Grade Report: {className}", pageHeaderStyle)

    assignmentNames = headers[1:7]
    assignmentResults = footers[1:7]
    assignmentBarChart = createBarChart(assignmentResults, assignmentNames)


    elements = [title, Spacer(0, 60), studentTable, assignmentBarChart, Spacer(0, 60),letGradeTable]
    pdf.build(elements)

def handle_pdf():
    className = 'CSC-233'
    headers = ['', 'HW 1', 'HW 2', 'HW 3', 'Quiz 1', 'Quiz 2', 'Quiz 3', 'HW Average', 'Quiz Average', 'Overall Grade']

    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")


    students = []
    for item in cursor.fetchall():
        students.append(list(item))

    for std in students:
        print(type(std))

    # students = [
    #     ['Caleb', 78, 85, 98, 63, 85, 96],
    #     ['Riz', 89, 95, 76, 89, 90, 94],
    #     ['Reese', 76, 90, 73, 86, 98, 87],
    #     ['Grace', 90, 98, 100, 67, 84, 88],
    #     ['Ethan', 75, 87, 78, 90, 87, 65],
    #     ['Chance', 89, 95, 76, 89, 90, 94],
    #     ['Eli', 76, 90, 73, 86, 98, 87],
    #     ['Chase', 76, 90, 73, 86, 98, 87],
    #     ['Ella', 89, 95, 76, 89, 90, 94],
    #     ['Chloe', 75, 87, 78, 90, 87, 65]
    # ]


    tableData = [headers]

    for student in students:
        hwAvg = round((student[1] + student[2] + student[3]) / 3.0, 2)
        quizAvg = round((student[4] + student[5] + student[6]) / 3.0, 2)
        ovrGrade = round((hwAvg + quizAvg) / 2.0, 2)
        student.append(hwAvg)
        student.append(quizAvg)
        student.append(ovrGrade)
        tableData.append(student)

    hw1Data, hw2Data, hw3Data, quiz1Data, quiz2Data, quiz3Data, hwAvgData, quizAvgData, ovrGradeData = [], [], [], [], [], [], [], [], []

    for student in students:
        hw1Data.append(student[1])
        hw2Data.append(student[2])
        hw3Data.append(student[3])
        quiz1Data.append(student[4])
        quiz2Data.append(student[5])
        quiz3Data.append(student[6])
        hwAvgData.append(student[7])
        quizAvgData.append(student[8])
        ovrGradeData.append(student[9])


    footers = [
        'Average',
        round(float(sum(hw1Data) / len(hw1Data)), 2),
        round(float(sum(hw2Data) / len(hw2Data)), 2),
        round(float(sum(hw3Data) / len(hw3Data)), 2),
        round(float(sum(quiz1Data) / len(quiz1Data)), 2),
        round(float(sum(quiz2Data) / len(quiz2Data)), 2),
        round(float(sum(quiz3Data) / len(quiz3Data)), 2),
        round(float(sum(hwAvgData) / len(hwAvgData)), 2),
        round(float(sum(quizAvgData) / len(quizAvgData)), 2),
        round(float(sum(ovrGradeData) / len(ovrGradeData)), 2)
    ]
    tableData.append(footers)

    letGradeA, letGradeB, letGradeC, letGradeD, letGradeF = 0, 0, 0, 0, 0

    for student in students:
        if student[-1] < 60:
            letGradeF += 1
        elif student[-1] < 70:
            letGradeD += 1
        elif student[-1] < 80:
            letGradeC += 1
        elif student[-1] < 90:
            letGradeB += 1
        else:
            letGradeA += 1

    letGradeData = [
        ["", "Letter Grades:", "", "A", "B", "C", "D", "F", ""],
        ["", "Student Totals:", "", letGradeA, letGradeB, letGradeC, letGradeD, letGradeF, ""]
    ]
    conn.close()
    createPdf(tableData, letGradeData, className, headers, footers)


def main():
    # Create main window
    window = tkinter.Tk()
    window.geometry("900x500")
    window.title("Final Project")

    # Title
    label = tkinter.Label(window, text="Welcome to Student Grading System.")
    label.grid(column=0, row=0)

    # Add student
    button = tkinter.Button(window, text="Add Student", command=lambda: handle(window))
    button.grid(column = 0, row = 1)

    #pdfGenerator
    mk_pdf = tkinter.Button(window, text="Make PDF", command=lambda: handle_pdf())
    mk_pdf.grid(column = 0, row = 2)

# Start the GUI
    window.mainloop()

main()

