import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, students_factory, course_factory):
    students = students_factory(_quantity=10)
    course = course_factory(name='Python', students=students)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data[0]['students']) == 10
    assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_course_by_id(client, course_factory):
    courses = course_factory(_quantity=5)
    test_id = courses[2].id

    response = client.get(f'/api/v1/courses/?id={test_id}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == test_id


@pytest.mark.django_db
def test_filter_course_by_name(client, course_factory):
    courses = course_factory(_quantity=5)
    test_name = courses[2].name

    response = client.get(f'/api/v1/courses/?name={test_name}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == test_name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'Python'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(name='Python')

    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'JS'})
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == 'JS'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(name='Python')
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1
