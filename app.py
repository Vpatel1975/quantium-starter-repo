import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "output.csv"))
df["date"] = pd.to_datetime(df["date"])
df_sorted = df.groupby("date")["sales"].sum().reset_index().sort_values("date")

fig = px.line(
    df_sorted,
    x="date",
    y="sales",
    labels={"date": "Date", "sales": "Total Sales ($)"},
)
price_increase_date = pd.Timestamp("2021-01-15").timestamp() * 1000
fig.add_vline(
    x=price_increase_date,
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase (15 Jan 2021)",
    annotation_position="top left",
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
