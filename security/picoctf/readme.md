# PicoCTF from Carnegie Mellon

## PicoPrimer

![Primer link](https://primer.picoctf.com/#_introduction)

Shell commands cheatsheet -  https://www.git-tower.com/blog/command-line-cheat-sheet/

Cross site scripting clarification : when we use a pregenerated cookie to authorise ourselves on the site.

### Symmetric Crypto example using AES

The most common versions are AES 128 and AES 256, which have a key length of 128 bits and AES 256 respectively. AES algorithm is considered secure. However, the implementation can be attacked successfully if it has flaws. For example, one famous way to break AES encryption is the Padding Oracle Attack,

ECB means Electronic Code Book. In this operation mode we encrypt independently blocks of the clear text according to the key length. For example, if we are using AES 128, we break the clear text in chunks of 128 bits and use AES to encrypt them independently.

A more secure operation mode is CBC, which means Cipher Block Chaining. In this mode we include additional elements. The first one is the initialization vector, a random value with the same size as the key. In AES, the key size is the same as the block size. Remember that in AES we must separate the cleartext in blocks with the same size as the key. Before starting the encryption, we do XOR between the first block of cleartext and the Initialization Vector, then we begin to encrypt using AES with the key of our choice. The initialization vector is different for every message, so if we send the same message twice, it will be different due to the initialization vector. We must attach the initialization vector to the message. Another element we add in this operation mode, is that we do not encrypt blocks independently, but we use the encrypted text from one block and XOR it with the next block of cleartext we want to encrypt.

In AES there is a common way of padding, which is a standard called PKCS #7. In AES 128, as we said previously, the block size is 128 bits, which is equivalent to 16 bytes. PKCS contains padding.

### Asymetric crypto example : RSA

In RSA, the public key is a pair of numbers, as well as the private key. The message can be anything that we can represent as a number. In a computer, everything is a number as we know. The encrypted text, also called ciphertext, will be another number. In summary, this what we need in RSA to encrypt and decrypt:

RSA public key: Is a pair of numbers (e,n)

RSA private key: Is a pair of numbers (d,n)

Message: m

Ciphertex: c

To encrypt: me mod n = c

To decrypt: cd mod n = m

RSA is only secure when large values are used. By 2019, RSA is considered secure only if the key is a number that would take at least 2048 bits. Which is roughly 617 digits. This is how it looks as a 617 digit number:

```python
639792933441952154134189948544473456738316249934191318148092777710386387734317720754565453220777092120190516609628049092636019759882816133231666365286193266863360627356763035447762803504507772355471058595487027908143562401451718062464362679456127531813407833033625423278394497538243720583531147711992606381334677687969597030983391307710987040859133746414428227726346594704745878477872019277152807317679077071572134447306057007334924369311383504931631284042512192565179806941135280131470130478164378851852909285452011658393419656213491434159562586586557055269049652098580338507224264829397285847831630577775606888764
```


