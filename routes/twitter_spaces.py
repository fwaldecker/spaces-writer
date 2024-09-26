from flask import Blueprint, request, jsonify
from services.ffmpeg_processing import process_conversion

twitter_bp = Blueprint('twitter_spaces', __name__)


@twitter_bp.route('/twitter_spaces/submit', methods=['POST'])
def submit():
    """Handles the form submission for converting Twitter Spaces audio"""
    twitter_url = request.form.get('twitter_url')
    job_id = 'twitter_job_001'  # Generate a unique job ID in your actual implementation
    try:
        result = process_conversion(twitter_url, job_id)
        return jsonify({'status': 'success', 'output': result})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
