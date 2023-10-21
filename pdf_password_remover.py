import os
from PyPDF2 import PdfReader, PdfWriter

# Directory where your PDF files are located
pdf_directory = '/app/pdf_files/'
print('hello to the colorado bug')
# Password to remove (provide the correct password)
pdf_password = os.getenv('PDF_PASSWORD', '')

# Loop through all files in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_file_path = os.path.join(pdf_directory, filename)

        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_file_path)

        # Check if the PDF is password-protected
        if pdf_reader.is_encrypted:
            try:
                # Attempt to decrypt the PDF using the provided password
                pdf_reader.decrypt(pdf_password)

                # Create a new PDF writer object
                pdf_writer = PdfWriter()

                # Add each page to the new PDF writer object
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                # Save the new, password-free PDF
                new_pdf_path = os.path.join(pdf_directory, 'unlocked_' + filename)
                with open(new_pdf_path, 'wb') as new_pdf_file:
                    pdf_writer.write(new_pdf_file)

                print(f'Success: Removed password from {filename}')
            except Exception as e:
                print(f'Error: Failed to remove password from {filename}: {str(e)}')
        else:
            print(f'Skipped: {filename} is not password-protected')

print('Processing complete.')
