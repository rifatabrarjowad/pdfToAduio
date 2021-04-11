import pyttsx3
import PyPDF2
book = open('pdf.pdf', 'rb')
pdfreaders = PyPDF2.PdfFileReader(book)
#pages = pdfreaders.numPages
#print(pages)
speaker = pyttsx3.init()
page = pdfreaders.getPage(2)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()