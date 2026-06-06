from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

number = int(input("How many pdfs do you want to merge?"))
for i in range(0,number):
    name=input(f"Enter the name {i+1} of the pdf file: ")
    if not name.endswith(".pdf"):
        name += ".pdf"
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()