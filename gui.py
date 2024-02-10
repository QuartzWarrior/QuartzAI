from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def gui():
    return await render_template('gui.html')

if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0", use_reloader=True, debug=True)
