import streamlit as st
import requests
import json

st.title("Estimation des émissions de CO2")

st.image("https://cdn.pixabay.com/photo/2020/01/15/09/13/co2-4767388_1280.jpg")

with st.form("Entrez les caractéristiques du véhicule"):
    c1, c2 = st.columns(2)
    with c1:
        marque = st.selectbox("Sélectionnez la marque du véhicule : ",
                                ('Renault', 'Mazda', 'DS', 'B.M.W.', 'Skoda', 'Jeep', 'Mini', 'Citroen', 'Nissan',
                                'Volkswagen', 'Alfa Romeo', 'Opel', 'Dacia', 'Kia', 'Mercedes', 'Seat',
                                'Porsche', 'Ford', 'Peugeot', 'Fiat', 'Lexus', 'Toyota', 'Suzuki', 'Hyundai',
                                'Land Rover', 'Volvo', 'Audi', 'Rolls Royce', 'Honda', 'M.G.', 'Mitsubishi',
                                'Cupra', 'Smart', 'Testa', 'Jaguar', 'Lamborghini', 'Ferrari', 'Alpine',
                                'Maserati', 'Subaru', 'Ssangyong', 'Bentley'),                                
                                index=None,
                                placeholder="Choisissez une option...")
        modele = st.selectbox("Sélectionnez le modèle du véhicule : ",
                                ("Kangoo", "Clio"),
                                index=None,
                                placeholder="Choisissez une option...")
        energie = st.selectbox("Sélectionnez le type de motorisation : ",
                                ('Essence', 'Elec+Essenc HR', 'Ess+Elec HNR', 'Gazole',
                                'Gaz+Elec HNR', 'Elec+Gazole HR', 'Ess+G.P.L.', 'Superéthanol', 'Gaz Nat.Veh'),
                                index=None,
                                placeholder="Choisissez une option...")
        carrosserie = st.selectbox("Sélectionnez le type de carrosserie :", 
                                    ('Combispace', 'Ts terrains/Chemins', 'Monospace compact', 'Berline', 'Break',
                                        'Coupé', 'Minibus', 'Cabriolet', 'Monospace', 'Minispace'),
                                    index=None,
                                    placeholder="Choisissez une option...")
        gamme = st.selectbox("Sélectionnez la gamme du véhicule :", 
                            ('Inférieure', 'Moyenne Supérieure', 'Moyenne Inférieure', 'Luxe', 'Supérieure', 'Economique'),
                            index=None,
                            placeholder="Choisissez une option...")
        type_de_boite = st.radio("Sélectionnez le type de boîte : ", 
                             ('Automatique', 'Mécanique', 'Variation continue'))
        nombre_rapports = st.number_input("Saisissez le nombre de rapports (entre 0 et 8)")
        bonus_malus = st.radio("Lors de son achat le véhicule bénéficie-t-il du", 
                              ('Malus', 'Bonus', 'Neutre', 'Autres'))
    
    with c2:
        cylindree = st.number_input("Saisissez le cylindrée (en cm3)")
        puissance_fiscale = st.number_input("Saisissez la puissance fiscale (en CV fiscaux)")
        puissance_max = st.number_input("Saisissez la puissance maximale (en kW)")
        poids = st.number_input("Saisissez le poids (en kilo)")
        
        conso_basse_vitesse = st.number_input("Saissisez la consommation à basse vitesse (en L pour 100km)")
        conso_vitesse_moyenne = st.number_input("Saissisez la consommation à vitesse moyenne (en L pour 100km)")
        conso_haute_vitesse = st.number_input("Saissisez la consommation à haute vitesse (en L pour 100km)")
        conso_tres_haute_vitesse = st.number_input("Saissisez la consommation à très haute vitesse (en L pour 100km)")
        conso_vitesse_mixte = st.number_input("Saissisez la consommation à vitesse mixte (en L pour 100km)")
        
    submitted = st.form_submit_button("Envoyer")
    
st.text("Réalisée par Cécile Guillot")