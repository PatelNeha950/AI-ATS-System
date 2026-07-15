import plotly.graph_objects as go


def circular_score(score):

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text":"ATS Score"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"green"},

                "steps":[

                    {"range":[0,40],"color":"red"},

                    {"range":[40,70],"color":"orange"},

                    {"range":[70,100],"color":"lightgreen"}

                ]

            }

        )
    )

    fig.update_layout(height=300)

    return fig