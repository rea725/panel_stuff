import panel as pn
import uuid
import plaidcloud.utilities.debug.wingdbstub
import altair as alt
from vega_datasets import data
pn.extension("vega")

themes = sorted(alt.themes.names())
theme = pn.widgets.Select(value="dark", options=themes, name="Theme")
color = pn.widgets.ColorPicker(value="#F08080", name="Color")

def plot(theme, color):
    alt.themes.enable(theme)

    return (
        alt.Chart(data.cars())
        .mark_circle(size=200)
        .encode(
            x='Horsepower:Q',
            y='Miles_per_Gallon:Q',
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .configure_mark(
            color=color
        )
        .properties(
            height=300,
            width="container",
        )
        .interactive()
    )

plot_altair = pn.Column(
    pn.Row(theme, color),
    pn.pane.Vega(pn.bind(plot, theme=theme, color=color), height=350, sizing_mode="stretch_width"),
    "**Altair Themes**: " + ", ".join(themes),
    styles={"border": "1px solid lightgray"}
)#.servable()



THEME = "shine"

ECHARTS_THEMES = {
    "infographic": "https://fastly.jsdelivr.net/npm/echarts/theme/infographic.js?_v_=20200710_1",
    "macarons": "https://fastly.jsdelivr.net/npm/echarts/theme/macarons.js?_v_=20200710_1",
    "roma": "https://fastly.jsdelivr.net/npm/echarts/theme/roma.js?_v_=20200710_1",
    "shine": "https://fastly.jsdelivr.net/npm/echarts/theme/shine.js?_v_=20200710_1",
    "vintage": "https://fastly.jsdelivr.net/npm/echarts/theme/vintage.js?_v_=20200710_1",
}

pn.pane.ECharts.param.theme.objects = pn.pane.ECharts.param.theme.objects + list(
    ECHARTS_THEMES
)

pn.extension("echarts", js_files=ECHARTS_THEMES)

echart_bar = {
    "title": {"text": "ECharts Example"},
    "tooltip": {},
    "legend": {"data": ["Sales"]},
    "xAxis": {"data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"]},
    "yAxis": {},
    "series": [{"name": "Sales", "type": "bar", "data": [5, 20, 36, 10, 10, 20]}],
}

plot = pn.pane.ECharts(
    echart_bar,
    height=500,
    sizing_mode="stretch_width",
    theme=THEME,
)
plot_echarts = pn.Column(plot.param.theme, plot, sizing_mode="stretch_width")#.servable()




import numpy as np

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import panel as pn

pn.extension()


def plot(style, color):
    x = np.arange(-2, 8, 0.1)
    y = 0.1 * x**3 - x**2 + 3 * x + 2

    plt.style.use("default")  # reset to not be affected by previous style changes
    plt.style.use(style)  # change to the specified style

    fig0 = Figure(figsize=(12, 6))
    ax0 = fig0.subplots()
    ax0.plot(x, y, linewidth=10.0, color=color)
    ax0.set_title(f"Matplotlib Style: {style}")

    plt.style.use("default")  # reset to not affect style of other plots

    return fig0


styles = sorted(plt.style.available)
style = pn.widgets.Select(value="dark_background", options=styles, name="Style")
color = pn.widgets.ColorPicker(value="#F08080", name="Color")

plot_mpl = pn.Column(
    pn.Row(style, color),
    pn.pane.Matplotlib(
        pn.bind(plot, style=style, color=color),
        height=400,
        sizing_mode="fixed",
    ),
    "**Matplotlib Styles**: " + ", ".join(styles),
)#.servable()





import pandas as pd
import plotly.express as px
import plotly.io as pio

import panel as pn

pn.extension("plotly")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)

def plot(template, color):
    fig = px.line(
        data,
        x="Day",
        y="Orders",
        template=template,
        color_discrete_sequence=(color,),
        title=f"Template: {template}",
    )
    fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
    fig.layout.autosize = True
    return fig

templates = sorted(pio.templates)
template = pn.widgets.Select(value="plotly_dark", options=templates, name="Template")
color = pn.widgets.ColorPicker(value="#F08080", name="Color")

plot_plotly_1 = pn.Column(
    pn.Row(template, color),
    pn.pane.Plotly(pn.bind(plot, template, color), sizing_mode="stretch_width"),
    "**Plotly Templates**: " + ", ".join(templates),
)#.servable()


import pandas as pd
import plotly.graph_objects as go

import panel as pn

pn.extension("plotly")

TEMPLATE = "plotly_dark"  # "ggplot2", "seaborn", "simple_white", "plotly", "plotly_white", "plotly_dark", "presentation", "xgridoff", "ygridoff", "gridon", "none"

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")

fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation",
    ))
fig.layout.autosize = True
fig.update_layout(template=TEMPLATE, title=f"Mt Bruno Elevation in a '{TEMPLATE}' template")

plot_plotly_2 = pn.pane.Plotly(fig, height=500, sizing_mode="stretch_width")#.servable()




import panel as pn

from vega_datasets import data

pn.extension("vega")

VEGA_ACCENT_COLOR = "#F08080"
VEGA_THEME = {
    "background": "#333",
    "title": {"color": "#fff"},
    "style": {"guide-label": {"fill": "#fff"}, "guide-title": {"fill": "#fff"}},
    "axis": {"domainColor": "#fff", "gridColor": "#888", "tickColor": "#fff"},
}

vegalite = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "A simple bar chart with rounded corners at the end of the bar.",
    "width": "container",
    "height": 300,
    "data": {
    "values": [
        {"a": "A", "b": 28},
        {"a": "B", "b": 55},
        {"a": "C", "b": 43},
        {"a": "D", "b": 91},
        {"a": "E", "b": 81},
        {"a": "F", "b": 53},
        {"a": "G", "b": 19},
        {"a": "H", "b": 87},
        {"a": "I", "b": 52}
    ]
    },
    "mark": {"type": "bar", "cornerRadiusEnd": 4, "tooltip": True},
    "encoding": {
        "x": {"field": "a", "type": "ordinal"},
        "y": {"field": "b", "type": "quantitative"},
        "color": {"value": VEGA_ACCENT_COLOR}
    },
}

vegalite["config"] = VEGA_THEME

plot_vega = pn.pane.Vega(vegalite, height=350, sizing_mode="stretch_width")#.servable()
"""
"""

pn.extension(design='material', global_css=[':root { --design-primary-color: purple; }'])

some_tabs = pn.Tabs(
    ('Slider', pn.widgets.FloatSlider(start=0, end=7, value=3)),
    ('Button', pn.widgets.Button(name='Click me!', button_type='primary'))
)

some_more_tabs = pn.Tabs(
    ('Slider', pn.widgets.FloatSlider(
        start=0, end=7, value=3, stylesheets=[':host { --design-primary-color: red; }']
        )),
    ('Button', pn.widgets.Button(name='Click me!', button_type='primary'))
)

custom_style = {
    'background': '#f9f9f9',
    'border': '1px solid black',
    'padding': '10px',
    'box-shadow': '5px 5px 5px #bcbcbc'
}

stylesheet1 = """
:host {
  --slider-size: 5px;
  --handle-width: 16px;
  --handle-height: 16px;
}

.noUi-handle {
  border-radius: 100%;
  box-shadow: unset;
  background-color: #0081f3;
}
"""


slider1 = pn.widgets.FloatSlider(
    name='Number', styles=custom_style, stylesheets=[stylesheet1]
)

slider2 = pn.widgets.FloatSlider(
    name='Number', stylesheets=['https://assets.holoviz.org/panel/how_to/styling/noUi.css']
)

color_stylesheet = """
:host(.red) .noUi-handle {
  background-color: red
}

:host(.green) .noUi-handle {
  background-color: green
}

:host(.blue) .noUi-handle {
  background-color: blue
}
"""

sliders345 = pn.Column(
    *(pn.widgets.FloatSlider(name='Number', stylesheets=[stylesheet1, color_stylesheet], css_classes=[cls])
      for cls in ('red', 'green', 'blue'))
)

text = (
    "This is a **{alert_type}** alert with [an example link]"
    "(https://panel.holoviz.org/). Give it a click if you like."
)

alerts = pn.Column(*[
    pn.pane.Alert(text.format(alert_type=at), alert_type=at)
    for at in pn.pane.Alert.param.alert_type.objects],
    sizing_mode="stretch_width"
)

df = pd.DataFrame({
    'int': [1, 2, 3],
    'float': [3.14, 6.28, 9.42],
    'str': ['A', 'B', 'C'],
    'bool': [True, False, True],
}, index=[1, 2, 3])

df_pane = pn.pane.DataFrame(df, width=400)



import folium
pn.extension(sizing_mode="stretch_both")
fol_map = folium.Map(location=[52.51, 13.39], zoom_start=12)
folium_pane = pn.pane.plot.Folium(
    fol_map,
    height=400,
    min_height=400,
    #stretch_both=True,
    #stretch_width=True,
    #stretch_heith=True,
    height_policy='min', 
)

fp = pn.pane.plot.Folium()


styles = {
    'background-color': '#F6F6F6', 'border': '2px solid black',
    'border-radius': '5px', 'padding': '10px'
}

html_pane = pn.pane.HTML("""
<h1>This is an HTML pane</h1>

<code>
x = 5;<br>
y = 6;<br>
z = x + y;
</code>

<br>
<br>

<table>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>
""", styles=styles)

one = pn.pane.Markdown('''
# H1
## H2
### H3
''')


my_id = str(uuid.uuid4())[:4]
print(my_id)


# Instantiate the template with widgets displayed in the sidebar
template = pn.template.MaterialTemplate(
    title='Template {}'.format(my_id),
    sidebar=[
        pn.Tabs(
            #pn.Card(plot_echarts, title='echarts', name='echarts'),
            #pn.Column(
            #pn.Card(slider1, name='slider 1'),
            #pn.Card(slider2, name='slider 2'),
             pn.Column(html_pane, name='html'),
            pn.Column(one, name='markdown'),
            pn.Column(fol_map, name='folium map', min_height=500, height=100),
            pn.Column(slider1, slider2, sliders345, name='sliders'),
            pn.Column(alerts, name='alerts'),
            pn.Column(df_pane, name='dataframe'),
            #slider2,
            #sliders345
            tabs_location='left',
            #width=300,
            
        )
    ],
    sidebar_width=500,
    logo='https://github.com/rea725/superset-images/blob/main/plaidcloud-white.png?raw=true',
    favicon='https://plaidcloud.com/wp-content/uploads/2021/10/cropped-favicon-32x32.png',
    header_background='#002F6C',
)

# Append a layout to the main area, to demonstrate the list-like API
template.main.append(
    pn.Row(
        pn.Tabs(
            pn.Card(fol_map, title='folium map', name='folium map', height=500),
            pn.Card(plot_altair, title='altair', name='altair'),
            pn.Card(plot_echarts, title='echarts', name='echarts'),
            pn.Card(plot_mpl, title='matplotlib', name='matplotlib'),
            pn.Card(plot_plotly_1, title='plotly_1', name='plotly_1'),
            pn.Card(plot_plotly_2, title='plotly_2', name='plotly_2'),
            pn.Card(plot_vega, title='vega', name='vega'),
            #pn.Card(plot_mpl, title='matplotlib'),
            #pn.Card(sliders345, title='sliders345'),
            #pn.Card(plot_altair, title='altair'),
            #pn.Card(plot_echarts, title='echarts'),
            tabs_location='right',
        ),
    ),


    #pn.Row(
        #pn.Card(plot_mpl, title='plot_plotly_1'),
        #pn.Card(plot_mpl, title='plot_plotly_2'),
    #), 
)


m = folium.Map(location=[52.51, 13.39], zoom_start=12)

folium_pane = pn.pane.plot.Folium(m, height=600)




if pn.state.served:
    template.servable()
    #folium_pane.servable()
