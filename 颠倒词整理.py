import shutil,sys,os

shutil.copyfile(sys.argv[1],'副本')
rst = open('颠倒词结果','w')

for keyword in open(sys.argv[1],'r',encoding='utf-8'):
    keyword = keyword.strip()
    ddc = [keyword]
    for i in open('副本','r',encoding='utf-8'):
        i = i.strip()
        if i == keyword:
            continue
        elif sorted(i) == sorted(keyword) and i != keyword:
            ddc.append(i)
    ddc.sort()
    if len(ddc) > 1:
        rst.write('%s\n' %(','.join(ddc)))
rst.close()

uniqci = []
for ci in open('颠倒词结果','r',encoding='utf-8'):
    if ci in uniqci:
        continue
    uniqci.append(ci)
with open('颠倒词结果.txt','w') as handle:
    handle.writelines(uniqci)

os.remove('颠倒词结果')
os.remove('副本')
