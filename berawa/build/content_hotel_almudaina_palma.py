# Contenido de la demo Hotel Almudaina (Palma) (es/ca/en/fr). Hechos de hotelalmudaina.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble','Superior con terraza','Triple y Cuádruple'],'ca':['Doble','Superior amb terrassa','Triple i Quàdruple'],'en':['Double','Superior with terrace','Triple and Quadruple'],'fr':['Double','Supérieure avec terrasse','Triple et Quadruple']}
RD={
'es':['Decoradas en tonos neutros; puedes elegir cama de matrimonio o dos camas, según disponibilidad (pídelo al reservar).','Para dos personas y con terraza, con vistas de la ciudad desde la Catedral hasta el mar Mediterráneo.','Triples para hasta tres personas y cuádruples amplias para cuatro. También hay individuales e individual económica.'],
'ca':['Decorades en tons neutres; pots triar llit de matrimoni o dos llits, segons disponibilitat (demana-ho en reservar).','Per a dues persones i amb terrassa, amb vistes de la ciutat des de la Catedral fins al mar Mediterrani.','Triples per a fins a tres persones i quàdruples àmplies per a quatre. També hi ha individuals i individual econòmica.'],
'en':['Decorated in neutral tones; choose a double bed or two beds, subject to availability (ask when booking).','For two people and with a terrace, with city views from the Cathedral to the Mediterranean Sea.','Triples for up to three people and spacious quadruples for four. There are also singles and an economy single.'],
'fr':['Décorées dans des tons neutres ; lit double ou deux lits au choix, selon disponibilité (à demander lors de la réservation).','Pour deux personnes et avec terrasse, avec vue sur la ville, de la cathédrale jusqu\'à la Méditerranée.','Triples jusqu\'à trois personnes et quadruples spacieuses pour quatre. Il y a aussi des individuelles et une individuelle économique.']}
ART={
'hero':('skyline',9601,['#1f3a52','#e9a96b','#f6d7a7','#2b4b63','#21394d','#152636']),
'intro':('columns',9602,['#eef0ee','#f8f7f3','#2f5d7c','#1f3a52','#132535']),
'r1':('arches',9611,['#efe9df','#d9b48a','#2f5d7c','#1f3a52','#132535']),
'r2':('waves',9612,['#1f3a52','#eab27a','#f7dfb8','#2f5d7c','#214560','#132535']),
'r3':('columns',9613,['#ecefec','#f7f6f2','#3a6a88','#1f3a52','#132535']),
'g1':('skyline',9621,['#1f3a52','#e5a467','#f4d4a2','#2a4a62','#20384c','#142535']),
'g2':('waves',9622,['#24435c','#ebb47d','#f6dcb3','#2f5d7c','#214560','#132535']),
'g3':('arches',9623,['#ede6db','#d6ae82','#2c5874','#1f3a52','#132535']),
'g4':('hills',9624,['#e4ebe6','#efe7d0','#e8b677','#a4bba0','#7a9883','#52705d']),
'g5':('columns',9625,['#ebeeeb','#f6f5f1','#356585','#1f3a52','#132535']),
'g6':('skyline',9626,['#1f3a52','#e1a063','#f2d09c','#294861','#1f374b','#132434'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Almudaina · Avenida Jaime III, Palma',see_rooms='Ver habitaciones',hero_k='Palma · Avenida Jaime III',hero_t='Palma desde la octava planta',hero_s='Hotel de cuatro estrellas en pleno centro de Palma, con el Sky Area y vistas desde la Catedral hasta el Castillo de Bellver.',
 intro_t='En pleno centro de Palma',intro_p1='El Hotel Almudaina es un hotel de cuatro estrellas, totalmente reformado, en la Avenida Jaime III, con 77 habitaciones, desde individuales hasta cuádruples.',
 intro_p2='Recepción 24 horas, wifi gratis, desayuno buffet con productos locales y, en la octava planta, el Sky Area con bar, terraza y restaurante.',
 stats=['77 habitaciones','Recepción 24 h','Sky Area en la 8.ª planta','Wifi gratis'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individual económica, individual, doble, superior con terraza, triple y cuádruple.',
 svcs=['Recepción 24 horas','Wifi gratis','Desayuno buffet','Leche sin lactosa y pan sin gluten bajo petición','Sky Area: bar, terraza y restaurante','Consigna de equipaje','Alquiler de coches y bicicletas','Toallas de playa (abril a octubre)'],
 loc_p='Avenida Jaime III, 9 · 07012 Palma. Desde el aeropuerto: taxi (unos 15 minutos) o autobús de la línea 1 hasta la parada Paseo Mallorca 18.',
 chips=['¿Qué habitaciones tiene?','¿Qué es el Sky Area?','¿Cómo llego desde el aeropuerto?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Almudaina · Avinguda Jaume III, Palma',see_rooms='Veure habitacions',hero_k='Palma · Avinguda Jaume III',hero_t='Palma des de la vuitena planta',hero_s='Hotel de quatre estrelles al bell mig de Palma, amb el Sky Area i vistes des de la Catedral fins al Castell de Bellver.',
 intro_t='Al bell mig de Palma',intro_p1='L\'Hotel Almudaina és un hotel de quatre estrelles, totalment reformat, a l\'Avinguda Jaume III, amb 77 habitacions, des d\'individuals fins a quàdruples.',
 intro_p2='Recepció 24 hores, wifi gratuït, esmorzar bufet amb productes locals i, a la vuitena planta, el Sky Area amb bar, terrassa i restaurant.',
 stats=['77 habitacions','Recepció 24 h','Sky Area a la 8a planta','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individual econòmica, individual, doble, superior amb terrassa, triple i quàdruple.',
 svcs=['Recepció 24 hores','Wifi gratuït','Esmorzar bufet','Llet sense lactosa i pa sense gluten sota petició','Sky Area: bar, terrassa i restaurant','Consigna d\'equipatge','Lloguer de cotxes i bicicletes','Tovalloles de platja (d\'abril a octubre)'],
 loc_p='Avinguda Jaume III, 9 · 07012 Palma. Des de l\'aeroport: taxi (uns 15 minuts) o autobús de la línia 1 fins a la parada Passeig Mallorca 18.',
 chips=['Quines habitacions té?','Què és el Sky Area?','Com hi arribo des de l\'aeroport?','Com es reserva?']),
'en':dict(title='Hotel Almudaina · Avenida Jaime III, Palma',see_rooms='See the rooms',hero_k='Palma · Avenida Jaime III',hero_t='Palma from the eighth floor',hero_s='Four-star hotel right in the centre of Palma, with the Sky Area and views from the Cathedral to Bellver Castle.',
 intro_t='Right in the centre of Palma',intro_p1='Hotel Almudaina is a fully renovated four-star hotel on Avenida Jaime III, with 77 rooms, from singles to quadruples.',
 intro_p2='24-hour reception, free wifi, buffet breakfast with local products and, on the eighth floor, the Sky Area with bar, terrace and restaurant.',
 stats=['77 rooms','24 h reception','Sky Area on the 8th floor','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Economy single, single, double, superior with terrace, triple and quadruple.',
 svcs=['24-hour reception','Free wifi','Buffet breakfast','Lactose-free milk and gluten-free bread on request','Sky Area: bar, terrace and restaurant','Luggage storage','Car and bike hire','Beach towels (April to October)'],
 loc_p='Avenida Jaime III, 9 · 07012 Palma. From the airport: taxi (about 15 minutes) or bus line 1 to the Paseo Mallorca 18 stop.',
 chips=['What rooms does it have?','What is the Sky Area?','How do I get there from the airport?','How do I book?']),
'fr':dict(title='Hotel Almudaina · Avenida Jaime III, Palma',see_rooms='Voir les chambres',hero_k='Palma · Avenida Jaime III',hero_t='Palma depuis le huitième étage',hero_s='Hôtel quatre étoiles en plein centre de Palma, avec le Sky Area et une vue de la cathédrale jusqu\'au château de Bellver.',
 intro_t='En plein centre de Palma',intro_p1='L\'Hotel Almudaina est un hôtel quatre étoiles entièrement rénové sur l\'Avenida Jaime III, avec 77 chambres, des individuelles aux quadruples.',
 intro_p2='Réception 24h/24, wifi gratuit, petit-déjeuner buffet avec produits locaux et, au huitième étage, le Sky Area avec bar, terrasse et restaurant.',
 stats=['77 chambres','Réception 24h/24','Sky Area au 8e étage','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelle économique, individuelle, double, supérieure avec terrasse, triple et quadruple.',
 svcs=['Réception 24h/24','Wifi gratuit','Petit-déjeuner buffet','Lait sans lactose et pain sans gluten sur demande','Sky Area : bar, terrasse et restaurant','Consigne à bagages','Location de voitures et de vélos','Serviettes de plage (d\'avril à octobre)'],
 loc_p='Avenida Jaime III, 9 · 07012 Palma. Depuis l\'aéroport : taxi (environ 15 minutes) ou bus ligne 1 jusqu\'à l\'arrêt Paseo Mallorca 18.',
 chips=['Quelles chambres a-t-il ?','Qu\'est-ce que le Sky Area ?','Comment venir depuis l\'aéroport ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hotelalmudaina.com/booking-process'; REN='https://www.hotelalmudaina.com/en/booking-process'; RFR='https://www.hotelalmudaina.com/fr/booking-process'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':REN,'fr':RFR})
D=dict(name='Hotel Almudaina',ac='#1f3a52',ac2='#2f5d7c',ac2_a11y='#24496a',book=BOOK,around=[],foot=FOOT,
 address='Avenida Jaime III, 9 · 07012 Palma',phones=['+34 971 727 340'],emails=['info@hotelalmudaina.com'],maps='Hotel Almudaina, Avenida Jaime III 9, Palma',t=T)
META=dict(repo='demo-hotel-almudaina-palma',name='Hotel Almudaina',legal_name='Hotelera Balear, S.A.',registry_ids=['CIF A07008279'],
 url='https://www.hotelalmudaina.com/',domain='hotelalmudaina.com',municipality='Palma',province='Illes Balears',sector='hotel de cuatro estrellas en el centro de Palma (Mallorca)',
 read_at='2026-10-29T16:52:00+01:00',created_at='2026-10-29T16:52:00+01:00',built_at='2026-10-29T17:05:00+01:00',audit_date='2026-10-29T10:40:00+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T10:38:41+01:00',url='https://www.google.com/maps/place/Hotel+Almudaina/@39.571837,2.645342,17z/data=!4m9!3m8!1s0x1297925b13da8ba7:0x2f3483637669c498!5m2!4m1!1i2!8m2!3d39.571837!4d2.645342!16s%2Fg%2F11_q71k19'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (hotelalmudaina.com/booking-process, plataforma Hotetec del propio dominio; versiones /en/ y /fr/); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Tienen habitación con terraza?','K02'),('¿Tienen habitación para cuatro?','K03'),('¿Dónde está?','K04'),('¿Cómo llego desde el aeropuerto?','K05'),('¿A qué hora es la entrada?','K06'),('¿Tienen desayuno?','K07'),('¿Admiten mascotas?','K08'),('¿Hay wifi?','K09'),('¿Qué es el Sky Area?','K10'),('¿Hay aparcamiento?','K11'),('¿Cómo reservo?','K12'),('¿Quién es el titular?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K12'),('¿Tienen spa?',None)],
'ca':[('Quines habitacions té?','K01'),('Teniu habitació amb terrassa?','K02'),('Teniu habitació per a quatre?','K03'),('On és?','K04'),('Com hi arribo des de l\'aeroport?','K05'),('A quina hora és l\'entrada?','K06'),('Teniu esmorzar?','K07'),('Admeteu mascotes?','K08'),('Hi ha wifi?','K09'),('Què és el Sky Area?','K10'),('Hi ha aparcament?','K11'),('Com reservo?','K12'),('Qui és el titular?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K12'),('Teniu spa?',None)],
'en':[('What rooms does it have?','K01'),('Do you have a room with a terrace?','K02'),('Do you have a room for four?','K03'),('Where is it?','K04'),('How do I get there from the airport?','K05'),('What time is check-in?','K06'),('Do you serve breakfast?','K07'),('Are pets allowed?','K08'),('Is there wifi?','K09'),('What is the Sky Area?','K10'),('Is there parking?','K11'),('How do I book?','K12'),('Who is the owner?','K13'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K12'),('Is there a spa?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Avez-vous une chambre avec terrasse ?','K02'),('Avez-vous une chambre pour quatre ?','K03'),('Où est-il ?','K04'),('Comment venir depuis l\'aéroport ?','K05'),('À quelle heure est l\'arrivée ?','K06'),('Servez-vous le petit-déjeuner ?','K07'),('Les animaux sont-ils admis ?','K08'),('Y a-t-il le wifi ?','K09'),('Qu\'est-ce que le Sky Area ?','K10'),('Y a-t-il un parking ?','K11'),('Comment réserver ?','K12'),('Qui est le titulaire ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K12'),('Y a-t-il un spa ?',None)]}
