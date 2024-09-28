from math import lcm

def process_mpz(mpz_t: str):
    # Python debauchery to rearrange the little endian gword "limbs"
    return int("".join(mpz_t[2:].replace(" ", "").split("0x")[::-1]), 16)

mpz_t_p_bytes = "0xda5d28fa653fd41d      0xf9fdd04a062c533b"
mpz_t_q_bytes = "0x6467957633a1d6d9      0x7ee4dd28cba569f5"

# Standard RSA from here
p = process_mpz(mpz_t_p_bytes)
q = process_mpz(mpz_t_q_bytes)
n = p*q

# Check to make sure that recovered primes multiply to correct N
PCAP_N = 56048657891568470071072200352453435307145615629716429378285176310839997106837
assert n == PCAP_N
e = 65537 # No need to bother with parsing this since it's in the PCAP
d = pow(e, -1, lcm(p-1, q-1))

# Decrypt C2 command sent from server
ct = 26837762086290757052486642102560852925225702609872568979330654281329444894706
m = pow(ct, d, n)
m_pt = bytes.fromhex(hex(m)[2:]).decode() # Hacky way to convert long->str
print(m_pt)