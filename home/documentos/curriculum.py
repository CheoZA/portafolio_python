from typing import List
from fpdf import FPDF
from home import models

from home.models import Persona, Proyecto

def generar_cv():
    
    persona : Persona = models.Persona.objects.first()
    proyectos =  models.Proyecto.objects.select_related().all()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(40, 10, persona.nombre + ' ' + persona.apellido)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(40, 40, str(persona.fecha_de_nacimiento))
    pdf.output('static/generated/cv.pdf', 'F')
