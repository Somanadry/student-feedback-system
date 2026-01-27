from ..models.issue import Issue
from ..extensions import db
from ..ai.categorizer import categorize_issue
from ..ai.summarizer import summarize_issue


def create_issue(data):
    description = data.get("description", "")

    category = categorize_issue(description)
    summary = summarize_issue(description)

    issue = Issue(
        title=data.get("title"),
        description=description,
        student_name=data.get("student_name"),
        department=data.get("department"),
        category=category,
        ai_summary=summary,
    )

    db.session.add(issue)
    db.session.commit()
    return issue



def get_all_issues():
    return Issue.query.order_by(Issue.created_at.desc()).all()


from ..models.status_log import StatusLog

def update_issue_status(issue_id, new_status, admin_name):
    issue = Issue.query.get(issue_id)

    if not issue:
        return None

    old_status = issue.status
    issue.status = new_status

    log = StatusLog(
        issue_id=issue.id,
        old_status=old_status,
        new_status=new_status,
        changed_by=admin_name,
    )

    db.session.add(log)
    db.session.commit()

    return issue
