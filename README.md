# medquad_ir_hacking
MedQuAD IR hacking

# Initial tasks
1. Put most code in medquad_ir.py
2. Write a function that loads the MedQuAD data set
3. Write a function htmltext = dump_medquad_url(url) that (possibly using Beautiful Soup https://pypi.org/project/beautifulsoup4/) and Boilerpipe(https://pypi.org/project/boilerpy3/) that download the webpage from the url value in the MedQuAD data set
4. Write a fuction text = extract_medquad_text(htmltext) which extracts only the html article from the url and strips out the html -- note this method should filter out the footer, header and other irrelevant web page segements
