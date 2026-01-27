from flask import Blueprint, request, jsonify
from ..services.issue_service import create_issue

student_bp = Blueprint("student", __name__)

@student_bp.route("/issues", methods=["POST"])
def submit_issue():
    data = request.get_json()

    required_fields = ["title", "description", "student_name"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    if len(data["title"]) < 5:
        return jsonify({"error": "Title too short"}), 400

    if len(data["description"]) < 10:
        return jsonify({"error": "Description too short"}), 400

    issue = create_issue(data)

    return jsonify(issue.to_dict()), 201
