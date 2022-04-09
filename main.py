import hassapi

server = hassapi.HassRestAPIClient()

print(server.getHassStates())
print("hello")