# Password Hashing Investigation

## **Aim:**
To learn about different hashing methods and what they are used for. To compare different algorithms and understand how they work/why different algorithms are created for. Also make a program for hashing & cracking the passwords that were hashed using weak algorithms.

## **Method:**
	1. Research Preparation: Find information about different hashing algorithms.
	2. Investigation: Compare different methods, Create a hashing program.
	3. Analyse: Document results & findings.

## **Research Findings:**

| Original password | Hashed Password | Algorithm Used | Time |
| ----------------- | --------------- | -------------- | ---- |
| Password123 | 42f749ade7f9e195bf475f37a44cafcb | MD5 | Fast |
| Password123 | b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb1 | SHA1 | Fast |
| Password123 | 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601 | SHA256 | Slower than MD5/SHA1, but fast |
| Password123 | $2a$12$.aEk0vYmwJHr0kAo/TS8BOc1uyi46U3wqyIF2XMvjx2OwVLu8Tvlu | Bcrypt | Slow on purpose |

## **Program results:**
	
| Input | Time used to crack MD5 (s) | Time used to crack SHA256 (s) |
| ----- | -------------------------- | ----------------------------- |
| aaaa | 0.0 | 0.0 |
| bcde | 2.158769130706787 | 0.9900956153869629 |
| abc4 | 0.025257587432861328 | 0.0255889892578125 |
| zzz0 | 29.589022874832153| 33.83320450782776 |

## **Comparison:**
All 4 hashing methods used on the same password gave out results with different length and characters used. MD5 & SHA1 are very fast hashing methods, meaning they are not going to stand against brute force attacks, when a person just uses a trial & error method to recover the password. MD5 is also known for having hash collisions, meaning different inputs produce the same output. The best option for hashing passwords is Bcrypt, because it was specifically created for password hashing. My program testing results showed that SHA256 tends to take more time to be cracked than MD5, but both can be cracked within a decent amount of time. The harder the password was, the longer was the time used to find it, even with the same length.

## **Conclusion:**
There are different ways to hash data to be stored in databases. Some old hashes are MD5 and SHA1, they are not used widely nowadays. For hashing data the choice should be SHA256, and Bcrypt for passwords as it is protected from brute force attacks. It is a good practice to make passwords longer and more complicated in order to protect yourself from brute force attacks.
