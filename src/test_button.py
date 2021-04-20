import pandas as pd

def test_update_button():
    df = pd.DataFrame(
        dict(temperature=[24, 26, 28], ice_cream_cones=[14, 20, 23], drinks=[18, 22, 28])
    )
    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.temperature,
            y=df.ice_cream_cones,
            name="Ice Cream",
            marker_color="#2457BD",
        ),
    )
    fig.add_trace(
        go.Scatter(
            x=df.temperature,
            y=df.drinks,
            name="Drinks",
            marker_color="#F0B729",
        )
    )


    fig.update_layout(
        template="simple_white",
        xaxis=dict(title_text="Temperature [°C]"),
        yaxis=dict(title_text="Units Sold"),
    )
    df["scoops"] = df["ice_cream_cones"] * 2

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.7,
                y=1.2,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Cones",
                            method="update",
                            args=[{"y": [df["ice_cream_cones"], df["drinks"]]}],
                        ),
                        dict(
                            label="Scoops",
                            method="update",
                            args=[{"y": [df["scoops"], df["drinks"]]}],
                        ),
                    ]
                ),
            )
        ]
    )
    return fig
