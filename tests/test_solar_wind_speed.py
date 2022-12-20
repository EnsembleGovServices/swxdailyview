import json


def test_get_solar_wind_speed_res_key(client):
    response = client.get('/get-solar-wind-speed')
    res = response.data.decode()
    output = json.loads(res)
    assert "avg_bt" in output.keys()


def test_get_solar_wind_speed_time_data_validation(client, time_stamp):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp1(client, time_stamp_1hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_1hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp0(client, time_stamp_0hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_0hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp2(client, time_stamp_2hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_2hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp3(client, time_stamp_3hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_3hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp4(client, time_stamp_4hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_4hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp5(client, time_stamp_5hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_5hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp6(client, time_stamp_6hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_6hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp7(client, time_stamp_7hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_7hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp8(client, time_stamp_8hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_8hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp9(client, time_stamp_9hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_9hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp10(client, time_stamp_10hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_10hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp11_validation(client, time_stamp_11hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_11hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp12(client, time_stamp_12hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_12hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp13(client, time_stamp_13hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_13hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp14(client, time_stamp_14hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_14hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp15(client, time_stamp_15hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_15hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp16(client, time_stamp_16hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_16hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp17(client, time_stamp_17hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_17hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp18(client, time_stamp_18hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_18hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp19(client, time_stamp_19hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_19hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp20(client, time_stamp_20hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_20hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp21(client, time_stamp_21hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_21hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp22(client, time_stamp_22hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_22hour}')
    assert response.status_code == 200

def test_get_solar_wind_time_stamp23(client, time_stamp_23hour):
    response = client.get(f'/get-solar-wind-speed?time_stamp={time_stamp_23hour}')
    assert response.status_code == 200
