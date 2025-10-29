# importing required modules
import PyPDF2
# creating a pdf file object
# pdfFileObj = open('./papers/antigaTAD01020230617-antiga.pdf', 'rb')
file_input=input("indique o documento pdf <path/name>:")
try:
    pdfFileObj = open(file_input+".pdf", 'rb')

    # creating a pdf reader object
    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # printing number of pages in pdf file
    num_pages=len(pdfReader.pages)
    print(len(pdfReader.pages))
    #print(pdfReader.numPages)

    # creating a page object
    #pageObj = pdfReader.getPage(0)
    pageObj = pdfReader.pages[0]

    # extracting text from page
    print(pageObj.extract_text())

    # all the text in the document
    print("all the text in the document *****\n")

    for x in range(0,num_pages):
        pageObj = pdfReader.pages[x]
        print("#######\nPage=",x)
        print(pageObj.extract_text())

    # closing the pdf file object
    pdfFileObj.close()
except:
    print("file not found")