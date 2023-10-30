import streamlit as st
from unidecode import unidecode
import requests
import json

st.title("Estimation des émissions de CO2")

st.image("https://cdn.pixabay.com/photo/2020/01/15/09/13/co2-4767388_1280.jpg")


tab1, tab2 = st.tabs(["Mode d'emploi", "Formulaire"])

with tab1:
    st.header("Comment a été construit cet outil ?")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet ligula velit. Aliquam erat volutpat. Integer mollis sapien ut libero dictum, feugiat tincidunt nisl ultricies. Fusce volutpat ligula vel lacus consequat scelerisque. Pellentesque aliquet nunc eu nunc consequat efficitur. Duis ornare dui nec faucibus congue. Duis in iaculis arcu. Ut aliquet leo arcu, eu luctus neque cursus eget. Vestibulum gravida condimentum urna iaculis consectetur. Fusce nec ante vel ante laoreet porttitor. Nulla sit amet sem ligula. Sed pharetra tortor at sapien auctor, eu porta lorem vehicula. Donec a mi in enim feugiat vulputate. Vivamus ullamcorper augue vel faucibus tempus. Phasellus tempus eget lectus a vehicula. Proin tincidunt felis aliquet bibendum pulvinar.")
    st.write("**Sources**")
    st.markdown("- [Données ayant servi à créer le modèle](https://data.ademe.fr/datasets/ademe-car-labelling)")
    st.markdown("- [Lire sa carte grise](https://www.cartegrise.com/carte-grise-detail)")
    st.markdown("- [Explication du cycle WLTP](https://www.reezocar.com/blog/conseils/quest-ce-que-le-cycle-de-consommation-wltp-12215.html)")
    st.markdown("- [Code Source](https://github.com/cecilegltslmcs/emissions_co2_voiture)")

with tab2:
    with st.form("Entrez les caractéristiques du véhicule"):
        c1, c2 = st.columns(2)
        with c1:
            marque = st.selectbox("Marque du véhicule : ",
                                    sorted(['Renault', 'Mazda', 'DS', 'B.M.W.', 'Skoda', 'Jeep', 'Mini', 'Citroen', 'Nissan',
                                    'Volkswagen', 'Alfa Romeo', 'Opel', 'Dacia', 'Kia', 'Mercedes', 'Seat',
                                    'Porsche', 'Ford', 'Peugeot', 'Fiat', 'Lexus', 'Toyota', 'Suzuki', 'Hyundai',
                                    'Land Rover', 'Volvo', 'Audi', 'Rolls Royce', 'Honda', 'M.G.', 'Mitsubishi',
                                    'Cupra', 'Smart', 'Tesla', 'Jaguar', 'Lamborghini', 'Ferrari', 'Alpine',
                                    'Maserati', 'Subaru', 'Ssangyong', 'Bentley']),                                
                                    index=None,
                                    placeholder="Choisissez une option...",
                                    help=" Cette information est présente dans la case D1 de la carte grise du véhicule.")
            modele = st.selectbox("Modèle du véhicule : ",
                                    ("Kangoo", "Clio"),
                                    index=None,
                                    placeholder="Choisissez une option...",
                                    help="Identique à la dénomination commerciale du véhicule présente dans la case D2 de la carte grise du véhicule.")
            energie = st.selectbox("Source d'énergie : ",
                                    ('Essence', 'Elec+Essenc HR', 'Ess+Elec HNR', 'Gazole',
                                    'Gaz+Elec HNR', 'Elec+Gazole HR', 'Ess+G.P.L.', 'Superéthanol', 'Gaz Nat.Veh'),
                                    index=None,
                                    placeholder="Choisissez une option...",
                                    help="La mention HR signifie Hybride Rechargeable et HNR Hybride Non Rechargeable.  Cette information est présente dans la case P3 de la carte grise du véhicule.")
            carrosserie = st.selectbox("Carrosserie :",
                                        ('Combispace', 'Ts terrains/Chemins', 'Monospace compact', 'Berline', 'Break',
                                        'Coupé', 'Minibus', 'Cabriolet', 'Monospace', 'Minispace'),
                                        index=None,
                                        placeholder="Choisissez une option...")
            gamme = st.selectbox("Gamme du véhicule :",
                                ('Inférieure', 'Moyenne Supérieure', 'Moyenne Inférieure', 'Luxe', 'Supérieure', 'Economique'),
                                index=None,
                                placeholder="Choisissez une option...")
            type_de_boite = st.selectbox("Type de boîte : ",
                                ('Automatique', 'Mécanique', 'Variation continue'),
                                index=None,
                                placeholder="Choisissez une option...")
            nombre_rapports = st.slider("Nombre de vitesses : ", 0, 9, 6)
            bonus_malus = st.selectbox("Lors de son achat le véhicule bénéficie-t-il du",
                                ('Malus', 'Bonus', 'Neutre', 'Autre'),
                                index=None,
                                placeholder="Choisissez une option...")
        
        with c2:
            cylindree = st.number_input("Cylindrée",
                                        value=None,
                                        placeholder="Entrez une valeur entière (en cm3)",
                                        help="Exprimée en cm3. Cette information est présente dans la case P1 de la carte grise du véhicule.")
            puissance_fiscale = st.number_input("Puissance administrative nationale",
                                                value=None,
                                                placeholder="Entrez une valeur entière (en CV)",
                                                min_value=4,
                                                max_value=95,
                                                help="Aussi appelée \"Chevaux fiscaux\". Exprimée en CV avec une valeur comprise entre 4 et 95. Cette information est présente dans la case P6 de la carte grise du véhicule.")
            puissance_max = st.number_input("Puissante nette maximale",
                                            value=None,
                                            placeholder="Entrez une valeur entière (en kW)",
                                            min_value=45,
                                            max_value=610,
                                            help="Exprimée en kW avec une valleur comprise entre 45 et 610kW. Cette information est présente dans la case P2 de la carte grise du véhicule.")
            poids = st.number_input("Poids à vide",
                                    value = None,
                                    placeholder="Entrez une valeur entière (en kilos)",
                                    min_value=800,
                                    max_value=2800,
                                    help="Exprimée en kilogrammes. Cette information est présente dans la case G1 de la carte grise du véhicule.")
            
            conso_basse_vitesse = st.number_input("Consommation à basse vitesse :",
                                                value=None,
                                                placeholder="Entrez une valeur décimale (en L/100km)",
                                                help="Exprimée en L pour 100 km. Elle correspond à une circulation en ville (max 56.5 km/h).")
            conso_vitesse_moyenne = st.number_input("Consommation à moyenne vitesse :",
                                                    value=None,
                                                    placeholder="Entrez une valeur décimale (en L/100km)",
                                                    help="Exprimée en L pour 100 km. Elle correspond à une circulation en milieu extra-urbain (max 76.6 km/h).")
            conso_haute_vitesse = st.number_input("Consommation à haute vitesse :",
                                                value=None,
                                                placeholder="Entrez une valeur décimale (en L/100km)",
                                                help="Exprimée en L pour 100 km. Elle correspond à une circulation sur route (max 97.4 km/h).")
            conso_tres_haute_vitesse = st.number_input("Consommation à très haute vitesse  :",
                                                    value=None,
                                                    placeholder="Entrez une valeur décimale (en L/100km)",
                                                    help="Exprimée en L pour 100 km. Elle correspond à une circulation sur autoroute (moy 131.3 km/h).")
            conso_vitesse_mixte = st.number_input("Consommation à vitesse mixte :",
                                                value=None,
                                                placeholder="Entrez une valeur décimale (en L/100km)",
                                                help="Exprimée en L pour 100 km.")
            
        submitted = st.form_submit_button("Envoyer")
        
    if submitted:
        carrosserie = carrosserie.replace(" ", "_").lower()
        gamme = gamme.replace(" ", "_").lower()
        type_de_boite = type_de_boite.replace(" ", "_").lower()
        
        car = {
            "Marque" : marque.lower(),
            "Modèle" : modele.lower(),
            "Energie" : energie.lower(),
            "Carrosserie" : carrosserie,
            "Cylindrée" : cylindree,
            "Gamme" : unidecode(gamme),
            "Puissance fiscale" : puissance_fiscale,
            "Puissance maximale" : puissance_max,
            "Poids à vide" : poids,
            "Rapport poids-puissance" : float(poids/puissance_max),
            "Type de boîte" : decode(type_de_boite),
            "Nombre rapports" : nombre_rapports,
            "Conso basse vitesse" : float(conso_basse_vitesse),
            "Conso moyenne vitesse" : float(conso_vitesse_moyenne),
            "Conso haute vitesse" : float(conso_haute_vitesse),
            "Conso T-haute vitesse" : float(conso_tres_haute_vitesse),
            "Conso vitesse mixte" : float(conso_vitesse_mixte)
        }
    
        json_car = json.dumps(car, indent=4)
        headers = {"Content-Type": "application/json"}
        req = requests.post("http://127.0.0.1:8000/predict",
                            data = json_car,
                            headers = headers)
        result = req.json()
            
        st.write(f"Emission de CO2 estimée: {result} g/km.")
    
# st.text("Réalisée par Cécile Guillot")