class Codec:

    def encode(self, list_of_commands):

        encoded_commands = ""
        for command in list_of_commands:
            length = len(command)
            encoded_commands += str(length)
            encoded_commands += "_"
            encoded_commands += command

        return encoded_commands
    

    def decode(self, encoded_string): 
        decoded_commands = []

        i = 0
        while i < len(encoded_string):

            length = ""
            while encoded_string[i] != "_":
                length += encoded_string[i]
                i += 1

            i += 1
            length = int(length)

            command = ""
            for j in range (length):
                command += encoded_string[i]
                j += 1
                i += 1
            
            decoded_commands.append(command)


        return decoded_commands

encoded = Codec().encode(["Hello", "World", "This is_a test"])
print(encoded)
decoded  = Codec().decode(encoded)
print(decoded)
