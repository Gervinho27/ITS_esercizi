#MATCH STATEMENT


https_status = 200
match https_status:
    case 200|201: # | si riferisce ad or
        print("Success")
    case 404:
        print("Not Found")
    case 500|501:
        print("Server Error")
    # caso default
    case _:
        print("palle culo")