#Imports FPDF so it has the functionality to create a pdf file.
from fpdf import FPDF

def generate_pdf(note):
    #Creates a PDF object and sets its font and starting coordinates.
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 10)
    pdf.set_font('Times', 'UB', 16)

    #Adds a header saying the following will be the condensed notes. 
    pdf.cell(ln=0, h=6, align='C', w=0, txt='Generated Notes', border = 0)

    #Adds the summary generated from ChatGPT to the PDF, which comes from the "note" object.
    pdf.set_font('Times', '', 12)
    pdf.set_y(pdf.get_y()+10)


    note.summary = fix_apostrophe(note.summary)
    pdf.multi_cell(w = 0, h = 6, txt = note.summary, border = 0, align = 'L', fill = False)

    #Adds a line separating the summary with the original transcript.
    pdf.set_y(pdf.get_y()+10)
    pdf.set_font('Times', 'UB', 16)

    pdf.cell(ln=0, h=6, align='C', w=0, txt='Original Audio Transcript', border = 0)

    #Adds the full transcription from the google cloud api into the pdf.
    pdf.set_xy(10, pdf.get_y()+10)
    pdf.set_font('Times', '', 12)
    
    note.transcription = fix_apostrophe(note.transcription)
    pdf.multi_cell(w = 0, h = 6, txt = note.transcription, border = 0, align = 'L', fill = False)

    #Creates the pdf file with the same name as the mp3 file. 
    pdf.output(f"notes/{note.name}pdf", 'F')

def fix_apostrophe(body_information):
    #Fixes ChatGPT's weird apostrophe formatting so apostrophes appears normal when viewed in the pdf. 
    return body_information.replace(r"\'", "'")

def main(note):
    #main() is ran in main.py to create the pdf with the information from note.
    generate_pdf(note)