AttributeError at /
'Map' object has no attribute '_repr_'

i solved by using
m = m._repr_html_()
