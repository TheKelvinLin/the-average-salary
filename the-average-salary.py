def avg(data):
    sum = 0
    result = 0
    count = data["count"]
    for item in data["employees"]:
        sum = sum + item["salary"]

    result = sum / count
    
    print(result)

avg({
    "count":3,
    "employees":[
    {
    "name":"Employee_A",
    "salary":10000
    },
    {
    "name":"Employee_B",
    "salary":20000
    },
    {
    "name":"Employee_C",
    "salary":30000
    }
    ]
})