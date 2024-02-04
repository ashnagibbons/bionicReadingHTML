# bionicReadingHTML
## This is a python script to turn text from any PDF document into bionic text in an HTML file!

This project is an ongoing project I have undertaken to experiment with Python PDF packages. My initial goal was only twofold: 
* get the text out of the PDF
* bold the first couple of letters of each word and write that to a file or format where it was displayed

Now that these are accomplished, I'm working on debugging and improving UX.

Bionic reading is a concept trademarked by [https://bionic-reading.com/](url). It bolds the first few letters of each word in a block of text. It is intended to help give you focal points on each word so that the text is broken up into something that is more manageabe visually, and so that your brain, focusing first on the bolded letters, "fills in" the rest of each word after reading the bolded part. This is especially helful for improving reading speed. As a student, this has been very useful for myself and my friends! 


This script uses the PyPDF2 module to read text from a PDF file. It then splits the text into a list of each word in the text, and loops through each word to bold about the first half of the word, and add the bolded portion onto the second half of the word, which stays in normal format. 

This text is then written into an HTML file. I landed on an HTML file after trying RTF and having trouble with opening the files. I will continue to experiment with reading from and writing to other types of files.


## Installation & Use

A website to support this script is forthcoming, but until then, take the following steps to use this script on your own PDFs:
* Install Python for your machine type (Linux, Mac, Windows, etc.) [https://www.python.org/downloads/](url)
* Install PyPDF2 [https://pypi.org/project/PyPDF2/](url)
* Open the main.py file and run it!

After running the program, the HTML file will have installed in your default directory on your device. You can open this file with a web browser, or in word processors such as TextEdit or Word.


## Known Issues (Work In Progress)
* The outputted text is not formatted into paragraphs yet, the HTML file will be one big block of text. This is the first issue I will be working on resolving, since I'm aware this really affects UX.
* As stated before, this script currently reads from PDFS ONLY, and writes into HTML FILES ONLY. I will work on expanding the types of supported files.
* This script requires users to install both Python and PyPDF, which can be confusing. I am working on making a website and/or app (probably through Django) so that this is accessible to anybody.


## Find a bug, or want to contribute?
I greatly appreciate anybody who comes across this project and finds any additional issues with it, or wants to contribute to fix any of the known issues above. I encourage you to clone and rename this project if you want to tweak it in any way, or please use the issues tab above to report any additional issues. 
 
