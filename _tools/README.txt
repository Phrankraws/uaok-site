Not published (see ../.vercelignore).

build_batmaine_pages.py  rebuilds researcher/avatar/crm/text-scheduling/dj/kids-game.html
    python3 _tools/build_batmaine_pages.py .
    All words, prices, Stripe links (LINKS) and screenshots (gallery=) live in this one file.

build_sales_pdf.py  makes the 8-page sales PDF from the same data (needs: pip install segno)
    python3 _tools/build_sales_pdf.py /tmp/sales.html   then print it to PDF with Chrome headless
