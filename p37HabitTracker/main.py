import requests
from datetime import datetime

userAPIurl = "https://pixe.la/v1/users"
user_params = {
    "token":"AryanSrivastava",
    "username": "aryan09",
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}

### Done only once
# response = requests.post(url = userAPIurl, json= user_params)
# print(response.text)

USERNAME = user_params["username"]
TOKEN = user_params["token"]

graph_params = {
    "id":"graph1",
    "name":"Reading Graph",
    "unit": "pages",
    "type":"int",
    "color":"sora",
    "timezone":"Asia/Kolkata"
}

header_graph = {
    "X-USER-TOKEN" : TOKEN
} 

graph_endpoint = f"{userAPIurl}/{USERNAME}/graphs"

### Done only once
# response = requests.post(url= graph_endpoint, json= graph_params, headers = header_graph)
# print(response.text)

## new entry

today = datetime.now()

graph_id = graph_params["id"]
newentryendpoint = graph_endpoint+f"/{graph_id}"
newentry_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"50"
}
# print(newentry_params["date"])

# response = requests.post(url= newentryendpoint, json= newentry_params, headers = header_graph)
# print(response.text)

#Update a pixel
# date = newentry_params["date"]
# or any other date
# newentry_params1 = {
#     "quantity":"100"
# }

# endpoint_update = newentryendpoint + f"/{date}"
# response = requests.put(url= endpoint_update, json= newentry_params1, headers = header_graph)
# print(response.text)

