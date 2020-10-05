1) Le fetch du modeClim en python ne fonctionne pas, ajuster la fonction getGlobalSettings.
2) Un bouton pour on/off manuellement pour les fournaise.
3) faire changer la couleur du mode clim selon le mode.
4) en mode clim aussi activer le relay_mode_climatisation
5) Systeme independant pour la thermo, 

6) chauffage, heat la thermo si la temperature de la thermo est en bas de la demande (temperature + degree de correction), on part la switch de la pompe, apres on part l'element. 
  
  quand la temperature est atteinte, on ferme l'élément, on ferme la pompe apres un delay (variable = delay de fermeture de la pompe de thermo)
  
  
  climatisation, si la temperature est au dessous de la demande, on part la pompe et ensuite le relay,
  
  quand la temperature est atteinte on ferme la pompe + delais variable.
  
7) mini script pour activer un GPIO on demand, on et off.






70.52.38.147 (jo house)
192.168.2.34 (db + site + sensor)
192.168.2.174 (etage sensor)
192.168.2.171 (relays)

Sensor DHT22-Temperature, setup is [DONE]
DS18B20 Sensor, setup is [DONE]

Need to adjust the main.py for relays.

Add the "type" columns in rooms. (utility or heat or clim)

Check room and heat based off type instead of mode.

Function, 
 
 


