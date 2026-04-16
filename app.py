import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "output.csv"))
df["date"] = pd.to_datetime(df["date"])

PRICE_INCREASE_DATE = pd.Timestamp("2021-01-15").timestamp() * 1000

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "'Segoe UI', sans-serif",
        "backgroundColor": "#0f1117",
        "minHeight": "100vh",
        "padding": "40px",
    },
    children=[
        html.Div(
            style={"textAlign": "center", "marginBottom": "32px"},
            children=[
                html.H1(
                    "Pink Morsel Sales Visualiser",
                    style={
                        "color": "#ff6eb4",
                        "fontSize": "2.4rem",
                        "letterSpacing": "0.05em",
                        "margin": "0 0 8px 0",
                    },
                ),
                html.P(
                    "Soul Foods — Sales before vs after the price increase of 15 Jan 2021",
                    style={"color": "#888", "fontSize": "0.95rem", "margin": 0},
                ),
            ],
        ),
        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "28px",
            },
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All Regions", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"color": "#ccc", "fontSize": "0.95rem"},
                    inputStyle={"marginRight": "6px", "accentColor": "#ff6eb4"},
                    labelStyle={"marginRight": "24px", "cursor": "pointer"},
                ),
            ],
        ),
        html.Div(
            style={
                "backgroundColor": "#1a1d27",
                "borderRadius": "12px",
                "padding": "16px",
                "boxShadow": "0 4px 24px rgba(0,0,0,0.4)",
            },
            children=[dcc.Graph(id="sales-chart")],
        ),
    ],
)


@app.callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    grouped = filtered.groupby("date")["sales"].sum().reset_index().sort_values("date")

    fig = px.line(
        grouped,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        color_discrete_sequence=["#ff6eb4"],
    )
    fig.add_vline(
        x=PRICE_INCREASE_DATE,
        line_dash="dash",
        line_color="#ff4444",
        annotation_text="Price Increase (15 Jan 2021)",
        annotation_position="top left",
        annotation_font_color="#ff4444",
    )
    fig.update_layout(
        paper_bgcolor="#1a1d27",
        plot_bgcolor="#1a1d27",
        font_color="#cccccc",
        xaxis=dict(gridcolor="#2e3145", zerolinecolor="#2e3145"),
        yaxis=dict(gridcolor="#2e3145", zerolinecolor="#2e3145"),
        margin=dict(l=40, r=40, t=20, b=40),
        hovermode="x unified",
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
