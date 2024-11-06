from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route to render the portfolio form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect the data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        linkedin = request.form.get('linkedin')
        college = request.form.get('college')

        # Here you can process the data, like saving it to a database or sending an email
        # For now, we will just print the data and redirect to a success page
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"LinkedIn: {linkedin}")
        print(f"College: {college}")

        return redirect(url_for('success'))

# Route to display a success message after form submission
@app.route('/success')
def success():
    return "Your portfolio details have been successfully submitted!"

if __name__ == '__main__':
    app.run(debug=True)
