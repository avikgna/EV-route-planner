import psycopg2

def insert_ev_data():
    connection = psycopg2.connect(
        host = "localhost",
        database = "EV_Specifications",
        user = "postgres",
        password = "Year-75763"
    )

    cursor = connection.cursor()
    #cursor handles database transactions, connection handles commits and fallbacks

    ev_trims_by_make_year_and_model = ev_trim_by_make_year_and_model = {
    ("Ford", 1999, "Ranger"): [
        "XL Electric Lead Acid 4X2 Regular CAB 5.75 FT. BOX 112 IN. WB Automatic",
        "XL Electric Nimh 4X2 Regular CAB 5.75 FT. BOX 112 IN. WB Automatic"
    ],
    ("Ford", 2000, "Ranger"): [
        "XL Electric Lead Acid 4X2 Regular CAB 5.75 FT. BOX 112 IN. WB Automatic",
        "XL Electric Nimh 4X2 Regular CAB 5.75 FT. BOX 112 IN. WB Automatic"
    ],
    ("Toyota", 2002, "Rav4 EV"): [
        "Base 4dr Front-Wheel Drive Automatic"
    ],
    ("Tesla", 2008, "Roadster"): [
        "Base 2dr Convertible Automatic"
    ],
    ("Tesla", 2009, "Roadster"): [
        "Base 2dr Convertible Automatic"
    ],
    ("Tesla", 2010, "Roadster"): [
        "Base 2dr Convertible Automatic",
        "Sport 2dr Convertible Automatic"
    ],
    ("Chevrolet", 2011, "Volt"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Nissan", 2011, "Leaf"): [
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2011, "Fortwo Electric Drive"): [
        "Base 2dr Cabriolet Automatic",
        "Base 2dr Coupe Automatic"
    ],
    ("Tesla", 2011, "Roadster"): [
        "2.5 Base 2dr Convertible Automatic",
        "2.5 Sport 2dr Convertible Automatic"
    ],
    ("Chevrolet", 2012, "Volt"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Fisker", 2012, "Karma"): [
        "Ecochic 4dr Sedan Automatic",
        "Ecosport 4dr Sedan Automatic",
        "Ecostandard 4dr Sedan Automatic"
    ],
    ("Ford", 2012, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Mitsubishi", 2012, "I Miev"): [
        "ES 4dr Hatchback Automatic",
        "SE 4dr Hatchback Automatic"
    ],
    ("Nissan", 2012, "Leaf"): [
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Tesla", 2012, "Model S"): [
        "Base 4dr Sedan Automatic",
        "Performance 4dr Sedan Automatic",
        "Signature 4dr Sedan Automatic",
        "Signature Performance 4dr Sedan Automatic"
    ],
    ("Toyota", 2012, "Rav4 EV"): [
        "Base 4dr Front-Wheel Drive Automatic"
    ],
    ("Chevrolet", 2013, "Volt"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Fiat", 2013, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2013, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Honda", 2013, "FIT EV"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Nissan", 2013, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2013, "Fortwo Electric Drive"): [
        "Passion 2dr Convertible Automatic",
        "Passion 2dr Coupe Automatic"
    ],
    ("Tesla", 2013, "Model S"): [
        "Base 4dr Sedan Automatic",
        "Performance 4dr Sedan Automatic"
    ],
    ("Toyota", 2013, "Rav4 EV"): [
        "Base 4dr Front-Wheel Drive Automatic"
    ],
    ("BMW", 2014, "I3"): [
        "Base 4dr Rear-Wheel Drive Hatchback Automatic",
        "Base W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Cadillac", 2014, "ELR"): [
        "Base 2dr Coupe Automatic"
    ],
    ("Chevrolet", 2014, "Spark EV"): [
        "1LT 4dr Hatchback Automatic",
        "2LT 4dr Hatchback Automatic"
    ],
    ("Chevrolet", 2014, "Volt"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Fiat", 2014, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2014, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Honda", 2014, "FIT EV"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Mercedes-Benz", 2014, "B-Class Electric Drive"): [
        "Base B-Class Electric Drive 4dr Hatchback Automatic"
    ],
    ("Mitsubishi", 2014, "I Miev"): [
        "ES 4dr Hatchback Automatic"
    ],
    ("Smart", 2014, "Fortwo Electric Drive"): [
        "Passion 2dr Cabriolet Automatic",
        "Passion 2dr Coupe Automatic"
    ],
    ("Tesla", 2014, "Model S"): [
        "Base 4dr Hatchback Automatic",
        "P85 4dr Hatchback Automatic",
        "P85D 4dr Hatchback Automatic"
    ],
    ("Toyota", 2014, "Rav4 EV"): [
        "Base 4dr Front-Wheel Drive Automatic"
    ],
    ("BMW", 2015, "I3"): [
        "Base 4dr Rear-Wheel Drive Hatchback Automatic",
        "Base W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Cadillac", 2015, "ELR"): [
        "Base 2dr Coupe Automatic"
    ],
    ("Chevrolet", 2015, "Spark EV"): [
        "1LT 4dr Hatchback Automatic",
        "2LT 4dr Hatchback Automatic"
    ],
    ("Chevrolet", 2015, "Volt"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Fiat", 2015, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2015, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("KIA", 2015, "Soul EV"): [
        "+ 4dr Hatchback Automatic",
        "Base 4dr Hatchback Automatic"
    ],
    ("Mercedes-Benz", 2015, "B-Class Electric Drive"): [
        "Base B-Class Electric Drive 4dr Hatchback Automatic"
    ],
    ("Nissan", 2015, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2015, "Fortwo Electric Drive"): [
        "Passion 2dr Cabriolet Automatic",
        "Passion 2dr Coupe Automatic"
    ],
    ("Tesla", 2015, "Model S"): [
        "60 4dr Rear-Wheel Drive Sedan Automatic",
        "70 4dr Rear-Wheel Drive Sedan Automatic",
        "70D 4dr All-Wheel Drive Sedan Automatic",
        "85 4dr Rear-Wheel Drive Sedan Automatic",
        "85D 4dr All-Wheel Drive Sedan Automatic",
        "P85D 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Volkswagen", 2015, "E Golf"): [
        "Limited Edition 4dr Front-Wheel Drive Hatchback Automatic",
        "SEL Premium 4dr Front-Wheel Drive Hatchback Automatic"
    ],
    ("BMW", 2016, "I3"): [
        "Base 4dr Rear-Wheel Drive Hatchback Automatic",
        "Base W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Cadillac", 2016, "ELR"): [
        "Base 2dr Coupe Automatic"
    ],
    ("Chevrolet", 2016, "Spark EV"): [
        "1LT 4dr Hatchback Automatic",
        "2LT 4dr Hatchback Automatic"
    ],
    ("Fiat", 2016, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2016, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("KIA", 2016, "Soul EV"): [
        "+ 4dr Hatchback Automatic",
        "Base 4dr Hatchback Automatic",
        "EVE 4dr Hatchback Automatic"
    ],
    ("Mercedes-Benz", 2016, "B-Class"): [
        "Base B 250E 4dr Hatchback Automatic"
    ],
    ("Mitsubishi", 2016, "I Miev"): [
        "ES 4dr Hatchback Automatic"
    ],
    ("Nissan", 2016, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2016, "Fortwo Electric Drive"): [
        "Passion 2dr Coupe Automatic"
    ],
    ("Tesla", 2016, "Model S"): [
        "60 4dr Rear-Wheel Drive Sedan 2016.5 Automatic",
        "60D 4dr All-Wheel Drive Sedan 2016.5 Automatic",
        "70 4dr Rear-Wheel Drive Sedan 2016.5 Automatic",
        "70 4dr Rear-Wheel Drive Sedan Automatic",
        "70D 4dr All-Wheel Drive Hatchback Automatic",
        "70D 4dr All-Wheel Drive Sedan 2016.5 Automatic",
        "75 4dr Rear-Wheel Drive Sedan 2016.5 Automatic",
        "75D 4dr All-Wheel Drive Sedan 2016.5 Automatic",
        "85D 4dr All-Wheel Drive Hatchback Automatic",
        "90D 4dr All-Wheel Drive Hatchback Automatic",
        "90D 4dr All-Wheel Drive Sedan 2016.5 Automatic",
        "P100D 4dr All-Wheel Drive Sedan 2016.5 Automatic",
        "P85D 4dr All-Wheel Drive Hatchback Automatic",
        "P90D 4dr All-Wheel Drive Hatchback Automatic",
        "P90D 4dr All-Wheel Drive Sedan 2016.5 Automatic"
    ],
    ("Tesla", 2016, "Model X"): [
        "60D 4dr Sport Utility Automatic",
        "70D 4dr Sport Utility Automatic",
        "75D 4dr Sport Utility Automatic",
        "90D 4dr Sport Utility Automatic",
        "P100D 4dr Sport Utility Automatic",
        "P90D 4dr Sport Utility Automatic"
    ],
    ("Toyota", 2016, "Mirai"): [
        "Base 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2016, "E Golf"): [
        "SE 4dr Front-Wheel Drive Hatchback Automatic"
    ],
    ("BMW", 2017, "I3"): [
        "60 AH 4dr Rear-Wheel Drive Hatchback Automatic",
        "94 AH 4dr Rear-Wheel Drive Hatchback Automatic",
        "94 AH W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Chevrolet", 2017, "Bolt EV"): [
        "LT 4dr Wagon Automatic",
        "LT Front-Wheel Drive Automatic",
        "Premier 4dr Wagon Automatic",
        "Premier Front-Wheel Drive Automatic"
    ],
    ("Fiat", 2017, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2017, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Hyundai", 2017, "Ioniq EV"): [
        "Electric 4dr Hatchback Automatic",
        "Limited 4dr Hatchback Automatic"
    ],
    ("KIA", 2017, "Soul EV"): [
        "+ 4dr Hatchback Automatic",
        "Base 4dr Hatchback Automatic",
        "EVE 4dr Hatchback Automatic"
    ],
    ("Mercedes-Benz", 2017, "B-Class"): [
        "Base B 250E Hatchback Automatic"
    ],
    ("Mitsubishi", 2017, "I Miev"): [
        "ES 4dr Hatchback Automatic"
    ],
    ("Nissan", 2017, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2017, "Fortwo Electric Drive"): [
        "Passion 2dr Cabriolet Automatic",
        "Passion 2dr Coupe Automatic",
        "Prime 2dr Cabriolet Automatic",
        "Prime 2dr Coupe Automatic",
        "Pure 2dr Coupe Automatic"
    ],
    ("Tesla", 2017, "Model 3"): [
        "Long Range 4dr Rear-Wheel Drive Sedan Automatic",
        "Standard 4dr Rear-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2017, "Model S"): [
        "100D 4dr All-Wheel Drive Sedan Automatic",
        "60 4dr Rear-Wheel Drive Sedan Automatic",
        "60D 4dr All-Wheel Drive Sedan Automatic",
        "75 4dr Rear-Wheel Drive Sedan Automatic",
        "75D 4dr All-Wheel Drive Sedan Automatic",
        "90D 4dr All-Wheel Drive Sedan Automatic",
        "P100D 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2017, "Model X"): [
        "100D 4dr Sport Utility Automatic",
        "75D 4dr Sport Utility Automatic",
        "90D 4dr Sport Utility Automatic",
        "P100D 4dr Sport Utility Automatic"
    ],
    ("Toyota", 2017, "Mirai"): [
        "Base 4dr Sedan Automatic"
    ],

    ("Volkswagen", 2017, "E Golf") : ['Limited Edition 4dr Front-Wheel Drive Hatchback Automatic', 
                                    'SE 4dr Front-Wheel Drive Hatchback Automatic', 
                                    'SEL Premium 4dr Front-Wheel Drive Hatchback Automatic'],
    ("BMW", 2018, "I3"): [
        "94Ah 4dr Rear-Wheel Drive Hatchback Automatic",
        "94Ah S 4dr Rear-Wheel Drive Hatchback Automatic",
        "94Ah S W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic",
        "94Ah W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Chevrolet", 2018, "Bolt EV"): [
        "LT 4dr Wagon Automatic",
        "Premier 4dr Wagon Automatic"
    ],
    ("Fiat", 2018, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Ford", 2018, "Focus Electric"): [
        "Base 4dr Hatchback Automatic"
    ],
    ("Hyundai", 2018, "Ioniq EV"): [
        "Electric 4dr Hatchback Automatic",
        "Limited 4dr Hatchback Automatic"
    ],
    ("Karma", 2018, "Revero"): [
        "Base Rear-Wheel Drive Sedan Automatic"
    ],
    ("KIA", 2018, "Soul EV"): [
        "+ 4dr Hatchback Automatic",
        "Base 4dr Hatchback Automatic",
        "EVE 4dr Hatchback Automatic"
    ],
    ("Nissan", 2018, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SL 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic"
    ],
    ("Smart", 2018, "Fortwo Electric Drive"): [
        "Passion 2dr Cabriolet Automatic",
        "Passion 2dr Coupe Automatic",
        "Prime 2dr Cabriolet Automatic",
        "Prime 2dr Coupe Automatic",
        "Pure 2dr Coupe Automatic"
    ],
    ("Tesla", 2018, "Model 3"): [
        "Long Range 4dr All-Wheel Drive Sedan Automatic",
        "Long Range 4dr Rear-Wheel Drive Sedan Automatic",
        "MID Range 4dr Rear-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2018, "Model S"): [
        "100D 4dr All-Wheel Drive Hatchback Automatic",
        "75D 4dr All-Wheel Drive Hatchback Automatic",
        "P100D 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2018, "Model X"): [
        "100D 4dr Sport Utility Automatic",
        "75D 4dr Sport Utility Automatic",
        "P100D 4dr Sport Utility Automatic"
    ],
    ("Toyota", 2018, "Mirai"): [
        "Base 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2018, "E Golf"): [
        "SE 4dr Front-Wheel Drive Hatchback Automatic",
        "SEL 4dr Front-Wheel Drive Hatchback Automatic",
        "SEL Premium 4dr Front-Wheel Drive Hatchback Automatic"
    ],
    ("Audi", 2019, "E Tron"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sport Utility Automatic"
    ],
    ("BMW", 2019, "I3"): [
        "120Ah 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Chevrolet", 2019, "Bolt EV"): [
        "LT 4dr Wagon Automatic",
        "Premier 4dr Wagon Automatic"
    ],
    ("Fiat", 2019, "500E"): [
        "Battery Electric 2dr Hatchback Automatic"
    ],
    ("Honda", 2019, "Clarity Electric"): [
        "Base 4dr Sedan Automatic"
    ],
    ("Honda", 2019, "Clarity Fuel Cell"): [
        "Clarity 4dr Sedan Automatic"
    ],
    ("Hyundai", 2019, "Ioniq EV"): [
        "Electric 4dr Hatchback Automatic",
        "Limited 4dr Hatchback Automatic"
    ],
    ("Hyundai", 2019, "Kona Electric"): [
        "Limited 4dr Front-Wheel Drive Automatic",
        "SEL 4dr Front-Wheel Drive Automatic",
        "Ultimate 4dr Front-Wheel Drive Automatic"
    ],
    ("Hyundai", 2019, "Nexo"): [
        "Blue 4dr Front-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic"
    ],
    ("Jaguar", 2019, "I Pace"): [
        "First Edition 4dr All-Wheel Drive Sport Utility Automatic",
        "HSE 4dr All-Wheel Drive Sport Utility Automatic",
        "S 4dr All-Wheel Drive Sport Utility Automatic",
        "SE 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Karma", 2019, "Revero"): [
        "Base Rear-Wheel Drive Sedan Automatic"
    ],
    ("KIA", 2019, "Niro EV"): [
        "EX 4dr Front-Wheel Drive Sport Utility Automatic",
        "EX Premium 4dr Front-Wheel Drive Sport Utility Automatic"
    ],
    ("KIA", 2019, "Soul EV"): [
        "+ 4dr Hatchback Automatic",
        "Base 4dr Hatchback Automatic"
    ],
    ("Nissan", 2019, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "S Plus 4dr Hatchback Automatic",
        "SL Plus 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic",
        "SV Plus 4dr Hatchback Automatic"
    ],
    ("Smart", 2019, "EQ Fortwo"): [
        "Passion 2dr Cabriolet Automatic",
        "Passion 2dr Coupe Automatic",
        "Prime 2dr Cabriolet Automatic",
        "Prime 2dr Coupe Automatic",
        "Pure 2dr Coupe Automatic"
    ],
    ("Tesla", 2019, "Model 3"): [
        "Long Range 4dr All-Wheel Drive Sedan Automatic",
        "Long Range 4dr Rear-Wheel Drive Sedan Automatic",
        "MID Range 4dr Rear-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic",
        "Standard Range 4dr Rear-Wheel Drive Sedan Automatic",
        "Standard Range Plus 4dr Rear-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2019, "Model S"): [
        "100D 4dr All-Wheel Drive Hatchback Automatic",
        "75D 4dr All-Wheel Drive Hatchback Automatic",
        "Base 4dr All-Wheel Drive Hatchback Automatic",
        "Long Range 4dr All-Wheel Drive Hatchback Automatic",
        "P100D 4dr All-Wheel Drive Hatchback Automatic",
        "Performance 4dr All-Wheel Drive Hatchback Automatic",
        "Standard Range 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2019, "Model X"): [
        "100D 4dr Sport Utility Automatic",
        "75D 4dr Sport Utility Automatic",
        "Base 4dr Sport Utility Automatic",
        "Long Range 4dr Sport Utility Automatic",
        "P100D 4dr Sport Utility Automatic",
        "Performance 4dr Sport Utility Automatic",
        "Standard Range 4dr Sport Utility Automatic"
    ],
    ("Toyota", 2019, "Mirai"): [
        "Base 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2019, "E Golf"): [
        "SE 4dr Front-Wheel Drive Hatchback Automatic",
        "SEL Premium 4dr Front-Wheel Drive Hatchback Automatic"
    ],
    ("Audi", 2020, "E Tron"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("BMW", 2020, "I3"): [
        "120Ah 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Chevrolet", 2020, "Bolt EV"): [
        "LT 4dr Wagon Automatic",
        "Premier 4dr Wagon Automatic"
    ],
    ("Honda", 2020, "Clarity Fuel Cell"): [
        "Clarity 4dr Sedan Automatic"
    ],
    ("Hyundai", 2020, "Ioniq EV"): [
        "Limited 4dr Hatchback Automatic",
        "SE 4dr Hatchback Automatic"
    ],
    ("Hyundai", 2020, "Kona Electric"): [
        "Limited 4dr Front-Wheel Drive Automatic",
        "SEL 4dr Front-Wheel Drive Automatic",
        "Ultimate 4dr Front-Wheel Drive Automatic"
    ],
    ("Hyundai", 2020, "Nexo"): [
        "Blue 4dr Front-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic"
    ],
    ("Jaguar", 2020, "I Pace"): [
        "HSE 4dr All-Wheel Drive Sport Utility Automatic",
        "S 4dr All-Wheel Drive Sport Utility Automatic",
        "SE 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Karma", 2020, "Revero GT"): [
        "Base Rear-Wheel Drive Sedan Automatic",
        "Sports Rear-Wheel Drive Sedan Automatic"
    ],
    ("KIA", 2020, "Niro EV"): [
        "EX 4dr Front-Wheel Drive Sport Utility Automatic",
        "EX Premium 4dr Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Mini", 2020, "SE Hardtop"): [
        "Cooper 2dr Automatic"
    ],
    ("Nissan", 2020, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "S Plus 4dr Hatchback Automatic",
        "SL Plus 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic",
        "SV Plus 4dr Hatchback Automatic"
    ],
    ("Porsche", 2020, "Taycan"): [
        "4S 4dr All-Wheel Drive Sedan Automatic",
        "Turbo 4dr All-Wheel Drive Sedan Automatic",
        "Turbo S 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2020, "Model 3"): [
        "Long Range 4dr All-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic",
        "Standard Range 4dr Rear-Wheel Drive Sedan Automatic",
        "Standard Range Plus 4dr Rear-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2020, "Model S"): [
        "Long Range 4dr All-Wheel Drive Hatchback Automatic",
        "Long Range Plus 4dr All-Wheel Drive Hatchback Automatic",
        "Performance 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2020, "Model X"): [
        "Long Range 4dr Sport Utility Automatic",
        "Long Range Plus 4dr Sport Utility Automatic",
        "Performance 4dr Sport Utility Automatic"
    ],
    ("Tesla", 2020, "Model Y"): [
        "Long Range 4dr Sport Utility Automatic",
        "Performance 4dr Sport Utility Automatic"
    ],
    ("Toyota", 2020, "Mirai"): [
        "Base 4dr Sedan Automatic"
    ],
    ("Audi", 2021, "E Tron"): [
        "Premium 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "Premium 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("BMW", 2021, "I3"): [
        "120Ah 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah S W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic",
        "120Ah W/Range Extender 4dr Rear-Wheel Drive Hatchback Automatic"
    ],
    ("Chevrolet", 2021, "Bolt EV"): [
        "LT 4dr Wagon Automatic",
        "Premier 4dr Wagon Automatic"
    ],
    ("Ford", 2021, "Mustang Mach E"): [
        "California Route 1 4dr 4X2 Automatic",
        "GT 4dr All-Wheel Drive Automatic",
        "Premium 4dr 4X2 Automatic",
        "Premium 4dr All-Wheel Drive Automatic",
        "Select 4dr 4X2 Automatic",
        "Select 4dr All-Wheel Drive Automatic"
    ],
    ("Honda", 2021, "Clarity Fuel Cell"): [
        "Clarity 4dr Sedan Automatic"
    ],
    ("Hyundai", 2021, "Ioniq EV"): [
        "Limited 4dr Hatchback Automatic",
        "SE 4dr Hatchback Automatic"
    ],
    ("Hyundai", 2021, "Kona Electric"): [
        "Limited 4dr Front-Wheel Drive Automatic",
        "SEL 4dr Front-Wheel Drive Automatic",
        "Ultimate 4dr Front-Wheel Drive Automatic"
    ],
    ("Hyundai", 2021, "Nexo"): [
        "Blue 4dr Front-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic"
    ],
    ("Karma", 2021, "GS 6"): [
        "Base Rear-Wheel Drive Sedan Automatic",
        "Luxury Rear-Wheel Drive Sedan Automatic",
        "Sport Rear-Wheel Drive Sedan Automatic"
    ],
    ("KIA", 2021, "Niro EV"): [
        "EX 4dr Front-Wheel Drive Sport Utility Automatic",
        "EX Premium 4dr Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Mini", 2021, "SE Hardtop"): [
        "Cooper 2dr Automatic"
    ],
    ("Nissan", 2021, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "S Plus 4dr Hatchback Automatic",
        "SL Plus 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic",
        "SV Plus 4dr Hatchback Automatic"
    ],
    ("Polestar", 2021, "2"): [
        "Launch Edition 4dr Fastback Automatic"
    ],
    ("Porsche", 2021, "Taycan"): [
        "4S 4dr All-Wheel Drive Sedan Automatic",
        "Base 4dr Rear-Wheel Drive Sedan Automatic",
        "Turbo 4dr All-Wheel Drive Sedan Automatic",
        "Turbo S 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Porsche", 2021, "Taycan Cross Turismo"): [
        "4 4dr All-Wheel Drive Wagon Automatic",
        "4S 4dr All-Wheel Drive Wagon Automatic",
        "Turbo 4dr All-Wheel Drive Wagon Automatic",
        "Turbo S 4dr All-Wheel Drive Wagon Automatic"
    ],
    ("Tesla", 2021, "Model 3"): [
        "Long Range 4dr All-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic",
        "Standard Range Plus 4dr Rear-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2021, "Model S"): [
        "Long Range 4dr All-Wheel Drive Hatchback Automatic",
        "Long Range Plus 4dr All-Wheel Drive Hatchback Automatic",
        "Performance 4dr All-Wheel Drive Hatchback Automatic",
        "Plaid 4dr All-Wheel Drive Hatchback Automatic",
        "Plaid+ 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2021, "Model X"): [
        "Long Range 4dr Sport Utility Automatic",
        "Long Range Plus 4dr Sport Utility Automatic",
        "Performance 4dr Sport Utility Automatic",
        "Plaid 4dr Sport Utility Automatic"
    ],
    ("Tesla", 2021, "Model Y"): [
        "Long Range 4dr All-Wheel Drive Sport Utility Automatic",
        "Performance 4dr All-Wheel Drive Sport Utility Automatic",
        "Standard Range 4dr Rear-Wheel Drive Sport Utility Automatic"
    ],
    ("Toyota", 2021, "Mirai"): [
        "Limited 4dr Sedan Automatic",
        "XLE 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2021, "Id.4"): [
        "1ST Edition 4dr 4X2 Automatic",
        "PRO 4dr 4X2 Automatic",
        "PRO 4dr All-Wheel Drive Automatic",
        "PRO S 4dr 4X2 Automatic",
        "PRO S 4dr All-Wheel Drive Automatic"
    ],
    ("Volvo", 2021, "Xc40 Recharge Pure Electric"): [
        "P8 4dr All-Wheel Drive Automatic"
    ],
    ("Audi", 2022, "E Tron"): [
        "Premium 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "S Line Premium 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("Audi", 2022, "E Tron GT"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sedan Automatic"
    ],
    ("Audi", 2022, "E Tron S"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "Premium Plus 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("Audi", 2022, "Q4 E Tron"): [
        "40 Premium 4dr 4X2 Sport Utility Automatic",
        "50 Premium 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "50 Premium 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("Audi", 2022, "RS E Tron GT"): [
        "Base 4dr All-Wheel Drive Quattro Sedan Automatic"
    ],
    ("BMW", 2022, "I4"): [
        "M50 4dr All-Wheel Drive Gran Coupe Automatic",
        "Edrive40 4dr Rear-Wheel Drive Gran Coupe Automatic"
    ],
    ("BMW", 2022, "IX"): [
        "Xdrive50 4dr All-Wheel Drive Sports Activity Vehicle Automatic"
    ],
    ("Chevrolet", 2022, "Bolt EUV"): [
        "LT Front-Wheel Drive Automatic",
        "Premier Front-Wheel Drive Automatic"
    ],
    ("Chevrolet", 2022, "Bolt EV"): [
        "1LT 4dr Wagon Automatic",
        "2LT 4dr Wagon Automatic"
    ],
    ("Ford", 2022, "F 150 Lightning"): [
        "Lariat All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "Platinum All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "PRO All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "XLT All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic"
    ],
    ("Ford", 2022, "Mustang Mach E"): [
        "California Route 1 4dr 4X2 Automatic",
        "California Route 1 4dr All-Wheel Drive Automatic",
        "GT 4dr All-Wheel Drive Automatic",
        "Premium 4dr 4X2 Automatic",
        "Premium 4dr All-Wheel Drive Automatic",
        "Select 4dr 4X2 Automatic",
        "Select 4dr All-Wheel Drive Automatic"
    ],
    ("GMC", 2022, "Hummer EV"): [
        "Edition 1 4X4 Automatic"
    ],
    ("Hyundai", 2022, "Ioniq 5"): [
        "Limited 4X2 Automatic",
        "Limited All-Wheel Drive Automatic",
        "SE 4X2 Automatic",
        "SE All-Wheel Drive Automatic",
        "SE Standard Range 4X2 Automatic",
        "SEL 4X2 Automatic",
        "SEL All-Wheel Drive Automatic"
    ],
    ("Hyundai", 2022, "Kona Electric"): [
        "Limited 4dr Front-Wheel Drive Automatic",
        "SEL 4dr Front-Wheel Drive Automatic"
    ],
    ("Hyundai", 2022, "Nexo"): [
        "Blue 4dr Front-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic"
    ],
    ("Jaguar", 2022, "I Pace"): [
        "HSE 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("KIA", 2022, "EV6"): [
        "Gt-Line 4dr 4X2 Automatic",
        "Gt-Line 4dr All-Wheel Drive Automatic",
        "Light 4dr 4X2 Automatic",
        "Wind 4dr 4X2 Automatic",
        "Wind 4dr All-Wheel Drive Automatic"
    ],
    ("KIA", 2022, "Niro EV"): [
        "EX 4dr Front-Wheel Drive Sport Utility Automatic",
        "EX Premium 4dr Front-Wheel Drive Sport Utility Automatic",
        "S 4dr Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Lucid", 2022, "AIR"): [
        "Dream Edition 4dr All-Wheel Drive Sedan Automatic",
        "Grand Touring 4dr All-Wheel Drive Sedan Automatic",
        "Pure 4dr All-Wheel Drive Sedan Automatic",
        "Pure 4dr Rear-Wheel Drive Sedan Automatic",
        "Touring 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Mazda", 2022, "MX 30 EV"): [
        "Base Front-Wheel Drive Sport Utility Automatic",
        "Premium Plus Package Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Mercedes-Benz", 2022, "AMG EQS"): [
        "Base AMG EQS 4dr All-Wheel Drive 4Matic+ Sedan Automatic"
    ],
    ("Mercedes-Benz", 2022, "EQB 300"): [
        "Base EQB 300 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2022, "EQB 350"): [
        "Base EQB 350 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2022, "EQS 450+"): [
        "Base EQS 450+ Sedan 4dr Rear-Wheel Drive Automatic"
    ],
    ("Mercedes-Benz", 2022, "EQS 580"): [
        "Base EQS 580 Sedan 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mini", 2022, "SE Hardtop"): [
        "Cooper 2dr Automatic"
    ],
    ("Nissan", 2022, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "S Plus 4dr Hatchback Automatic",
        "SL Plus 4dr Hatchback Automatic",
        "SV 4dr Hatchback Automatic",
        "SV Plus 4dr Hatchback Automatic"
    ],
    ("Polestar", 2022, "2"): [
        "Long Range Dual Motor 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Single Motor 4dr Front-Wheel Drive Fastback Automatic"
    ],
    ("Porsche", 2022, "Taycan"): [
        "4S 4dr All-Wheel Drive Sedan Automatic",
        "Base 4dr Rear-Wheel Drive Sedan Automatic",
        "GTS 4dr All-Wheel Drive Sedan Automatic",
        "Turbo 4dr All-Wheel Drive Sedan Automatic",
        "Turbo S 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Porsche", 2022, "Taycan Cross Turismo"): [
        "4 4dr All-Wheel Drive Wagon Automatic",
        "4S 4dr All-Wheel Drive Wagon Automatic",
        "Turbo 4dr All-Wheel Drive Wagon Automatic",
        "Turbo S 4dr All-Wheel Drive Wagon Automatic"
    ],
    ("Porsche", 2022, "Taycan Sport Turismo"): [
        "GTS 4dr All-Wheel Drive Wagon Automatic"
    ],
    ("Rivian", 2022, "R1S"): [
        "Adventure All-Wheel Drive Sport Utility Automatic",
        "Explore All-Wheel Drive Sport Utility Automatic",
        "Launch Edition All-Wheel Drive Sport Utility Automatic"
    ],
    ("Rivian", 2022, "R1T"): [
        "Adventure All-Wheel Drive Crew CAB Automatic",
        "Explore All-Wheel Drive Crew CAB Automatic",
        "Launch Edition All-Wheel Drive Crew CAB Automatic"
    ],
    ("Tesla", 2022, "Model 3"): [
        "Base 4dr Rear-Wheel Drive Sedan Automatic",
        "Long Range 4dr All-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2022, "Model S"): [
        "Base 4dr All-Wheel Drive Hatchback Automatic",
        "Plaid 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2022, "Model X"): [
        "Base 4dr Sport Utility Automatic",
        "Plaid 4dr Sport Utility Automatic"
    ],
    ("Tesla", 2022, "Model Y"): [
        "Long Range 4dr All-Wheel Drive Sport Utility Automatic",
        "Performance 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Toyota", 2022, "Mirai"): [
        "Limited 4dr Sedan Automatic",
        "XLE 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2022, "Id.4"): [
        "PRO 4dr 4X2 Automatic",
        "PRO 4dr All-Wheel Drive Automatic",
        "PRO S 4dr 4X2 Automatic",
        "PRO S 4dr All-Wheel Drive Automatic"
    ],
    ("Volvo", 2022, "C40 Recharge Pure Electric"): [
        "P8 Ultimate 4dr All-Wheel Drive Automatic"
    ],
    ("Volvo", 2022, "Xc40 Recharge Pure Electric"): [
        "P8 Twin 4dr All-Wheel Drive Automatic",
        "P8 Twin Plus 4dr All-Wheel Drive Automatic",
        "P8 Twin Ultimate 4dr All-Wheel Drive Automatic"
    ],

    ("Audi", 2023, "E Tron"): [
        "Premium 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "S Line Premium 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("Audi", 2023, "E Tron GT"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sedan Automatic"
    ],
    ("Audi", 2023, "E Tron S"): [
        "Premium Plus 4dr All-Wheel Drive Quattro Sport Utility Automatic",
        "Premium Plus 4dr All-Wheel Drive Quattro Sportback Automatic"
    ],
    ("Audi", 2023, "Q4 E Tron"): [
        "40 Premium 4dr 4X2 Sport Utility Automatic",
        "50 Premium 4dr All-Wheel Drive Quattro Sport Utility Automatic"
    ],
    ("Audi", 2023, "RS E Tron GT"): [
        "Base 4dr All-Wheel Drive Quattro Sedan Automatic"
    ],
    ("BMW", 2023, "I4"): [
        "M50 4dr All-Wheel Drive Gran Coupe Automatic",
        "Edrive35 4dr Rear-Wheel Drive Gran Coupe Automatic",
        "Edrive40 4dr Rear-Wheel Drive Gran Coupe Automatic"
    ],
    ("BMW", 2023, "I7"): [
        "Xdrive60 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("BMW", 2023, "IX"): [
        "M60 4dr All-Wheel Drive Sports Activity Vehicle Automatic",
        "Xdrive50 4dr All-Wheel Drive Sports Activity Vehicle Automatic"
    ],
    ("Cadillac", 2023, "Lyriq"): [
        "Luxury 4X2 Automatic",
        "Luxury All-Wheel Drive Automatic"
    ],
    ("Chevrolet", 2023, "Bolt EUV"): [
        "LT Front-Wheel Drive Automatic",
        "Premier Front-Wheel Drive Automatic"
    ],
    ("Chevrolet", 2023, "Bolt EV"): [
        "1LT 4dr Wagon Automatic",
        "2LT 4dr Wagon Automatic"
    ],
    ("Ford", 2023, "F 150 Lightning"): [
        "Lariat All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "Platinum All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "PRO All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "XLT All-Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic"
    ],
    ("Ford", 2023, "Mustang Mach E"): [
        "California Route 1 4dr All-Wheel Drive Automatic",
        "GT 4dr All-Wheel Drive Automatic",
        "Premium 4dr 4X2 Automatic",
        "Premium 4dr All-Wheel Drive Automatic",
        "Select 4dr 4X2 Automatic",
        "Select 4dr All-Wheel Drive Automatic"
    ],
    ("Genesis", 2023, "Electrified G80"): [
        "Electric 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Genesis", 2023, "Electrified Gv70"): [
        "Advanced 4dr All-Wheel Drive Automatic"
    ],
    ("Genesis", 2023, "Gv60"): [
        "Advanced 4dr All-Wheel Drive Automatic",
        "Performance 4dr All-Wheel Drive Automatic"
    ],
    ("GMC", 2023, "Hummer EV Pickup"): [
        "3X 4X4 Automatic"
    ],
    ("Hyundai", 2023, "Ioniq 5"): [
        "Limited 4X2 Automatic",
        "Limited All-Wheel Drive Automatic",
        "SE 4X2 Automatic",
        "SE All-Wheel Drive Automatic",
        "SE Standard Range 4X2 Automatic",
        "SEL 4X2 Automatic",
        "SEL All-Wheel Drive Automatic"
    ],
    ("Hyundai", 2023, "Kona Electric"): [
        "Limited 4dr Front-Wheel Drive Automatic",
        "SE 4dr Front-Wheel Drive Automatic",
        "SEL 4dr Front-Wheel Drive Automatic"
    ],
    ("Hyundai", 2023, "Nexo"): [
        "Blue 4dr Front-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic"
    ],
    ("Jaguar", 2023, "I Pace"): [
        "HSE 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("KIA", 2023, "EV6"): [
        "GT 4dr All-Wheel Drive Automatic",
        "Gt-Line 4dr 4X2 Automatic",
        "Gt-Line 4dr All-Wheel Drive Automatic",
        "Wind 4dr 4X2 Automatic",
        "Wind 4dr All-Wheel Drive Automatic"
    ],
    ("KIA", 2023, "Niro EV"): [
        "Wave 4dr Front-Wheel Drive Sport Utility Automatic",
        "Wind 4dr Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Lexus", 2023, "RZ 450E"): [
        "Luxury 4dr All-Wheel Drive Automatic",
        "Premium 4dr All-Wheel Drive Automatic"
    ],
    ("Lordstown", 2023, "Endurance"): [
        "Work 4X4 Crew CAB Automatic"
    ],
    ("Lucid", 2023, "AIR"): [
        "Grand Touring 4dr All-Wheel Drive Sedan Automatic",
        "Grand Touring Performance 4dr All-Wheel Drive Sedan Automatic",
        "Pure 4dr All-Wheel Drive Sedan Automatic",
        "Pure 4dr Rear-Wheel Drive Sedan Automatic",
        "Touring 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Mazda", 2023, "MX 30 EV"): [
        "Base Front-Wheel Drive Sport Utility Automatic",
        "Premium Plus Package Front-Wheel Drive Sport Utility Automatic"
    ],
    ("Mercedes-Benz", 2023, "AMG EQE"): [
        "Base AMG EQE 4dr All-Wheel Drive 4Matic+ Sedan Automatic"
    ],
    ("Mercedes-Benz", 2023, "AMG EQS"): [
        "Base AMG EQS 4dr All-Wheel Drive 4Matic+ Sedan Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQB 250"): [
        "Base EQB 250 4dr Front-Wheel Drive Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQB 300"): [
        "Base EQB 300 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQB 350"): [
        "Base EQB 350 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQE 350"): [
        "Base EQE 350 Sedan 4dr All-Wheel Drive 4Matic+ Automatic",
        "Base EQE 350 Sedan 4dr Rear-Wheel Drive Automatic",
        "Base EQE 350+ Sedan 4dr Rear-Wheel Drive Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQE 500"): [
        "Base EQE 500 Sedan 4dr All-Wheel Drive 4Matic+ Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQS 450"): [
        "Base EQS 450 SUV 4dr All-Wheel Drive 4Matic Automatic",
        "Base EQS 450 Sedan 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQS 450+"): [
        "Base EQS 450 SUV 4dr All-Wheel Drive 4Matic Automatic",
        "Base EQS 450 Sedan 4dr All-Wheel Drive 4Matic Automatic",
        "Base EQS 450+ 4dr All-Wheel Drive 4Matic Sedan Automatic",
        "Base EQS 450+ 4dr All-Wheel Drive 4Matic Sport Utility Automatic",
        "Base EQS 450+ SUV 4dr 4X2 Automatic",
        "Base EQS 450+ Sedan 4dr Rear-Wheel Drive Automatic"
    ],
    ("Mercedes-Benz", 2023, "EQS 580"): [
        "Base EQS 580 SUV 4dr All-Wheel Drive 4Matic Automatic",
        "Base EQS 580 Sedan 4dr All-Wheel Drive 4Matic Automatic"
    ],
    ("Mini", 2023, "SE Hardtop"): [
        "Cooper 2dr Automatic",
        "Cooper Signature 2dr Automatic"
    ],
    ("Nissan", 2023, "Ariya"): [
        "Empower+ 4dr Front-Wheel Drive Automatic",
        "Engage 4dr Front-Wheel Drive Automatic",
        "Evolve+ 4dr Front-Wheel Drive Automatic",
        "Premiere 4dr Front-Wheel Drive Automatic",
        "Venture+ 4dr Front-Wheel Drive Automatic"
    ],
    ("Nissan", 2023, "Leaf"): [
        "S 4dr Hatchback Automatic",
        "SV Plus 4dr Hatchback Automatic"
    ],
    ("Polestar", 2023, "2"): [
        "Long Range Dual Motor 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Dual Motor BST Edition 270 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Dual Motor Performance 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Dual Motor Performance Plus 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Dual Motor Plus 4dr All-Wheel Drive Fastback Automatic",
        "Long Range Single Motor 4dr Front-Wheel Drive Fastback Automatic",
        "Long Range Single Motor Plus 4dr Front-Wheel Drive Fastback Automatic"
    ],
    ("Porsche", 2023, "Taycan"): [
        "4S 4dr All-Wheel Drive Sedan Automatic",
        "Base 4dr Rear-Wheel Drive Sedan Automatic",
        "GTS 4dr All-Wheel Drive Sedan Automatic",
        "Turbo 4dr All-Wheel Drive Sedan Automatic",
        "Turbo S 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Porsche", 2023, "Taycan Cross Turismo"): [
        "4 4dr All-Wheel Drive Wagon Automatic",
        "4S 4dr All-Wheel Drive Wagon Automatic",
        "Turbo 4dr All-Wheel Drive Wagon Automatic",
        "Turbo S 4dr All-Wheel Drive Wagon Automatic"
    ],
    ("Porsche", 2023, "Taycan Sport Turismo"): [
        "GTS 4dr All-Wheel Drive Wagon Automatic"
    ],
    ("Rivian", 2023, "R1S"): [
        "Adventure All-Wheel Drive Sport Utility Automatic"
    ],
    ("Rivian", 2023, "R1T"): [
        "Adventure All-Wheel Drive Crew CAB Automatic"
    ],
    ("Subaru", 2023, "Solterra"): [
        "Limited 4dr All-Wheel Drive Automatic",
        "Premium 4dr All-Wheel Drive Automatic",
        "Touring 4dr All-Wheel Drive Automatic"
    ],
    ("Tesla", 2023, "Model 3"): [
        "Base 4dr Rear-Wheel Drive Sedan Automatic",
        "Performance 4dr All-Wheel Drive Sedan Automatic"
    ],
    ("Tesla", 2023, "Model S"): [
        "Base 4dr All-Wheel Drive Hatchback Automatic",
        "Plaid 4dr All-Wheel Drive Hatchback Automatic"
    ],
    ("Tesla", 2023, "Model X"): [
        "Base 4dr Sport Utility Automatic",
        "Plaid 4dr Sport Utility Automatic"
    ],
    ("Tesla", 2023, "Model Y"): [
        "Long Range 4dr All-Wheel Drive Sport Utility Automatic",
        "Performance 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Toyota", 2023, "Bz4X"): [
        "Limited 4dr All-Wheel Drive Automatic",
        "Limited 4dr Front-Wheel Drive Automatic",
        "XLE 4dr All-Wheel Drive Automatic",
        "XLE 4dr Front-Wheel Drive Automatic"
    ],
    ("Toyota", 2023, "Mirai"): [
        "Limited 4dr Sedan Automatic",
        "XLE 4dr Sedan Automatic"
    ],
    ("Volkswagen", 2023, "Id.4"): [
        "PRO 4dr 4X2 Automatic",
        "PRO 4dr All-Wheel Drive Automatic",
        "PRO S 4dr 4X2 Automatic",
        "PRO S 4dr All-Wheel Drive Automatic",
        "PRO S Plus 4dr 4X2 Automatic",
        "PRO S Plus 4dr All-Wheel Drive Automatic",
        "S 4dr 4X2 Automatic",
        "Standard 4dr 4X2 Automatic"
    ],
    ("Volvo", 2023, "C40 Recharge Pure Electric"): [
        "Twin Core 4dr All-Wheel Drive Sport Utility Automatic",
        "Twin Plus 4dr All-Wheel Drive Sport Utility Automatic",
        "Twin Ultimate 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Volvo", 2023, "Xc40 Recharge Pure Electric"): [
        "Twin Core 4dr All-Wheel Drive Sport Utility Automatic",
        "Twin Plus 4dr All-Wheel Drive Sport Utility Automatic",
        "Twin Ultimate 4dr All-Wheel Drive Sport Utility Automatic"
    ],
    ("Audi", 2024, "E Tron"): [],
    ("Audi", 2024, "Q4 E Tron"): [
        "50 Premium 4dr ALL Wheel Drive Quattro Sport Utility Automatic"
    ],
    ("BMW", 2024, "I4"): [
        "M50 4dr ALL Wheel Drive Gran Coupe",
        "Edrive35 4dr Rear Wheel Drive Gran Coupe",
        "Edrive40 4dr Rear Wheel Drive Gran Coupe",
        "Xdrive40 4dr ALL Wheel Drive Gran Coupe"
    ],
    ("BMW", 2024, "I7"): [
        "M70 4dr ALL Wheel Drive Sedan",
        "Edrive50 4dr Rear Wheel Drive Sedan",
        "Xdrive60 4dr ALL Wheel Drive Sedan"
    ],
    ("BMW", 2024, "IX"): [
        "M60 4dr ALL Wheel Drive Sports Activity Vehicle Automatic",
        "Xdrive50 4dr ALL Wheel Drive Sports Activity Vehicle Automatic"
    ],
    ("Cadillac", 2024, "Lyriq"): [
        "Luxury W 1SC 4X2 Automatic",
        "Luxury W 1SD 4X2 Automatic",
        "Luxury W 1SE 4X2 Automatic",
        "Sport W 1SF 4X2 Automatic",
        "Sport W 1SJ 4X2 Automatic",
        "Sport W 1SK 4X2 Automatic",
        "Tech W 1SA 4X2 Automatic"
    ],
    ("Ford", 2024, "F 150 Lightning"): [
        "Flash ALL Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "Lariat ALL Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "Platinum ALL Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "PRO ALL Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic",
        "XLT ALL Wheel Drive Supercrew CAB 5.5 FT. BOX 145 IN. WB Automatic"
    ],
    ("Ford", 2024, "Mustang Mach E"): [
        "Premium 4dr ALL Wheel Drive Automatic"
    ],
    ("Chevrolet", 2024, "Bolt EUV"): [],
    ("Chevrolet", 2024, "Bolt EV"): [],
    ("Genesis", 2024, "Electrified Gv70"): [
        "Advanced 4dr ALL Wheel Drive Automatic"
    ],
    ("Genesis", 2024, "Gv60"): [
        "Advanced 4dr ALL Wheel Drive Automatic",
        "Performance 4dr ALL Wheel Drive",
        "Standard 4dr 4X2 Automatic"
    ],
    ("GMC", 2024, "Hummer EV Pickup"): [
        "2X 4X4 Automatic",
        "3X 4X4 Automatic"
    ],
    ("Hyundai", 2024, "Ioniq 5"): [
        "Limited ALL Wheel Drive Automatic",
        "SE ALL Wheel Drive Automatic",
        "SEL 4X2 Automatic",
        "SEL ALL Wheel Drive Automatic"
    ],
    ("Jaguar", 2024, "I Pace"): [
        "R Dynamic HSE 4dr ALL Wheel Drive Sport Utility Automatic"
    ],
    ("KIA", 2024, "EV6"): [
        "GT Line 4dr ALL Wheel Drive Automatic",
        "Light Long Range 4dr ALL Wheel Drive Automatic",
        "Wind 4dr ALL Wheel Drive Automatic"
    ],
    ("KIA", 2024, "Niro EV"): [
        "Wave 4dr Front Wheel Drive Sport Utility Automatic",
        "Wind 4dr Front Wheel Drive Sport Utility Automatic"
    ],
    ("Lexus", 2024, "RZ 450E"): [
        "Luxury 4dr ALL Wheel Drive Automatic"
    ],
    ("Mercedes-Benz", 2024, "EQB 300"): [
        "Base EQB 300 4dr ALL Wheel Drive 4Matic Automatic"
    ],
    ("Mercedes-Benz", 2024, "EQB 350"): [
        "Base EQB 350 4dr ALL Wheel Drive 4Matic Automatic"
    ],
    ("Toyota", 2024, "Bz4X"): [
        "XLE 4dr Front Wheel Drive Automatic"
    ],
    ("Volkswagen", 2024, "Id.4"): [],
    ("Volvo", 2024, "C40 Recharge Pure Electric"): [
        "Core 4dr Rear Wheel Drive Sport Utility Automatic",
        "Plus 4dr Rear Wheel Drive Sport Utility Automatic",
        "Twin Core 4dr ALL Wheel Drive Sport Utility Automatic",
        "Twin Ultimate 4dr ALL Wheel Drive Sport Utility Automatic",
        "Ultimate 4dr Rear Wheel Drive Sport Utility Automatic"
    ]
}

    for (make, year, model), trims in ev_trims_by_make_year_and_model.items():
        manufacturer_sql = "INSERT INTO EV_MANUFACTURERS (make) VALUES (%s) ON CONFLICT (make) DO NOTHING RETURNING ID"
        cursor.execute(manufacturer_sql, (make,))
        resultA = cursor.fetchone()
        if resultA is None:
            # If no row was inserted (i.e. manufacturer already exists), fetch its id.
            cursor.execute("SELECT id FROM ev_manufacturers WHERE make = %s", (make,))
            manufacturer_id = cursor.fetchone()[0]
        else:
            manufacturer_id = resultA[0]

        model_sql = "INSERT INTO EV_MODELS (manufacturer_id, model, year_produced) VALUES (%s, %s, %s) ON CONFLICT (manufacturer_id, model, year_produced) DO NOTHING RETURNING ID"
        cursor.execute(model_sql, (manufacturer_id, model, year))
        resultB = cursor.fetchone()

        if resultB is None:
            cursor.execute("SELECT id FROM ev_models WHERE (manufacturer_id, model, year_produced) = (%s, %s, %s)", (manufacturer_id, model, year))
            ev_model_id = cursor.fetchone()[0]
        else:
            ev_model_id = resultB[0]
        print("Inserted model id:", ev_model_id)
        
        for trim in trims:
            trim_sql = "INSERT INTO EV_TRIMS (ev_model_id, trim) VALUES (%s, %s) ON CONFLICT (ev_model_id, trim) DO NOTHING RETURNING ID"
            cursor.execute(trim_sql, (ev_model_id, trim))
            resultC = cursor.fetchone()

            if resultC is None:
                cursor.execute("SELECT id FROM ev_trims WHERE (ev_model_id, trim) = (%s, %s)", (ev_model_id, trim))                
                trim_id = cursor.fetchone()[0]
            else:
                trim_id = resultC[0]    
            print("Inserted trim_id", trim_id )
        


            



    
    #manufacturer_id = cursor.fetchone()[0]
    #print(manufacturer_id)

    connection.commit()

insert_ev_data()


