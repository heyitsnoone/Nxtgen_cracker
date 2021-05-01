# Build By Nxtgen Boy
# the_nxtgen_boy instagram
# Nxtgen_boy Snapchat

try:
    import hashlib, random, os, base64, binascii, ecdsa, base58, secrets, time
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'base58==1.0.0'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'ecdsa==0.13'])

loop = True
z = 0
x = 0
t = 0

while loop:
        while True:
            t = random.randint(0,9)
            test_list = [32, 64]
            random_num = random.choice(test_list)
            secret_exponent = os.urandom(random_num)
            pvt = hashlib.sha256(secret_exponent).hexdigest()
            privatekey = binascii.unhexlify(pvt)
            s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
            publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
            extended_key = "80"+pvt
            first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
            second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
            final_key = extended_key+second_sha256[:8]
            WIF = base58.b58encode(binascii.unhexlify(final_key))
            alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
            c = '0'; byte = '00'; zero = 0
            var = hashlib.new('ripemd160')
            var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
            a = (byte + var.hexdigest())
            doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
            address = a + doublehash[0:8]
            for char in address:
                if (char != c):
                    break
                zero += 1
            zero = zero // 2
            n = int(address, 16)
            output = []
            while (n > 0):
                n, remainder = divmod (n, 58)
                output.append(alphabet[remainder])
            count = 0
            while (count < zero):
                output.append(alphabet[0])
                count += 1
            addr = ''.join(output[::-1])
            print("Scanned: "+str(z)+"     |     Found: "+str(x)+"     |     Luck: "+ "0.00000"+str(t)+ "%" )
            print("-----------------------------------------------------------------------")
            with open("base.dat", "r") as m:
                add = m.read().split()
                for ad in add:
                    continue
                if addr in add:
                    x=x+1
                    print("Scanned: "+str(z)+" Found: "+str(x)+" Luck: "+"100"+"%")
                    data = open("F.csv","a")
                    data.write(str(addr)+","+str(WIF)+","+"\n")
                    data.close()
                elif addr not in add:
                    z=z+1