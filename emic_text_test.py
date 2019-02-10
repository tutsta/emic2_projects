import time


def wait_for_ready():
    while True:
        in_txt = input("type : to continue ")
        if in_txt == ':':
            break
        else:
            time.sleep(0.5)
			
wait_for_ready()
input_text = input("Input text: ")
buffer = "S%s" % (input_text)
print(buffer)
print("\n")
