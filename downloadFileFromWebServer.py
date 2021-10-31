import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(type(res))
print("res.status_code " + str(res.status_code))

try:
    res.raise_for_status()

    print("res.text len " + str(len(res.text)))
    #print(res.text[:250])

    fileName = "download.txt"
    downloadFile = open(fileName, "wb")

    for chunk in res.iter_content(10000):
        downloadFile.write(chunk)

    downloadFile.close()

    print(f"\n Download to {fileName}")

except Exception as ex:
    print(f"download failure {ex}")
