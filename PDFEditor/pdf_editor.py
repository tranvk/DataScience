import PyPDF2
import pathlib
import pdfkit

'''
Focus: covert PDF to python string, identify index of word to edit, modify word, copy to new PDF,
download new PDF with new name
'''

#are all PDFs made equal in terms of encoding





def changeWordByIndex(PDFString, new_word):

    #turn string into list of strings
    word_list = PDFString.split()

    word_list[1] = new_word

    #convert list back to string

    modifiedString = "".join(word_list)

    return modifiedString




def PDFtoString (file_name):


    link = pathlib.Path(file_name)
    if (link.is_file()): #is_file() method uses try/except in implementation

        pdfFileObj = open(file_name, 'rb') #open pdf in read binary mode

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    if (pdfReader.isEncrypted): #check if PDF is encrypted, decrypt if true
        password = input("Enter the password: ")
        pdfReader.decrypt(password)

        #file will remain encrypted on disk

    pageNumber = input("Enter the PDF's page number: ")

    pageObj = pdfReader.getPage(int(pageNumber) - 1) #get pageObj

    pageString = pageObj.extractText() #to string

    return (pageString)


def main():

    PDFwords = PDFtoString('meetingminutes.pdf')

    new_company = input("Enter the company name: ")

    newPDFString = changeWordByIndex(PDFwords, new_company) #list modified and turned to string

    PDFtitle = "coverletter" + new_company + ".pdf"

    pdfkit.from_string(newPDFString, PDFtitle)



if __name__ == "__main__":
    main()

print(main())
