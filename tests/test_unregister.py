def test_unregister_success(client):
    # Arrange
    email = "john@mergington.edu"  # present in Gym Class per fixtures
    activity = "Gym Class"

    # Act
    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Removed" in data.get("message", "")

    # Verify participant was removed
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange / Act
    resp = client.post(f"/activities/Nope/unregister", params={"email": "x@x.com"})

    # Assert
    assert resp.status_code == 404


def test_unregister_missing_participant_returns_404(client):
    # Arrange / Act
    resp = client.post(f"/activities/Chess Club/unregister", params={"email": "notfound@example.com"})

    # Assert
    assert resp.status_code == 404
