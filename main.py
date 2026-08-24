import pandas as pd

# नया डेटा
data = {
    "Year": [2024] * 15,
    "Rank": list(range(1, 16)),
    "Rider": [
        "Remco Evenepoel (BEL)", "Filippo Ganna (ITA)", "Wout van Aert (BEL)",
        "Mathieu van der Poel (NED)", "Tadej Pogacar (SLO)", "Jonas Vingegaard (DEN)",
        "Primoz Roglic (SLO)", "Adam Yates (GBR)", "Carlos Rodriguez (ESP)",
        "Mads Pedersen (DEN)", "Jasper Philipsen (BEL)", "Ben O'Connor (AUS)",
        "Richard Carapaz (ECU)", "Joao Almeida (POR)", "Enric Mas (ESP)"
    ],
    "Time": [
        "6h 19' 37\"", "+0h 14' 22\"", "+0h 18' 45\"", "+0h 22' 10\"", "+0h 25' 33\"",
        "+0h 29' 48\"", "+0h 34' 12\"", "+0h 38' 55\"", "+0h 42' 07\"", "+0h 47' 29\"",
        "+0h 51' 14\"", "+0h 56' 38\"", "+1h 02' 11\"", "+1h 07' 45\"", "+1h 13' 22\""
    ],
    "Team": [
        "Soudal Quick-Step", "Ineos Grenadiers", "Visma-Lease a Bike",
        "Alpecin-Deceuninck", "UAE Team Emirates", "Visma-Lease a Bike",
        "Red Bull-Bora", "UAE Team Emirates", "Ineos Grenadiers",
        "Lidl-Trek", "Alpecin-Deceuninck", "Decathlon AG2R",
        "EF Education", "UAE Team Emirates", "Movistar Team"
    ]
}

df = pd.DataFrame(data)

# Cleaning
df["Rider Name"] = df["Rider"].str.replace(r"\s*\(.*\)", "", regex=True).str.strip()
df["Country"] = df["Rider"].str.extract(r"\((.*?)\)")
df["Team"] = df["Team"].str.strip()

print(df[["Rank", "Rider Name", "Country", "Time", "Team"]])

# Excel file save करना
df.to_excel("Olympics_Cycling_2024_Cleaned.xlsx", index=False)
print("\nFile successfully saved!")
