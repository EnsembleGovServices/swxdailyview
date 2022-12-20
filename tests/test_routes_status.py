def test_root_route(client):
    response = client.get('/')
    assert response.status_code == 200


def test_current_kp_index_status(client):
    response = client.get('/current-kp-index')
    assert response.status_code == 200


def test_get_interval_kp_data_status(client):
    response = client.get('/get-interval-kp-data')
    assert response.status_code == 200


def test_predicted_kp_index_status(client):
    response = client.get('/predicted-kp-index')
    assert response.status_code == 200


def test_goes_proton_flux_status(client):
    response = client.get('/get-proton-flux-data')
    assert response.status_code == 200


def test_get_mid_latitude_status(client):
    response = client.get('/get-mid-latitude')
    assert response.status_code == 200


def test_get_high_latitude_status(client):
    response = client.get('/get-high-latitude')
    assert response.status_code == 200

def test_get_mid_latitude_with_given_timestamp(client, time_stamp):
    response = client.get(f'/get-mid-latitude?time_stamp={time_stamp}')
    assert response.status_code == 200


def test_get_high_latitude_with_given_timestamp(client, time_stamp):
    response = client.get(f'/get-high-latitude?time_stamp={time_stamp}')
    assert response.status_code == 200


def test_get_solar_wind_speed(client):
    response = client.get('/get-solar-wind-speed')
    assert response.status_code == 200

def test_get_solar_wind_speed_with_given_timestamp(client, time_stamp):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp}')
    assert response.status_code == 200


def test_goes_proton_flux_status_with_given_time_stamp(client, time_stamp):
    response = client.get(f'/get-proton-flux-data?time_stamp={time_stamp}')
    assert response.status_code == 200
