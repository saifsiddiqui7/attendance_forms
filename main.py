import requests

r = requests.get('https://docs.google.com/forms/d/e/1FAIpQLSexwRVI3f4daEVMIxYzVAG2UMXDsVAW6AbsMMekKgF7MvuWrA/viewform')

print(r.text)