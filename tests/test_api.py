from app.main import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_price_endpoint_applies_bulk_discount():
    client = app.test_client()

    response = client.get("/price?unit_price=10&quantity=10")

    assert response.status_code == 200
    assert response.get_json() == {
        "quantity": 10,
        "total": 90.0,
        "unit_price": 10.0,
    }


def test_price_endpoint_rejects_missing_parameters():
    client = app.test_client()

    response = client.get("/price?quantity=10")

    assert response.status_code == 400
