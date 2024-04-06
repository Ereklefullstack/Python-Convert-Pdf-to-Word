import aspose.words as aw
import os

# doc = aw.Document("1.pdf")
# doc.save("123.docx")


pdf_path = r"C:\Users\Iran Computer\Documents\Proposal.pdf"
doc = aw.Document(pdf_path)

# جدا کردن نام فایل و پسوند
file_name, file_extension = os.path.splitext(pdf_path)

# ذخیره فایل ورد با همان نام فایل پی دی اف
doc.save(file_name + ".docx")