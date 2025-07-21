import statistics

def process_mountains(file_path, topN=5):
    countries = set()
    missing_altitudes = 0
    altitudes = []
    mountain_records = []

    with open(file_path, 'r', encoding='utf-8-sig') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) != 4:
                continue  # skip malformed lines

            name, altitude_str, country, iso_code = parts
            countries.add(country)

            if altitude_str == "NULL":
                missing_altitudes += 1
                altitude = None
            else:
                altitude = float(altitude_str)  # Acceptă valori cu zecimale
                altitudes.append(altitude)
            mountain_records.append({
                "name": name,
                "altitude": altitude,
                "country": country,
                "iso": iso_code
            })

    # Q1: Number of distinct countries
    print(f"1. Număr total de țări în baza de date: {len(countries)}")

    # Q2: Number of mountains without altitude
    print(f"2. Număr de munți fără informație de altitudine: {missing_altitudes}")

    # Q3: Statistics on available altitudes
    if altitudes:
        min_alt = min(altitudes)
        max_alt = max(altitudes)
        avg_alt = statistics.mean(altitudes)
        median_alt = statistics.median(altitudes)
        stddev_alt = statistics.stdev(altitudes) if len(altitudes) > 1 else 0.0

        print("3. Statistici pentru altitudinile disponibile:")
        print(f"   Min: {min_alt:.2f} m")
        print(f"   Max: {max_alt:.2f} m")
        print(f"   Medie: {avg_alt:.2f} m")
        print(f"   Mediană: {median_alt:.2f} m")
        print(f"   Deviație standard: {stddev_alt:.2f} m")
    else:
        print("3. Nu există altitudini disponibile pentru analiză.")

    # Q4: Top N highest mountains
    mountains_with_alt = [m for m in mountain_records if m["altitude"] is not None]
    top_mountains = sorted(mountains_with_alt, key=lambda m: m["altitude"], reverse=True)[:topN]

    print(f"4. Cei mai înalți {topN} munți din lume:")
    for m in top_mountains:
        print(f"   {m['name']} ({m['altitude']:.0f} m) – {m['country']} [{m['iso']}]")

# Exemplu de rulare
process_mountains("IntroToPy/mountains_db.tsv", topN=5)
