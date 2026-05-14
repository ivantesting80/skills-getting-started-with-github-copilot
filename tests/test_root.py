def test_root_redirects_to_static_index(client):
    # Arrange
    # (client fixture provided)

    # Act
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location") == "/static/index.html"
