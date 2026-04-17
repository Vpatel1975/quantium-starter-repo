from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualiser", timeout=10)


def test_chart_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element(".js-plotly-plot", timeout=10)


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
