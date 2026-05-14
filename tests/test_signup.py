def test_signup_success(client):
    # Arrange
    email = "tester@example.com"
    activity = "Chess Club"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Signed up" in data.get("message", "")

    # Verify participant was added
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    email = "emma@mergington.edu"  # already in Programming Class
    activity = "Programming Class"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_signup_unknown_activity_returns_404(client):
    # Arrange / Act
    resp = client.post(f"/activities/Nonexistent/signup", params={"email": "a@b.com"})

    # Assert
    assert resp.status_code == 404
