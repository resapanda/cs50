"""In a file called extensions.py,
implement a program that prompts the user
for the name of a file and then outputs that
file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:

.gif image/gif
.jpg image/jpeg
.jpeg image/jpeg
.png image/png
.pdf application/pdf
.txt text/plain
.zip application/zip

If the file’s name ends with some other suffix
or has no suffix at all, output application/octet-stream instead,
which is a common default."""

file_chunks = input("File name: ").lower().strip().split('.')
suffix = file_chunks[len(file_chunks)-1]

match suffix:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")

# if "gif" in file_name or "jpeg" in file_name or "png" in file_name:
#     file_name[0] = "image/"
#     result = ""
#     for s in file_name:
#         result += s
#     print(result)
#
# elif "jpg" in file_name:
#     file_name[0] = "image/"
#     result = ""
#     for s in file_name:
#         result += s
#     result = result.replace("jpg","jpeg")
#     print(result)
#
# elif "pdf" in file_name or "zip" in file_name:
#     file_name[0] = "application/"
#     result = ""
#     for s in file_name:
#         result += s
#     print(result)
#
# elif "txt" in file_name:
#     print("text/plain")
#
# else:
#     print("application/octet-stream")

