import slate

pdf = 'E:/xhy_python/data-wrangling-master/data/chp5/EN-FINAL Table 9.pdf'

with open(pdf) as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print page