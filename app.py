import os
import shortuuid
from flask import Flask, request, redirect, jsonify, render_template
from dotenv import load_dotenv
from models import db, URL

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Flask & MySQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Home page – HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('original_url')
    if not original_url:
        return jsonify({'error': 'No URL provided'}), 400

    # Generate short ID and save
    short_id = shortuuid.uuid()[:6]
    url = URL(original_url=original_url, short_id=short_id)
    db.session.add(url)
    db.session.commit()

    return jsonify({'short_url': f'{os.getenv("BASE_URL")}/{short_id}'}), 201

# Redirect to original URL
@app.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    url = URL.query.filter_by(short_id=short_id).first()
    if not url:
        return jsonify({'error': 'URL not found'}), 404

    url.clicks += 1
    db.session.commit()
    return redirect(url.original_url)

# URL stats
@app.route('/stats/<short_id>', methods=['GET'])
def url_stats(short_id):
    url = URL.query.filter_by(short_id=short_id).first()
    if not url:
        return jsonify({'error': 'URL not found'}), 404

    return jsonify({
        'original_url': url.original_url,
        'short_id': url.short_id,
        'clicks': url.clicks
    })

if __name__ == '__main__':
    app.run(debug=True)
