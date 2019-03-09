
def count_all(quan):
    quan = quan.lower()
    dem = {}
    for i in quan:
        if i not in dem:
            dem.setdefault(i,1)
        else:
            dem[i] = dem[i] + 1
    dem = sorted(dem.items())
    for i in dem:
        print(i[0],' ',i[1])
count_all('aadhfgbaiwfiasduhfuiaghowuiae')

        