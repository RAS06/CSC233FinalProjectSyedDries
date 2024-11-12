from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing

# Data Preparation
className = 'CSC-233'
students = ['Caleb', 'Grace', 'Riz', 'Reece', 'Sam', 'Ethan', 'Tom', 'Joe', 'Dan', 'Caitlyn']
assignments = [
    ['HW 1', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['Exam 1', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 2', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['Exam 2', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 3', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 4', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['Final Exam', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 5', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 6', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55],
    ['HW 7', 95, 95, 85, 85, 85, 75, 75, 65, 65, 55]
]

# Calculate assignment averages and categorize by type
studentCount = len(students)
assignmentCount = len(assignments)
headers = [''] + students + ['Average']
examData, hwData = [headers], [headers]

# Process the assignments and calculate averages
for assignment in assignments:
    assignmentName = assignment[0]
    average = round(sum(assignment[1:]) / studentCount, 2)
    assignment.append(average)
    if 'Exam' in assignmentName:
        examData.append(assignment)
    else:
        hwData.append(assignment)

letGradeA, letGradeB,letGradeC, letGradeD, letGradeF = 0, 0, 0, 0, 0
i = 1
while i < (studentCount + 1):
    gradeTotal = 0
    averageGrade = 0
    for assignment in assignments:
        gradeTotal += assignment[i]
    averageGrade = gradeTotal / assignmentCount
    if averageGrade < 60:
        letGradeF += 1
    elif averageGrade < 70:
        letGradeD += 1
    elif averageGrade < 80:
        letGradeC += 1
    elif averageGrade < 90:
        letGradeB += 1
    else:
        letGradeA += 1
    i += 1

letGradeData = [
    ["", "Letter Grades:", "", "A", "B", "C", "D", "F", ""],
    ["", "Student Totals:", "", letGradeA, letGradeB,letGradeC, letGradeD, letGradeF, ""]
    ]

# Combine data for easy display
organizedData = hwData[1:] + examData[1:]

# Table Style Setup
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
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (1, 1), (-1, -1), colors.ghostwhite),
        ('LINEBEFORE', (2,1), (-2, -1), 1, colors.slategrey),
        ('LINEABOVE', (1,2), (-1, -1), 1, colors.slategrey),
        ('LINEBEFORE', (1, 1), (1, -1), 2, colors.black),
        ('LINEBEFORE', (-1, 0), (-1, -1), 2, colors.black),
        ('LINEABOVE', (1, 1), (-1, 1), 2, colors.black),
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

# Paragraph Style Setup
def getParagraphStyles():
    styles = getSampleStyleSheet()
    pageHeaderStyle = ParagraphStyle(
        "pageHeader", parent=styles["Title"], leading=20, fontName='Helvetica-Bold'
    )
    centeredHeaderStyle = ParagraphStyle(
        "centeredHeader", parent=styles["BodyText"], leading=20, alignment=TA_CENTER, fontName='Helvetica-Bold'
    )
    bufferStyle = ParagraphStyle(
        "buffer", parent=styles["BodyText"], leading= 30, alignment=TA_CENTER, fontName='Helvetica-Bold',
        textColor=colors.white
    )
    return pageHeaderStyle, centeredHeaderStyle, bufferStyle


# Create Bar Chart
def createBarChart(data, categories):
    drawing = Drawing(400, 200)
    barChart = VerticalBarChart()
    barChart.data = data
    barChart.valueAxis.valueMin = min([assignment[-1] for assignment in organizedData]) - 5
    barChart.valueAxis.valueMax = max([assignment[-1] for assignment in organizedData]) + 5
    barChart.valueAxis.valueStep = 2
    barChart.categoryAxis.categoryNames = categories
    barChart.width = 480
    barChart.height = 120
    barChart.bars[0].fillColor = colors.slategrey
    drawing.add(barChart)
    return drawing

# Create PDF
def createPdf():
    pageHeaderStyle, centeredHeaderStyle, bufferStyle = getParagraphStyles()
    examTable = Table(examData)
    hwTable = Table(hwData)
    letGradeTable = Table(letGradeData)
    examTable.setStyle(getTableStyle())
    hwTable.setStyle(getTableStyle())
    letGradeTable.setStyle(getLetGradeTableStyle())
    

    fileName = 'StudentGradeReport.pdf'
    pdf = SimpleDocTemplate(fileName, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)

    title = Paragraph("Student Grade Report: " + className, pageHeaderStyle)
    examHeader = Paragraph("Exam Grades", centeredHeaderStyle)
    hwHeader = Paragraph("Homework Grades", centeredHeaderStyle)
    buffer = Paragraph("Overall Grades", bufferStyle)
    
    categories = [assignment[0] for assignment in organizedData]
    averageScores = [[assignment[-1] for assignment in organizedData]]
    barChart = createBarChart(averageScores, categories)

    elements = [title, buffer, hwHeader, hwTable, buffer, examHeader, examTable, barChart, buffer, letGradeTable]
    pdf.build(elements)

# Generate PDF
createPdf()
