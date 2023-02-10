import requests
from time import gmtime, strftime

class TestNewFileHeader:
    def test_header(self):
        time_value = strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
        #print(strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime()))
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        assert "Date" in response.headers, "There is not field 'Date' in the response headers"
        date_value = response.headers.get('Date')
        assert date_value == time_value, f"Header Date is not equal {time_value}"

        assert "Content-Type" in response.headers, "There is not field 'Content-Type' in the response headers"
        content_type_value = response.headers.get('Content-Type')
        assert content_type_value == "application/json", "Header Content-Type is not equal application/json"

        assert "Content-Length" in response.headers, "There is not field 'Content-Length' in the response headers"
        content_length_value = response.headers.get('Content-Length')
        assert content_length_value == "15", "Header Content-Length is not equal 15"

        assert "Connection" in response.headers, "There is not field 'Connection' in the response headers"
        connection_value = response.headers.get('Connection')
        assert connection_value == "keep-alive", "Header Connection is not equal keep-alive"

        assert "Keep-Alive" in response.headers, "There is not field 'Keep-Alive' in the response headers"
        keep_alive_value = response.headers.get('Keep-Alive')
        assert keep_alive_value == "timeout=10", "Header Keep-Alive is not equal timeout=10"

        assert "Server" in response.headers, "There is not field 'Server' in the response headers"
        server_value = response.headers.get('Server')
        assert server_value == "Apache", "Header Server is not equal Apache"

        assert "x-secret-homework-header" in response.headers, "There is not field 'x-secret-homework-header' in the response headers"
        x_secret_homework_header_value = response.headers.get('x-secret-homework-header')
        assert x_secret_homework_header_value == "Some secret value", "Header x-secret-homework-header is not equal Some secret value"

        assert "Cache-Control" in response.headers, "There is not field 'Cache-Control' in the response headers"
        cache_control_value = response.headers.get('Cache-Control')
        assert cache_control_value == "max-age=0", "Header Cache-Control is not equal max-age=0"

        assert "Expires" in response.headers, "There is not field 'Expires' in the response headers"
        expires_value = response.headers.get('Expires')
        assert expires_value == time_value, f"Header Expires is not equal {time_value}"

