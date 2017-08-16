An extremely simple one-time-pad encryption system.

Generate one-time-pad:
otp_gen.py [chars required] > otp.txt

Encrypt:
otp_crypt.py -c otp.txt PLAINTEXT

Decrypt:
otp_crypt.py -d otp.txt CRYPTEXT
