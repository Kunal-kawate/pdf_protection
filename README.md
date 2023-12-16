# pdf_protection
pikepdf is a Python library for reading and writing PDF files, pikepdf is based on QPDF, a powerful PDF manipulation and repair library. 

```markdown
# PDF Password Protection

This Python script utilizes the `pikepdf` library to password-protect a PDF file by restricting permissions. It's a simple tool that allows you to secure your PDF documents with a password.

## Usage

1. Install the `pikepdf` library using the following command:

    ```bash
    pip install pikepdf
    ```

2. Update the script with the name of the PDF file you want to protect and specify the desired password.

    ```python
    import pikepdf

    pdf_name = "write_here_your_pdf_name.pdf"  # Specify the name of the PDF you want to protect
    protected_pdf_name = "write_here_protected_pdf_name.pdf"  # Specify the name for the protected PDF
    password = "write_here_password"  # Specify the desired password

    old_pdf = pikepdf.Pdf.open(pdf_name)
    no_extr = pikepdf.Permissions(extract=False)

    old_pdf.save(protected_pdf_name, encryption=pikepdf.Encryption(user=password, owner="KunyaThing", allow=no_extr))
    ```

3. Run the script to create the password-protected PDF:

    ```bash
    python protect_pdf.py
    ```

## Requirements

- Python 3.x
- `pikepdf` library

## Note

Make sure to replace placeholders in the script with your actual PDF file name, the desired name for the protected PDF, and the chosen password.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!

```
