import PyPDF2 
from PyPDF2 import PdfReader, PdfWriter
#FIXME: how to separate paragraphs

def get_text(pdf_path):
    #get the file name and read in bytecode
    file = open(pdf_path, "rb")

    #use pdfreader function to get all text in the PDF from each page
    reader = PdfReader(file)

    total_text = ""
    total_page_text = ""
    
    for i in range(0, len(reader.pages)):
        page_selected = reader.pages[i]
        text_from_page = page_selected.extract_text()

        total_page_text = str(text_from_page)

        total_text = total_text + total_page_text

    return total_text
   
def bold_text(text):
    #add HTML tags for bold format
    return "<strong>" + text + "</strong>"

def bionicText(total_text, outputfile):
    
    bionicWords = ""
    boldedPortion = 0
    
    words = total_text.split()

    #format each word as bionic (first few characters bolded)
    for word in words:
        if (len(word) % 2 == 0):
            boldedPortion = len(word)//2
        else:
            boldedPortion = (len(word)//2) + 1
            

        word = bold_text(word[0:boldedPortion]) + word[boldedPortion:len(word)]

        bionicWords = bionicWords + word + " "
   
                
    out_file = open(outputfile, 'w')
    out_file.write("<p>" + bionicWords + "</p>")

    out_file.close()



def main():
    file = input("Please type in the name of your PDF file: ")
    if (file[-4:] != ".pdf"):
        file = file + ".pdf"
    text_from_file = get_text(file)
    
    last_period = file.rfind(".")
    outfile = file[:last_period] + ".html"
    
    bionicText(text_from_file, outfile)
    print("\n\nYour bionic text is stored in", outfile + "!")
    
    
   
main()


