# -*- coding: utf-8 -*-
"""
Arbeidskrav 1: PY1010 
Frist: fredag 8.11.24
Levering: Github
Av: Marianne Riksheim Stavseth

Oppgavetekst

Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne 
de årlige kostnadene ved elbil sammenliknet med bensinbil.

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene 
for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt 
nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån 
og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, 
men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. 
Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: 
    Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 
    8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: 
    Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. 
Bensinbil: 1,0 kr/km.
Bomavgift: 
    Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
"""

# Definerer antall kjørte km/år. Setter verdien til 10 000km
Lengde = 10000

# Definerer forsikringskostnader for hhv. elbil (E) og bensinbil (B)
Forsikring_E = 5000
Forsikring_B = 7500

# Definerer trafikkforsikring (lik for E og B)
Trafikkforsikring = 8.38*365 # Antar ikke skuddår :)

# Definerer drivstoffbruk for hhv. elbil (E) og bensinbil (B)
Strompris = 2.00
Drivstoff_E = Lengde*0.2*Strompris
Drivstoff_B = Lengde*1 

# Definerer bomavgift for hhv. elbil (E) og bensinbil (B)
Bomavgift_E = 0.1*Lengde
Bomavgift_B = 0.3*Lengde

# Setter så opp årlige kostnader for hhv. elbil (E) og bensinbil (B)
Arlig_kost_E = Forsikring_E + Trafikkforsikring + Drivstoff_E + Bomavgift_E
Arlig_kost_B = Forsikring_B + Trafikkforsikring + Drivstoff_B + Bomavgift_B

# Setter så opp en print av årlige kostnader for elbil og bensinbil, samt differansen
print("Årsavgift elbil =", Arlig_kost_E)
print("Årsavgift besinbil =", Arlig_kost_B)
print("Differanse i årlig kostnad =", Arlig_kost_B-Arlig_kost_E)
