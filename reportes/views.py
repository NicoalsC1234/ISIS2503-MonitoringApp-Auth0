
import os

from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_reportes import create_reportes, get_reportes

def reportes_list(request):
    reportes = get_reportes()
    context = {
        'reportes_list': reportes
    }
    return render(request, 'Reportes/actividades.html', context)

def reportes_create(request):
    response = HttpResponse(content_type= 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Sprint2-student-report.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize =A4)


    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750,"08/04/2021")
    c.line(460,747,560,747)

    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''No.''',styleBH)
    alumno = Paragraph('''Alumno''',styleBH)
    b1 = Paragraph('''Materia1''',styleBH)
    b2 = Paragraph('''Materia2''', styleBH)
    b3 = Paragraph('''Materia3''', styleBH)
    total = Paragraph('''TOTAL''', styleBH)
    data = [[numero,alumno,b1,b2,b3,total]]

    alumnos = [{'#':'1','nombre':'Nicolas Chalee Guerrero', 'b1':'3.4','b2':'2.2','b3':'4.5','total':'3.36'}]

    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_CENTER
    styleN.fontSize = 7

    width, height = A4
    high = 650
    for student in alumnos:
        this_student = [student['#'],student['nombre'],student['b1'], student['b2'],student['b3'],student['total']]
        data.append(this_student)
        high = high -18

    table = Table(data, colWidths=[1.9*inch, 9.5*inch,1.9*inch,1.9*inch,1.9*inch,1.9*inch])
    table.setStyle(TableStyle([('INNERGRID',(0,0),(-1,-1),0.25, colors.black),('BOX',(0,0),(-1,-1),0.25, colors.black),]))

    table.wrapOn(c,width,height)
    table.drawOn(c,30,high)
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
    return render(request, 'Reportes/actividadesCreate.html', context)
