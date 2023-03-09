from bokeh.models import ColorBar, ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap

x = list(range(1, 11))
y = list(range(1, 11))

source = ColumnDataSource(dict(x=x,y=y))

p = figure(width=600, height=600, title="Linear color map based on Y")

# use the field name of the column source
cmap = linear_cmap(field_name='y', palette="Spectral6", low=min(y), high=max(y))

p.scatter(x='x', y='y', color=cmap, size=25, source=source)

# pass the mapper's transform to the colorbar
color_bar = ColorBar(color_mapper=cmap['transform'], width=25)

p.add_layout(color_bar, 'right')

show(p)
