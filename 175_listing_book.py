import pyttsx3 as pt
import PyPDF2 as pd
book = open("01. Anna Karenina author Leo Tolstoy.pdf",'rb')
reader = pd.PdfFileReader(book)# it read pdf 
pages = reader.numPages# it function to say about pages
print(pages)
speaker = pt.init()
for num in range(13,pages):
    page = reader.getPage(12)# give the page which you have
    Text = page.extract_text()
#print(Text)
    speaker.say(Text)
    speaker.runAndWait()