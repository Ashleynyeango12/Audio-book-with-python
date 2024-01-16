import pyttsx3
import PyPDF2

book = open("Atomic Habits.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.pages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.pages[7]
Text = page.extract_text()
speaker.say(Text)
speaker.runAndWait()
