import json


def test_get_interval_kp_data(client):
    response = client.get('/get-interval-kp-data')
    res = response.data.decode()
    output = json.loads(res)
    assert "00-03" in output[0].keys()
    assert "06-09" in output[2].keys()
    assert "03-06" in output[1].keys()
    assert "09-12" in output[3].keys()
    assert "12-15" in output[4].keys()
    assert "15-18" in output[5].keys()
    assert "18-21" in output[6].keys()
    assert "21-00" in output[7].keys()
    assert response.status_code == 200

def test_get_interval_kp_data_with_time_stamp(client, time_stamp):
    response = client.get(f'/get-interval-kp-data?time_stamp={time_stamp}')
    assert response.status_code == 200