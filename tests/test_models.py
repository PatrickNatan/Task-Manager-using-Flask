from todo_project import create_app, db
from todo_project.models import User, Task

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    user1 = User(username='testuser1', password='password1')
    user2 = User(username='testuser2', password='password2')
    db.session.add(user1)
    db.session.add(user2)

    task1 = Task(content='Test task 1', user_id=1)
    task2 = Task(content='Test task 2', user_id=2)
    db.session.add(task1)
    db.session.add(task2)

    db.session.commit()

    yield

    db.drop_all()

# tests/test_models.py
from todo_project.models import User, Task

def test_new_user():
    user = User(username='testuser', password='testpassword')
    assert user.username == 'testuser'
    assert user.password == 'testpassword'

def test_new_task():
    task = Task(content='Test task', user_id=1)
    assert task.content == 'Test task'
    assert task.user_id == 1

# tests/test_routes.py
def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Todo App" in response.data

def test_create_task(test_client, init_database):
    response = test_client.post('/create',
                                data=dict(content='A new test task'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Task created successfully" in response.data