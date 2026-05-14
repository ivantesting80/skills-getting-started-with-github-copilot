def test_get_activities(client):
    # Arrange
    # (client fixture provided)

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    # Some known activities should be present
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Basketball Team" in data
