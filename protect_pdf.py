import pikepdf

old_pdf = pikepdf.Pdf.open("write_here_your_pdf_name.pdf") #write here pdf name you want to protect that pdf 

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("write_here_protected_pdf_name.pdf",encryption=pikepdf.Encryption(user="write_here_password",owner="KunyaThing",allow=no_extr))