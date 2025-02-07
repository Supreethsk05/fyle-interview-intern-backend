import pytest
from core.models.assignments import Assignment
from core import db


def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2
        
        
@pytest.fixture
def transaction_block(request):
    db.session.begin(subtransactions=True)
    request.addfinalizer(db.session.rollback)

def test_post_assignment_null_content(client, h_student_1):
    """
    failure case: content cannot be null
    """

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': None
        })

    assert response.status_code == 400

@pytest.mark.usefixtures("transaction_block")
def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None

@pytest.mark.usefixtures("transaction_block")
def test_submit_assignment_student_1(client, h_student_1):
    Assignment.query.filter_by(id=2).update({'state': 'DRAFT', 'teacher_id': None})
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 2

@pytest.mark.usefixtures("transaction_block")
def test_assignment_resubmit_error(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 1,
            'teacher_id': 2
        })
    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'only a draft assignment can be submitted'

@pytest.mark.usefixtures("transaction_block")
def test_upsert_assignment_edit(client, h_student_1):
    """
    success case: check if the student can edit an existing assignment
    """
    content = 'ABCD UpdatePost'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 2,
            'content': content
        }
    )

    assert response.status_code == 200
    data = response.json['data']
    assert data['content'] == content