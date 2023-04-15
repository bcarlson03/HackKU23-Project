#What needs to be imported into "output".
from fpdf import FPDF

def generate_pdf(note):
    #Creates a PDF object and sets its font and starting coordinates.
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 20)
    pdf.set_font('Times', 'B', 13.0)

    #Adds a header saying the following will be the condensed notes. 
    pdf.cell(ln=0, h=5.0, align='C', w=0, txt='Generated Notes', border = 0)

    #Adds the summary generated from ChatGPT to the PDF.
    summary_string = ''
    for line in note.summary:
        summary_string += line + '\n'
    pdf.multi_cell(w = 0, h = 5, txt = summary_string, border = 0, align = 'L', fill = False)

    #Adds a line separating the summary with the original transcript.
    pdf.cell(ln=0, h=5.0, align='C', w=0, txt='Original Audio Transcript', border = 0)

    #Adds the full transcription from the google cloud api into the pdf. 
    transcription_string = ''
    for line in note.transcription:
        transcript_string += line + '\n'
    pdf.multi_cell(w = 0, h = 5, txt = summary_string, border = 0, align = 'L', fill = False)

    #Creates the pdf file with the same name as the mp3 file. 
    pdf.output(f"notes/{note.name}", 'F')

def main(note):
    generate_pdf(note)