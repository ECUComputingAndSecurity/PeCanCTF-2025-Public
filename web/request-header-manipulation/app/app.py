from flask import Flask, request

app = Flask(__name__, static_url_path='')

# Define the required headers and their expected values
REQUIRED_HEADERS = {
    "User-Agent": ("Cheese", "I only trust users of the 'Cheese' browser"),
    "Accept-Language": ("1337", "I will only reply to those that accept '1337' as their language of choice"),
    "Accept": ("flag", "I can't believe your not even going to accept a 'flag' instead of text/html or even worse */*"),
    "Date": ("Thu, 01 Jan 1970 00:00:00 GMT", "If the message wasn't sent at the exact time of the Unix Epoch, then I don't care"),
    "Referer": ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Go rick roll yourself, then refer back to here"),
    "ECT": ("5g", "Are you even going to be using an effective connection of 5g?"),
    "From": ("", "What email is this request even from?")
}

FLAG = "pecan{HTTP_r3q35st_h34d3r5_c4n_g3t_qu1t3_w13rd_4nd_5p3c1f1c}"

def error403(clue: str):
	return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>403 Forbidden</title>
        <style>
            body {{
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            h1 {{
                font-size: 5em;
                margin-bottom: 0.2em;
                color: #ff4c4c;
            }}
            p {{
                font-size: 1.5em;
                text-align: center;
                max-width: 600px;
                line-height: 1.4;
            }}
            .container {{
                text-align: center;
                padding: 20px;
                background-color: #2a2a3b;
                border: 1px solid #444;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>403</h1>
            <p>{clue}</p>
        </div>
    </body>
    </html>
    """

@app.route('/')
def index():
	# Check for each required header
	for header, (expected_value, clue) in REQUIRED_HEADERS.items():
		actual_value = request.headers.get(header)
		if (expected_value and (actual_value != expected_value)) or (not expected_value and not actual_value):
			return error403(clue)  # Forbidden with clue as message 

	# All headers match, return the flag
	return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>403 Forbidden</title>
        <style>
            body {{
                background-color: #1e1e2f;
                color: #ffffff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            h1 {{
                font-size: 5em;
                margin-bottom: 0.2em;
                color: #ff4c4c;
            }}
            p {{
                font-size: 1.5em;
                text-align: center;
                max-width: 600px;
                line-height: 1.4;
            }}
            .container {{
                text-align: center;
                padding: 20px;
                background-color: #2a2a3b;
                border: 1px solid #444;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Flag</h1>
            <p>{FLAG}</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
