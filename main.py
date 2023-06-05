import os
from pypdf import PdfReader, PdfWriter
import argparse


parser = argparse.ArgumentParser(description='split pdf')
parser.add_argument('-f', '--pdf', help='input pdf')
parser.add_argument('-s', '--start', type=int, default=2, help='start page')
parser.add_argument('-e', '--end', type=int, default=0, help='end page')


def do_pdf_split(path, start_page, end_page):
    base_name = os.path.splitext(os.path.basename(path))[0]
    pdf_reader = PdfReader(path)
    pdf_writer = PdfWriter()
    page_start = start_page
    pages = pdf_reader.pages
    page_end = end_page if end_page else len(pages)
    for p_num in range(page_start-1, page_end):
        pdf_writer.add_page(pages[p_num])
    out_file_name = f".\\{base_name}_{page_start}-{page_end}.pdf"
    with open(out_file_name, 'wb') as out:
        pdf_writer.write(out)


if __name__ == "__main__":
    args = parser.parse_args()
    path = args.pdf
    start_page, end_page = args.start, args.end
    do_pdf_split(args.pdf, start_page, end_page)