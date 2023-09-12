import pyttsx3
import PyPDF3
engine = pyttsx3.init()
book = open('sample.pdf', 'rb')
pdfRead= PyPDF3.PdfFileReader(book)
 
#to start the reading from 1st page in the pdf
page = pdfRead.getPage(3)
 
#to extract text to read
text = page.extractText()
#takes in message to read or text
engine.say(text)
 
engine.runAndWait()
