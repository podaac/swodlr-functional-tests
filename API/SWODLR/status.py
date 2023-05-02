import requests


class Status():
    
    def GetStatus() -> requests.response:
        print(f'\r\nGetting Status...')

        url = conf.Cumulus_baseurl + endpoint

        custom_header = {
            "Content-Type": "application/json" }
        if authorizationHeader:
            custom_header["Authorization"] = f"Bearer {FileHandler.GetLaunchpadToken()}"
        if invalidData:
            custom_header["Authorization"] = "Bearer asd"

        response = requests.get(
            url = url,
            headers = custom_header)

        print(f"Response: {response.status_code}")
        if response.status_code != 200:
            print(f"Response text:\r\n{response.text}\r\n")
            print(f"Request url:\r\n{response.request.url}\r\n")
        
        return response