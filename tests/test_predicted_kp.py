import json


def test_predicted_kp(client):
    response = client.get('/predicted-kp-index')
    res = response.data.decode()
    output = json.loads(res)
    assert "highest_predicted_kp_index" in output.keys()
    assert "noaa_scale" in output.keys()
    assert response.status_code == 200


def test_get_predicted_kp_index_with_time_stamp(client, time_stamp):
    response = client.get(f'/predicted-kp-index?time_stamp={time_stamp}')
    assert response.status_code == 200