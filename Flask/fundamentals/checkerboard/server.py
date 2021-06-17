from flask import Flask, render_template;

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:rows>')
def spec_rows(rows):
    return render_template('rows.html', rows=rows)

@app.route('/<int:rows>/<int:cols>')
def spec_rows_and_cols(rows, cols):
    return render_template('rows_and_cols.html', rows=rows, cols=cols)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.