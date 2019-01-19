import plotly as py
import plotly.graph_objs as go

filename = "time_tmp_hr.txt"    # Hvor den henter data fra
time, tmp, hr = ([],[],[])      # De tre arrayene vi legger dataen inn i

# For-loop som legger dataene inn i aray
with open(filename) as f:
    for line in f:
        linearray = line.strip().split(' ')                     # splitter hver linje på mellomrom
        time.append(linearray[0][:2]+':'+linearray[0][2:])      # tidspunktet men formaterer fra 2200 -> 22:00
        tmp.append(float(linearray[1])+0.5)                     # temperatur men parser til flyttall for desimal
        hr.append(int(linearray[2]))                            # hjerterytme parses til int for heltall

# en 'trace' er navnet for an linje/graf. Her setter jeg opp tracen for temperaturen
# Ville ha en graf med både temp of hjerterytme så jeg trengte to tracer der hver delte x-aksen tid men hadde
# forskjellig y akse
tmp_trace = go.Scatter(
    x = time,
    y = tmp,
    mode = 'lines',         # for å få linjer med punkter der det er datapunkter
    name = 'Temperature'    # navnet som vises til høyre for grafen. linje-navn
)

hr_trace = go.Scatter(
    x = time,
    y = hr,
    mode = 'lines',
    name = 'Hart rate',
    yaxis ='y2'             # Viktig for å skille mellom y-aksene. Denne setter hjerterytme til y-akse nr 2
)

data = [tmp_trace, hr_trace]    # samler begge tracene til ett dataobjekt

# Definerer layout
layout = go.Layout(
    title='Feber og Hjerterytme',       # tittelen til hele grafen
# Første y-akse
    yaxis=dict(
        title='Temperatur',             # navnet som skal stå på aksen
        range=[36,38]                   # Ville bestemme min- og maxverdi på y-aksen
    ),
# andre y-akse
    yaxis2=dict(
        title='Hjerterytme',
# komenterte denne ut siden jeg kanskje kom til å få høyere enn 150 en gang, om ingenting står vil den endres dynamisk
        #range=[50,150],
        titlefont=dict(                 # likte ikke default-fargen
            color='rgb(190, 30, 30)'
        ),
        tickfont=dict(
            color='rgb(190, 30, 30)'
        ),
        overlaying='y',                 # setter yaxis2 til å være en y-akse
        side='right'                    # hvilken side aksen skal hvises på
    )
)

# lager et graph-objekt. dette er en dictionary på json-form det er det plot() vil ha.
graph = {"data": data,"layout": layout}

# funksjonskallet som genererer grafen.
py.offline.plot(graph, auto_open=True)
