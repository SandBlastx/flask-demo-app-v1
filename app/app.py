"""
Flask application demonstrating transitive dependency vulnerability.

This app DOES NOT import jinja2 directly - it only imports Flask.
Jinja2 is a transitive dependency through Flask.
The vulnerability is in the |xmlattr filter used in the template.
"""

from flask import Flask, render_template, request

# Note: We are NOT importing jinja2 directly
# It comes as a transitive dependency through Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route that accepts user attributes and renders them using xmlattr filter.
    This demonstrates how a vulnerability in a transitive dependency (Jinja2)
    can affect the application.
    """
    user_attrs = {}
    
    if request.method == 'POST':
        # Collect all form data as attributes
        user_attrs = request.form.to_dict()
    
    return render_template('index.html', user_attrs=user_attrs)


@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'healthy', 'message': 'Flask app running'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
