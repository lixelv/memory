# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_text():
#     return "Hello, World!"

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0")

def sum_for_list(lst):
    a = set()
    for i in lst: 
        j = 2
        while i != 1 and i != -1:
            if i % j == 0: i //= j; a.add(j)
            else: j += 1
    return sorted([[i, sum(filter(lambda x: x % i == 0, lst))] for i in a], key = lambda x: x[0])

print(sum_for_list([123, 456, 997])) # {2, 3, 5, 7}