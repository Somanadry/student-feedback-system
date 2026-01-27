from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ..services.issue_service import get_all_issues, update_issue_status

admin_bp = Blueprint("admin", __name__)


# 🔹 Get all issues (Admin only)
@admin_bp.route("/issues", methods=["GET"])
@jwt_required()
def list_issues():
    username = get_jwt_identity()
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Unauthorized"}), 403

    issues = get_all_issues()
    return jsonify([issue.to_dict() for issue in issues])


# 🔹 Update issue status (Admin only)
@admin_bp.route("/issues/<int:issue_id>/status", methods=["PUT"])
@jwt_required()
def change_status(issue_id):
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()

    if not data or "status" not in data or "admin_name" not in data:
        return jsonify({"error": "Missing status or admin_name"}), 400

    issue = update_issue_status(issue_id, data["status"], data["admin_name"])

    if not issue:
        return jsonify({"error": "Issue not found"}), 404

    return jsonify({
        "message": "Status updated",
        "issue_id": issue.id,
        "new_status": issue.status
    })
