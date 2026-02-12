# no. 3

keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_C = keahlian_A.union(keahlian_B)
print("Keahlian yang dimiliki oleh keduanya: ",keahlian_C)

print("Keahlian yang dimiliki oleh A: ", keahlian_A)

keahlian_D = keahlian_A.intersection(keahlian_B)
print("Keahlian yang unik: ", keahlian_D)