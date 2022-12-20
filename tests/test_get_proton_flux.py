import json


def test_get_proton_flux_output_keys_six_hours(client):
    response = client.get('/get-proton-flux-data?hours=6')
    res = response.data.decode()
    output = json.loads(res)
    assert "gt_10" in output.keys()
    assert "gt_50" in output.keys()
    assert "gt_100" in output.keys()
    assert response.status_code == 200

def test_get_proton_flux_output_keys_in_one_day(client):
    response = client.get('/get-proton-flux-data?days=1')
    res = response.data.decode()
    output = json.loads(res)
    assert "gt_10" in output.keys()
    assert "gt_50" in output.keys()
    assert "gt_100" in output.keys()
    assert response.status_code == 200

def test_get_proton_flux_output_keys_in_three_days(client):
    response = client.get('/get-proton-flux-data?days=3')
    res = response.data.decode()
    output = json.loads(res)
    assert "gt_10" in output.keys()
    assert "gt_50" in output.keys()
    assert "gt_100" in output.keys()
    assert response.status_code == 200

def test_get_proton_flux_output_keys_in_seven_days(client):
    response = client.get('/get-proton-flux-data?days=7')
    res = response.data.decode()
    output = json.loads(res)
    print("++++this is output:", output)
    assert "gt_10" in output.keys()
    assert "gt_50" in output.keys()
    assert "gt_100" in output.keys()
    assert response.status_code == 200

def test_given_param_is_valid(client):
    response = client.get('/get-proton-flux-data?day=7')
    res = response.data.decode()
    output = json.loads(res)
    assert "Requested Interval is invalid You have only [ 6 hours, 1/3/7 days options]" == output['error']

def test_given_days_param(client):
    response = client.get('/get-proton-flux-data?days=9')
    res = response.data.decode()
    output = json.loads(res)
    assert 'Days requested must be 1 day, 3 day or 7 day only.' == output['error']

def test_given_hours_parameter(client):
    response = client.get('/get-proton-flux-data?hours=7')
    res = response.data.decode()
    output = json.loads(res)
    assert 'Hours requested must be 6 hours only.' == output['error']