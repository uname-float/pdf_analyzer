import sys
from analyzer import PDFAnalyzer

def main():
    if len(sys.argv) < 4:
        print("Usage: python cli.py <pdf_file> <keyword1> <keyword2> ...")
        sys.exit(1)

    pdf_file = sys.argv[1]
    keywords = sys.argv[2:]

    pdf_analyzer = PDFAnalyzer(pdf_file)
    results = pdf_analyzer.ricerca_keyword(keywords)
    pdf_analyzer.scrivi_risultati(results, "results.txt")

if __name__ == "__main__":
    main()

