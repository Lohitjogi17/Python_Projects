# Create Your Own AudioBook using Python Codes 
import pyttsx3
import PyPDF2
file=open("Climatechange.pdf", mode="rb")
pdf_reader= PyPDF2.PdfFileReader(file)
pages=pdf_reader.numPages
print(pages)
melo = pyttsx3.init()
for i in range(2,pages):
    page=pdf_reader.getPage()
    text = page.extractText()
    melo.say(text)
    melo.runAndWait()
