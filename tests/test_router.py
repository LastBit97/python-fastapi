from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_combine_files():
    files = [('files', open('test_data/file1.csv', 'rb')), ('files', open('test_data/file2.json', 'rb'))]
    response = client.post(
        url="/upload/test.csv",
        files=files
    )
    assert response.status_code == 200
    assert response.json() == {"filename": "test.csv"}


def test_combine_files_415():
    files = [('files', open('test_data/file3.txt', 'rb')), ('files', open('test_data/file2.json', 'rb'))]
    response = client.post(
        url="/upload/test.csv",
        files=files
    )
    assert response.status_code == 415


def test_load_file():
    response = client.get("/load/example.csv")
    assert response.status_code == 200


def test_load_file_404():
    response = client.get("/load/qwerty.csv")
    assert response.status_code == 404


def test_filter():
    response = client.post(
        "/filter/case_sensitive",
        json=["Мама", "МАМА", "Мама", "папа", "ПАПА", "ДЯдя", "брАт", "Дядя", "Дядя"],
    )
    assert response.status_code == 200
