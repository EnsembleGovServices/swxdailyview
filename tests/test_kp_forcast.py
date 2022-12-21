import json

# if time_stamp is not provided it will take current timestamp automatically
def test_current_kp_index_status(client):
    response = client.get('/current-kp-index')
    res = response.data.decode()
    output = json.loads(res)
    assert "kp_index" in output.keys()
    assert response.status_code == 200

def test_current_kp_index_with_time_stamp(client, time_stamp):
    response = client.get(f'/current-kp-index?time_stamp={time_stamp}')
    res = response.data.decode()
    output = json.loads(res)
    assert "kp_index" in output.keys()
    assert response.status_code == 200