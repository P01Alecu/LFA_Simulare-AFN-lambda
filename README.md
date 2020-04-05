# LFA_Simulare-AFN-lambda
Dˆandu-se un automat finit nedeterminist - λ  ̧si m cuvinte formate din alfabetul
acestuia, testat ̧i acceptant ̧a automatului la fiecare din ele.
Input (afn.in)
• Pe prima linie a fi ̧sierului se g ̆ase ̧ste un num ̆ar n - indicele maxim al unei
st ̆ari din automat ({q0, q1, . . . , qn}, n + 1 st ̆ari)

• Pe urm ̆atoarea linie se afl ̆a un  ̧sir de caractere diferite reprezentˆand alfa-
betul automatului (de exemplu qwertyuiopasdfghjklzxcvbnm)

• Pe urm ̆atoarea linie se afl ̆a mult ̧imea de st ̆ari finale ale automatului, sep-
arate printr-un spat ̧iu

• Pe urm ̆atoarea linie se afl ̆a un num ̆ar natural k
• Pe urm ̆atoarele k linii se afl ̆a cˆate o relat ̧ie de adiacent ̧ ̆a ˆıntre st ̆arile din
automat reprezentate printr-un simbol α (simbol din alfabet sau λ)  ̧si dou ̆a
numere naturale ≤ n (de exemplu “a 1 3” reprezint ̆a o muchie q1
a−→ q3)

• Pe urm ̆atoarea linie a fi ̧sierului se afl ̆a un num ̆ar natural m
• Pe urm ̆atoarele m linii se afl ̆a cˆate un cuvˆant format din caractere ale
alfabetului
Output (afn.out)

• m linii, linia i r ̆aspunde la ˆıntrebarea: “este cuvˆantul de la pozit ̧ia i ac-
ceptat de automatul dat?” (0 - Nu, 1 - Da).
