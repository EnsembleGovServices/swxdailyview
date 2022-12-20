import json

def test_get_high_latitude_minor_key(client):
    response = client.get('/get-high-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "minor" in output.keys()

def test_get_high_latitude_moderate_key(client):
    response = client.get('/get-high-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "moderate" in output.keys()

def test_get_high_latitude_strong_key(client):
    response = client.get('/get-high-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "strong" in output.keys()

def test_get_high_latitude_severe_key(client):
    response = client.get('/get-high-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "severe" in output.keys()

def test_get_high_latitude_extreme_key(client):
    response = client.get('/get-high-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "extreme" in output.keys()