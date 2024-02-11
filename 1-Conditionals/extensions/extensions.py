def main():
    filename = input("File: ").lower().strip()
    if filename.endswith("jpg" or "jpeg"):
        print("image/jpg")
    elif filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("text/plain")
    elif filename.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
