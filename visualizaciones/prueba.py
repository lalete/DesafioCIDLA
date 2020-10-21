import json
import pandas as pd 
import math
import matplotlib.pyplot as plt

with open('historiales_clinicos.json') as json_data:
    d = json.load(json_data)
    print(type(d))
    print(type(d[0]))
    #print(json.dumps(d[0], indent=2, sort_keys=True))

df1 = pd.DataFrame(d[0]['sesiones_medica'][0]['arquetipos'][0])
n = []
c = []
cn = -1
cd0 = 0
cd1 = 0
cd2 = 0

for i in d:
    cn = cn + 1
    n.append(d[cn]['nombre'])

for i in d[0]['profesionales_que_atendieron']:
    cd0 = cd0 + 1
c.append(cd0)

for i in d[1]['profesionales_que_atendieron']:
    cd1 = cd1 + 1
c.append(cd1)

for i in d[2]['profesionales_que_atendieron']:
    cd2 = cd2 + 1
c.append(cd2)


df = pd.DataFrame({'nombres':n, 'doctores':c})
ax = df.plot.bar(x='nombres', y='doctores', rot=0)
plt.show()

axe = df1.plot.bar(x='clave', y='tipo', rot=90)
plt.show()