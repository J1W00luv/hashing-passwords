# Password Hashing Investigation

## **Aim:**
	To learn about different hashing methods and what they are used for. To compare different algorithms and understand how they work/why different algorithms are created for.

## **Method:**
	1. Research Preparation: Find information about different hashing algorithms.
	2. Investigation: Compare different methods.
	3. Analyse: Document results & findings.

## **Findings:**

| Original password | Hashed Password | Algorithm Used | Time |
| ----------------- | --------------- | -------------- | ---- |
| Password123 | 42f749ade7f9e195bf475f37a44cafcb | MD5 | Fast |
| Password123 | b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb1 | SHA1 | Fast |
| Password123 | 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601 | SHA256 | Slower than MD5/SHA1, but fast |
| Password123 | $2a$12$.aEk0vYmwJHr0kAo/TS8BOc1uyi46U3wqyIF2XMvjx2OwVLu8Tvlu | Bcrypt | Slow on purpose |


## **Comparison:**
	All 4 hashing methods used on the same password gave out results with different length and characters used. MD5 & SHA1 are very vulnerable hashings, and therefore not used anymore. They are the shortest and take the least time to hash the data. This means they are not going to stand against brute force attacks, when a person just uses a trial & error method to recover the password. MD5 is also known for having hash collisions, meaning different inputs produce the same output. The best option for hashing passwords is Bcrypt, because it was specifically created for password hashing. It takes the longest time to hash the password, so brute force attacks are not an efficient way to try to guess the password since unlike with MD5/SHA1, not billions of combinations can be tried every second.

## **Conclusion:**
	There are different ways to hash data to be stored in databases. Some old hashes are MD5 and SHA1, they are not used widely nowadays. For hashing data the choice should be SHA256, and Bcrypt for passwords as it is protected from brute force attacks.
