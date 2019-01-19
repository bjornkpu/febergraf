import plotly as py
import plotly.graph_objs as go

filename = "time_tmp_hr.txt"
time, tmp, hr = ([],[],[])

with open(filename) as f:
    for line in f:
        linearray = line.strip().split(' ')
        time.append(linearray[0][:2]+':'+linearray[0][2:])
        tmp.append(float(linearray[1])+0.5)
        hr.append(int(linearray[2]))

tmp_trace = go.Scatter(
    x = time,
    y = tmp,
    mode = 'lines',
    name = 'Temperature'
)

hr_trace = go.Scatter(
    x = time,
    y = hr,
    mode = 'lines',
    name = 'Hart rate',
    yaxis ='y2'
)

data = [tmp_trace, hr_trace]

layout = go.Layout(
    title='Feber og Hjerterytme',
    yaxis=dict(
        title='Temperatur',
        range=[36,38]
    ),
    yaxis2=dict(
        title='Hjerterytme',
        #range=[50,150],
        titlefont=dict(
            color='rgb(190, 30, 30)'
        ),
        tickfont=dict(
            color='rgb(190, 30, 30)'
        ),
        overlaying='y',
        side='right'
    )
)


graph = {"data": data,"layout": layout}

py.offline.plot(graph, auto_open=True)
