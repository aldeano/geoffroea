# -*- coding: utf-8 -*-

tipos_usuarios = (
    ("adm", "Administrador"),
    ("er", "Encargado(a) Regional"),
    ("jf", "Jefe(a) de Turno"),
    ("insp", "Inspector")
    )

tipos_documentos = (
    ("ci", "Carnet de Identidad"),
    ("pas", "Pasaporte"),
    ("otro", "Otro")
    )

opciones_genero = (
    ("m", "Masculino"),
    ("f", "Femenino")
    )

horarios_ccff = (
    ("continuado", "continuado"),
    ("turnos", "turnos"),
    ("esporadico", "esporádico")
    )

tipo_transporte = (
    ("nave", "Nave"),
    ("avion", "Avión"),
    ("tren", "Tren"),
    ("bus", "Bus"),
    ("camion", "Camión"),
    ("auto", "Auto"),
    ("moto", "Moto"),
    ("otro", "Otro")
    )

medidas_destruccion = (
    ("incineracion", "Incineración"),
    ("autoclave", "Autoclave"),
    ("enterramiento", "Enterramiento"),
    ("otro", "Otro")
    )

def ubicacion(tipo_control):
'''Define la lista de opciones donde es encontrada una intercepción
, le tiene que pasar el tipo de control - terrestre, marítimo o aéreo - 
para definir la lista final '''
    lista = [
    ["equipaje", "Equipaje"],
    ]
    if tipo_control == "terrestre":
        lista.append(["Pasajeros"], [
            ["bicicleta", "Bicicleta"],
            ["bus", "Bus"],
            ["moto", "Motocicleta"],
            ["tren", "Tren"],
            ["veh_dipl", "Vehículo Diplomático"],
            ["veh_part", "Vehículo Particular"],
            ["veh_hum", "Vehículo con Tracción Humana"]
            ],
            ["Carga"], [
            ["atingente", "Carga atingente a SAG"],
            ["no_atingente", "Carga no atingente a SAG"]
            ],
            ["FFAA"], [
            ["auto", "Auto"],
            ["bus", "Bus"],
            ["carga_atingente", "Carga atingente a SAG"],
            ["carga_no_atingente", "Carga no atingente a SAG"]
            ])
    elif tipo_control == "aereo":
        lista.append(["Pasajeros"], [
            ["avion", "Avión"],
            ["avioneta", "Avioneta"],
            ["helicoptero", "Helicóptero"]
            ],
            ["Carga"], [
            ["avion", "Avión"]
            ],
            ["FFAA"], [
            ["avion_carga", "Avión de Carga"],
            ["avion_pas", "Avión de Pasajeros"],
            ["avioneta", "Avioneta"],
            ["helicoptero", "Helicóptero"]
            ])
    else:
        lista.append(["Pasajeros"], [
            ["crucero", "Crucero"],
            ["velero", "Velero"],
            ],
            ["Carga"], [
            ["cisterna", "Barco Cisterna"],
            ["contenedor", "Barco Contenedor"],
            ["mercante", "Barco Mercante"]
            ],
            ["FFAA"], [
            ["guerra", "Buque de Guerra"],
            ["instruccion", "Buque de Instrucción"],
            ["psj-carga", "Buque de Pasajeros-Carga"],
            ["tanque", "Buque Tanque"]
            ]) 
    return lista

'''
Listado de puertos que tengo que modificar para hacerlos presentables
<option value="2"   >PTO. DE ARICA</option>
                                        
<option value="9"   >PUERTO DE IQUIQUE</option>

<option value="10"   >PUERTO DE PATACHE</option>

<option value="11"   >PUERTO DE PATILLO</option>

<option value="18"   >PUERTO DE MEJILLONES</option>

<option value="14"   >CALETA COLOSO</option>

<option value="19"   >PUERTO DE TOCOPILLA</option>

<option value="16"   >PUERTO DE ANGAMOS</option>

<option value="17"   >PUERTO DE ANTOFAGASTA</option>

<option value="15"   >CALETA MICHILLA</option>

<option value="27"   >PUERTO DE BARQUITO</option>

<option value="100"   >PUERTO PUNTA TOTORALILLO</option>

<option value="26"   >PUERTO DE CALDERA</option>

<option value="30"   >PUERTO DE HUASCO</option>

<option value="32"   >PUNTA DE CHUNGOS</option>

<option value="34"   >PUERTO DE COQUIMBO</option>

<option value="35"   >PUERTO DE GUAYACAN</option>

<option value="38"   >PUERTO POLICARPO TORO</option>

<option value="41"   >PUERTO DE QUINTERO</option>

<option value="42"   >PUERTO DE VENTANAS</option>

<option value="43"   >PUERTO DE SAN ANTONIO</option>

<option value="97"   >PUERTO SAN JUAN BAUTISTA</option>

<option value="44"   >PUERTO DE VALPARAISO</option>

<option value="51"   >PUERTO DE PENCO</option>

<option value="52"   >PUERTO DE SAN VICENTE</option>

<option value="54"   >PUERTO MOLO 500</option>

<option value="50"   >PUERTO DE LIRQUEN</option>

<option value="49"   >PUERTO DE CORONEL</option>

<option value="53"   >PUERTO DE TALCAHUANO</option>

<option value="95"   >PUERTO DE ANCUD</option>

<option value="59"   >PUERTO DE CASTRO</option>

<option value="64"   >PTO. DE PUERTO MONTT</option>

<option value="65"   >PUERTO DE SAN JOSÉ</option>

<option value="67"   >PUERTO DE CORRAL</option>

<option value="75"   >PUERTO CHACABUCO</option>

<option value="77"   >PUERTO NAVARINO</option>

<option value="96"   >PUERTO WILLIAMS</option>

<option value="98"   >NUEVO PUERTO DE BAHÍA CATALINA</option>

<option value="79"   >PTO. JOSÉ SANTOS MARDONES</option>

<option value="83"   >PTO. DE PUERTO NATALES</option>
'''

#obtenido en https://github.com/witoi/django-cl/
comunas = (
    # ('15', u'Región de Arica y Parinacota'),
    ('15101', u'Arica'),
    ('15102', u'Camarones'), 
    ('15201', u'Putre'),
    ('15202', u'General '),

    # ('01', u'Región de Tarapacá'),
    ('01101', u'Iquique'),
    ('01107', u'Alto Hospicio'),
    ('01401', u'Pozo Almonte'),
    ('01402', u'Camiña'),
    ('01403', u'Colchane'),
    ('01404', u'Huara'),
    ('01405', u'Pica'),

    # ('02', u'Región de Antofagasta'),
    ('02101', u'Antofagasta'),
    ('02102', u'Mejillones'),
    ('02103', u'Sierra Gorda'),
    ('02104', u'Taltal'),
    ('02201', u'Calama'),
    ('02202', u'Ollagüe'),
    ('02203', u'San Pedro de Atacama'),
    ('02301', u'Tocopilla'),
    ('02302', u'María Elena'),

    # ('03', u'Región de Atacama'),
    ('03101', u'Copiapó'),
    ('03102', u'Caldera'),
    ('03103', u'Tierra Amarilla'),
    ('03201', u'Chañaral'),
    ('03202', u'Diego de Almagro'),
    ('03301', u'Vallenar'),
    ('03302', u'Alto del Carmen'),
    ('03303', u'Freirina'),
    ('03304', u'Huasco'),

    # ('04', u'Región de Coquimbo'),
    ('04101', u'La Serena'),
    ('04102', u'Coquimbo'),
    ('04103', u'Andacollo'),
    ('04104', u'La Higuera'),
    ('04105', u'Paiguano'),
    ('04106', u'Vicuña'),
    ('04201', u'Illapel'),
    ('04202', u'Canela'),
    ('04203', u'Los Vilos'),
    ('04204', u'Salamanca'),
    ('04301', u'Ovalle'),
    ('04302', u'Combarbalá'),
    ('04303', u'Monte Patria'),
    ('04304', u'Punitaqui'),
    ('04305', u'Río Hurtado'),

    # ('05', u'Región de Valparaíso'),
    ('05101', u'Valparaíso'),
    ('05102', u'Casablanca'),
    ('05103', u'Concón'),
    ('05104', u'Juan Fernández'),
    ('05105', u'Puchuncaví'),
    ('05107', u'Quintero'),
    ('05109', u'Viña del Mar'),
    ('05201', u'Isla de Pascua'),
    ('05301', u'Los Andes'),
    ('05302', u'Calle Larga'),
    ('05303', u'Rinconada'),
    ('05304', u'San Esteban'),
    ('05401', u'La Ligua'),
    ('05402', u'Cabildo'),
    ('05403', u'Papudo'),
    ('05404', u'Petorca'),
    ('05405', u'Zapallar'),
    ('05501', u'Quillota'),
    ('05502', u'Calera'),
    ('05503', u'Hijuelas'),
    ('05504', u'La Cruz'),
    ('05506', u'Nogales'),
    ('05601', u'San Antonio'),
    ('05602', u'Algarrobo'),
    ('05603', u'Cartagena'),
    ('05604', u'El Quisco'),
    ('05605', u'El Tabo'),
    ('05606', u'Santo Domingo'),
    ('05701', u'San Felipe'),
    ('05702', u'Catemu'),
    ('05703', u'Llaillay'),
    ('05704', u'Panquehue'),
    ('05705', u'Putaendo'),
    ('05706', u'Santa María'),
    ('05801', u'Quilpué'),
    ('05801', u'Limache'),
    ('05801', u'Olmué'),
    ('05801', u'Villa Alemana'),

    # ('06', u'Región del Libertador General Bernardo O\'Higgins'),
    ('06101', u'Rancagua'),
    ('06102', u'Codegua'),
    ('06103', u'Coinco'),
    ('06104', u'Coltauco'),
    ('06105', u'Doñihue'),
    ('06106', u'Graneros'),
    ('06107', u'Las Cabras'),
    ('06108', u'Machalí'),
    ('06109', u'Malloa'),
    ('06110', u'Mostazal'),
    ('06111', u'Olivar'),
    ('06112', u'Peumo'),
    ('06113', u'Pichidegua'),
    ('06114', u'Quinta de Tilcoco'),
    ('06115', u'Rengo'),
    ('06116', u'Requínoa'),
    ('06117', u'San Vicente'),
    ('06201', u'Pichilemu'),
    ('06202', u'La Estrella'),
    ('06203', u'Litueche'),
    ('06204', u'Marchihue'),
    ('06205', u'Navidad'),
    ('06206', u'Paredones'),
    ('06301', u'San Fernando'),
    ('06302', u'Chépica'),
    ('06303', u'Chimbarongo'),
    ('06304', u'Lolol'),
    ('06305', u'Nancagua'),
    ('06306', u'Palmilla'),
    ('06307', u'Peralillo'),
    ('06308', u'Placilla'),
    ('06309', u'Pumanque'),
    ('06310', u'Santa Cruz'),

    # ('07', u'Región del Maule'),
    ('07101', u'Talca'),
    ('07102', u'Constitución'),
    ('07103', u'Curepto'),
    ('07104', u'Empedrado'),
    ('07105', u'Maule'),
    ('07106', u'Pelarco'),
    ('07107', u'Pencahue'),
    ('07108', u'Río Claro'),
    ('07109', u'San Clemente'),
    ('07110', u'San Rafael'),
    ('07201', u'Cauquenes'),
    ('07202', u'Chanco'),
    ('07203', u'Pelluhue'),
    ('07301', u'Curicó'),
    ('07302', u'Hualañe'),
    ('07303', u'Licantén'),
    ('07304', u'Molina'),
    ('07305', u'Rauco'),
    ('07306', u'Romeral'),
    ('07307', u'Sagrada Familia'),
    ('07308', u'Teno'),
    ('07309', u'Vichuquén'),
    ('07401', u'Linares'),
    ('07402', u'Colbún'),
    ('07403', u'Longaví'),
    ('07404', u'Parral'),
    ('07405', u'Retiro'),
    ('07406', u'San Javier'),
    ('07407', u'Villa Alegre'),
    ('07408', u'Yerbas Buenas'),

    # ('08', u'Región del Biobío'),
    ('08101', u'Concepción'),
    ('08102', u'Coronel'),
    ('08103', u'Chiguayante'),
    ('08104', u'Florida'),
    ('08105', u'Hualqui'),
    ('08106', u'Lota'),
    ('08107', u'Penco'),
    ('08108', u'San Pedro de la Paz'),
    ('08109', u'Santa Juana'),
    ('08110', u'Talcahuano'),
    ('08111', u'Tompe'),
    ('08112', u'Hualpén'),
    ('08201', u'Lebu'),
    ('08202', u'Arauco'),
    ('08203', u'Cañeete'),
    ('08204', u'Contulmo'),
    ('08205', u'Curanilahue'),
    ('08206', u'Los Alamos'),
    ('08207', u'Tirúa'),
    ('08301', u'Los Angeles'),
    ('08302', u'Antuco'),
    ('08303', u'Cabrero'),
    ('08304', u'Laja'),
    ('08305', u'Mulchén'),
    ('08306', u'Nacimiento'),
    ('08307', u'Negrete'),
    ('08308', u'Quilaco'),
    ('08309', u'Quilleco'),
    ('08310', u'San Rosendo'),
    ('08311', u'Santa Bárbara'),
    ('08312', u'Tucapel'),
    ('08313', u'Yumbel'),
    ('08314', u'Alto Biobío'),
    ('08401', u'Chillán'),
    ('08402', u'Bulnes'),
    ('08403', u'Cobquecura'),
    ('08404', u'Coelemu'),
    ('08405', u'Coihueco'),
    ('08406', u'Chillán Viejo'),
    ('08407', u'El Carmen'),
    ('08408', u'Ninhue'),
    ('08409', u'Ñiquén'),
    ('08410', u'Pemuco'),
    ('08411', u'Pinto'),
    ('08412', u'Portezuelo'),
    ('08413', u'Quillón'),
    ('08414', u'Quirihue'),
    ('08415', u'Ráuil'),
    ('08416', u'San Carlos'),
    ('08417', u'San Fabián'),
    ('08418', u'San Ignacio'),
    ('08419', u'San Nicolás'),
    ('08420', u'Treguaco'),
    ('08421', u'Yungay'),

    # ('09', u'Región de La Araucanía'),
    ('09101', u'Temuco'),
    ('09102', u'Carahue'),
    ('09103', u'Cunco'),
    ('09104', u'Curarrehue'),
    ('09105', u'Freire'),
    ('09106', u'Galvarino'),
    ('09107', u'Gorbea'),
    ('09108', u'Lautaro'),
    ('09109', u'Loncoche'),
    ('09110', u'Melipeuco'),
    ('09111', u'Nueva Imperial'),
    ('09112', u'Padre Las Casas'),
    ('09113', u'Perquenco'),
    ('09114', u'Pitrufquén'),
    ('09115', u'Pucón'),
    ('09116', u'Saavedra'),
    ('09117', u'Teodoro Schmidt'),
    ('09118', u'Toltén'),
    ('09119', u'Vilcún'),
    ('09120', u'Villarrica'),
    ('09121', u'Cholchol'),
    ('09201', u'Angol'),
    ('09202', u'Collipulli'),
    ('09203', u'Curacautín'),
    ('09204', u'Ercilla'),
    ('09205', u'Lonquimay'),
    ('09206', u'Los Sauces'),
    ('09207', u'Lumaco'),
    ('09208', u'Purén'),
    ('09209', u'Renaico'),
    ('09210', u'Traiguén'),
    ('09211', u'Victoria'),

    # ('14', u'Región de Los Ríos'),
    ('14101', u'Valdivia'),
    ('14102', u'Corral'),
    ('14103', u'Lanco'),
    ('14104', u'Los Lagos'),
    ('14105', u'Máfil'),
    ('14106', u'Mariquina'),
    ('14107', u'Paillaco'),
    ('14108', u'Panguipulli'),
    ('14201', u'La Unión'),
    ('14202', u'Futrono'),
    ('14203', u'Lago Ranco'),
    ('14204', u'Río Bueno'),

    # ('10', u'Región de Los Lagos'),
    ('10101', u'Puerto Montt'),
    ('10102', u'Calbuco'),
    ('10103', u'Cochamó'),
    ('10104', u'Fresia'),
    ('10105', u'Frutillar'),
    ('10106', u'Los Muermos'),
    ('10107', u'Llanquihue'),
    ('10108', u'Maullín'),
    ('10109', u'Puerto Varas'),
    ('10201', u'Castro'),
    ('10202', u'Ancud'),
    ('10203', u'Chonchi'),
    ('10204', u'Curaco de Vélez'),
    ('10205', u'Dalcahue'),
    ('10206', u'Puqueldón'),
    ('10207', u'Queilén'),
    ('10208', u'Quellón'),
    ('10209', u'Quemchi'),
    ('10210', u'Quinchao'),
    ('10301', u'Osorno'),
    ('10302', u'Puerto Octay'),
    ('10303', u'Purranque'),
    ('10304', u'Puyehue'),
    ('10305', u'Río Negro'),
    ('10306', u'San Juan de la Costa'),
    ('10307', u'San Pablo'),
    ('10401', u'Chaitén'),
    ('10402', u'Futaleufú'),
    ('10403', u'Hualaihué'),
    ('10404', u'Palena'),

    # ('11', u'Región de Aisén del General Carlos Ibañez del Campo'),
    ('11101', u'Coihaique'),
    ('11102', u'Lago Verde'),
    ('11201', u'Aisén'),
    ('11202', u'Cisnes'),
    ('11203', u'Guaitecas'),
    ('11301', u'Cochrane'),
    ('11302', u'O\'Higgins'),
    ('11303', u'Tortel'),
    ('11401', u'Chile Chico'),
    ('11402', u'Río Ibáñez'),

    # ('12', u'Región de Magallanes y de la Antártica Chilena'),
    ('12101', u'Punta Arenas'),
    ('12102', u'Laguna Blanca'),
    ('12103', u'Río Verde'),
    ('12104', u'San Gregorio'),
    ('12201', u'Cabo de Hornos'),
    ('12202', u'Antártica'),
    ('12301', u'Porvenir'),
    ('12302', u'Primavera'),
    ('12303', u'Timaukel'),
    ('12401', u'Natales'),
    ('12402', u'Torres del Paine'),

    # ('13', u'Región Metropolitana de Santiago'),
    ('13101', u'Santiago'),
    ('13102', u'Cerrillos'),
    ('13103', u'Cerro Navia'),
    ('13104', u'Conchalí'),
    ('13105', u'El Bosque'),
    ('13106', u'Estación Central'),
    ('13107', u'Huechuraba'),
    ('13108', u'Independencia'),
    ('13109', u'La Cisterna'),
    ('13110', u'La Florida'),
    ('13111', u'La Granja'),
    ('13112', u'La Pintana'),
    ('13113', u'La Reina'),
    ('13114', u'Las Condes'),
    ('13115', u'Lo Barnechea'),
    ('13116', u'Lo Espejo'),
    ('13117', u'Lo Prado'),
    ('13118', u'Macul'),
    ('13119', u'Maipú'),
    ('13120', u'Ñuñoa'),
    ('13121', u'Pedro Aguirre Cerda'),
    ('13122', u'Peñalolén'),
    ('13123', u'Providencia'),
    ('13124', u'Pudahuel'),
    ('13125', u'Quilicura'),
    ('13126', u'Quinta Normal'),
    ('13127', u'Recoleta'),
    ('13128', u'Renca'),
    ('13129', u'San Joaquín'),
    ('13130', u'San Miguel'),
    ('13131', u'San Ramón'),
    ('13132', u'Vitacura'),
    ('13201', u'Puente Alto'),
    ('13202', u'Pirque'),
    ('13203', u'San José de Maipo'),
    ('13301', u'Colina'),
    ('13302', u'Lampa'),
    ('13303', u'Tiltil'),
    ('13401', u'San Bernardo'),
    ('13402', u'Buin'),
    ('13403', u'Calera de Tango'),
    ('13404', u'Paine'),
    ('13501', u'Melipilla'),
    ('13502', u'Alhué'),
    ('13503', u'Curacaví'),
    ('13504', u'María Pinto'),
    ('13505', u'San Pedro'),
    ('13601', u'Talagante'),
    ('13602', u'El Monte'),
    ('13603', u'Isla de Maipo'),
    ('13604', u'Padre Hurtado'),
    ('13605', u'Peñaflor'),
)