import praw,OAuth2Util

r = praw.Reddit("Flair PDF Analyze")
o = OAuth2Util.OAuth2Util(r)

flair = r.get_flair_list('leagueoflegends',limit = None)
flairlist = {}

for f in flair:
    if f['flair_css_class'] not in list(flairlist.keys()):
        flairlist[f['flair_css_class']] = 0
        print('added %s to the list' % f['flair_css_class'])
    else:
        flairlist[f['flair_css_class']] =  flairlist[f['flair_css_class']] + 1

f = open('Counter.txt','w')
for k,v in flairlist.items():
    try:
        f.write(k + ' , ' + str(v) + '\n')
    except:
        print(k,v)
f.close()
