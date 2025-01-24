import os
from dash import Dash, html, dcc, Input, Output, State
from ai import model

# Fetch the API key from environment variables
if "GEMINI_API_KEY" not in os.environ:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set!")

# Initialize Dash app
app = Dash(__name__)
app.title = "Which is Bigger?"

# Define the layout
app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "textAlign": "center", "padding": "50px"},
    children=[
        html.H1("Which is Bigger?"),
        html.P("Enter two numbers below, and let AI determine the larger number!"),
        dcc.Input(id="num1", type="number", placeholder="Enter first number", style={"marginRight": "10px"}),
        dcc.Input(id="num2", type="number", placeholder="Enter second number", style={"marginRight": "10px"}),
        html.Button("Compare", id="compare-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Div(id="result", style={"marginTop": "20px", "fontSize": "20px", "color": "blue"}),
    ],
)

# Define callback for the compare button
@app.callback(
    Output("result", "children"),
    Input("compare-btn", "n_clicks"),
    State("num1", "value"),
    State("num2", "value"),
)
def compare_numbers(n_clicks, num1, num2):
    if n_clicks > 0:
        if num1 is None or num2 is None:
            return "Please enter valid numbers."
        
        try:
            chat_session = model.start_chat(
                history=[{"role": "user", "parts": [f"What is bigger, {num1} or {num2}?"]}]
            )
            response = chat_session.send_message(f"What is bigger, {num1} or {num2}?")
            return response.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"
    return ""

# Run the app
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True,port=8082)