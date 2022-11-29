import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print("Download speed: ", down)
print("Upload speed: ", upload)
