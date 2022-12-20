import json

def test_get_mid_latitude_minor_key(client):
    response = client.get('/get-mid-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "minor" in output.keys()

def test_get_mid_latitude_moderate_key(client):
    response = client.get('/get-mid-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "moderate" in output.keys()

def test_get_mid_latitude_strong_key(client):
    response = client.get('/get-mid-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "strong" in output.keys()

def test_get_mid_latitude_severe_key(client):
    response = client.get('/get-mid-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "severe" in output.keys()

def test_get_mid_latitude_extreme_key(client):
    response = client.get('/get-mid-latitude')
    res = response.data.decode()
    output = json.loads(res)
    assert "extreme" in output.keys()