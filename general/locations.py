import http.client, urllib.parse
import requests
def generate_request(url,query,region):

        params = urllib.parse.urlencode({
        'access_key': '29317752d1863d61aaa79a5113839b2f',
        'query': query,
        'region': region,
        'limit': 1,
        })

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

def get_location(query,region):
        response = generate_request('http://api.positionstack.com/v1/forward?access_key=29317752d1863d61aaa79a5113839b2f',query,region)
        if response:
            data = (response.get('data')[0])
            locate = {
                'latitude' : data.get('latitude'),
                'longitude' : data.get('longitude'),
                'region' : data.get('region'),
                'country_code' : data.get('country_code'),    
            }
           

            return locate

    


if __name__ == '__main__':
    print(get_location('Atanasio Girardot','Medellin'))
  