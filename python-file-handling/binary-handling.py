class BinaryHandling:

    def read_write_binary_file(self):
        file = open("data/test.jpg", "rb")
        data = file.read()

        file = open("copy.jpg", "wb")
        file.write(data)
        file.close()

bh = BinaryHandling()
bh.read_write_binary_file()
