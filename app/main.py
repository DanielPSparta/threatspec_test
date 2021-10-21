# @component MyApp:Web:Guest (#guest)
# @component MyApp:Web:Main (#main)
# @connects #guest to #main

def main():
    print("hello world")

# @component MyApp:Web:Login (#login)
# @connects #guest to #login with HTTP/GET-Request
# @connects #login to #guest with HTTP/GET-Response
def login():
    print("This is the login page")
