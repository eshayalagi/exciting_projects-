from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_filename):
    writer = PdfWriter()
    for pdf_file in pdf_list:
        try:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            print(f"Error reading {pdf_file}: {e}")

    with open(output_filename, "wb") as output:
        writer.write(output)
    print(f"Merged PDF saved as: {output_filename}")

if __name__ == "__main__":
    num_files = int(input("How many PDFs do you want to merge? "))
    pdfs_to_merge = []

    for i in range(num_files):
        path = input(f"Enter path for PDF #{i + 1}: ")
        pdfs_to_merge.append(path)

    output_file = input("Enter output filename (e.g., merged.pdf): ")
    merge_pdfs(pdfs_to_merge, output_file)
