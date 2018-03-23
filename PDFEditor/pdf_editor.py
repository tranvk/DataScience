import PyPDF2
import pathlib



def PDFtoString (file):


    link = pathlib.Path(file)
    if (link.is_file()): #is_file() method uses try/except in implementation

        pdfFileObj = open (file, 'rb') #open pdf in read binary mode



    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #test if library is working
    #print(pdfReader.numPages)

    pageNumber = input("Enter the PDF's page number: ")

    pageObj = pdfReader.getPage(int(pageNumber) - 1) #get pageObj

    pageString = pageObj.extractText()

    print(pageString)

print (PDFtoString('meetingminutes2.pdf'))
