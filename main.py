import requests

physics = 'https://docs.google.com/forms/d/e/1FAIpQLSexwRVI3f4daEVMIxYzVAG2UMXDsVAW6AbsMMekKgF7MvuWrA/formResponse'
physicsData = {
    # Last Name
    'entry.616020434': 'Siddiqui',
    # First Name
    'entry.570950898': 'Saif',
    # Color Group
    'entry.2110622356': 'Monday, Tuesday, Thursday (I have a purple box on my ID)',
    # Class Period
    'entry.816737777': '1 AP Physics C Mechanics',
}
requests.post(physics, physicsData)