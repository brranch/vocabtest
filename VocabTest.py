# -*- coding: utf-8 -*-
# import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
BasicVocab = ['']
AdvancedVocab = ['abandonado','abarcar','abarquillar','abastecimiento','abatible','abdicar','abdomen','abecedario','abolicionista','abono','abrasivo','abrochar ','abrupto ','absolución','absorber ','absorción','abultar ','abusivo','acacia ','academicismo','acahual ','acallar ','acampanado ','acanaladura','acantáceo','acápite ','acaracolado','acaramelado','acarrear ','acérrimo ','acharolado ','achicharrar','aclamación ','acolchado ','acólito ','acondicionador','acordeonista','acreedor ','acribillar ','acromático','actitud ','actividad ','actual ','actualización','acuarela ','acuchillamiento','acueducto','acuerdo ','acupuntura ','acusar ','ademán ','adenología','adicción ','adivino ','admisible ','adolecer ','adolescente','adoquín','aeronáutica','aeropuerto','afín','agarrotado','agazaparse','agosto ','agravio ','aguarrás ','agudización ','aherrumbrar','ahora ','ahorrativa ','ahumado','aire ','ajedrez','ajeno ','ajonjolí','alacena','alacrán','alambique','albañil','albino','álbum ','alcachofa','alcahuete','alcancía','alcantarillado','alcoba','alcornoque','alcurnia','aldaba','aldea','alegoría','aleluya','alemán','alergia','aleta','alevosía''alfabético''alfabeto','alfiler','alfombra','alguacil','aliciente','alijo ','almazara','almeja','almendra','alquitrán','altimetría','alzar ','amable ','amado ','amar ','ámbito ','americano','amigo','amnesia','amor','ampolla','añejo','anillo','ánodo','añoranza','antagónico','antepenúltima','antipático','aorta','aparato ','apelación ','apostatar ','aprehensivo','aprovisionamiento','aptitud ','aquilino','arce','archiduque','ardid ','armazón','aroma ','arquero ','arquetipo ','arquitecto','arreglar ','arteria ','artesano ','artificial','artimaña ','artista ','ascensión','asepsia ','asertivo','asesoría','aseverar','asilvestrado','asonante','atajo','atento','aterrizaje','atolladero','atómico','atuendo','bacalao','bacteria','báculo','badén','bajorrelieve','bala','balancín','balbucear','balcón','balonazo','balsa','báltico','bamba','banalidad','banana','banderilla','barbarie','barniz','Barranquilla','bastante','bastón','bastoncillo','batacazo','batidora','baúl','bautizado','becerro','begonia','bendita','beneplácito','benévolo','bengala','berrinche','berro','berza','besar','besugo','bético','betún','bibliófilo','bicéfala','bien','bienaventurado','bienvenido','bifurcación','bigote','bisagra','bisutería','bizantinismo','blanco','blasón','boca','boceto','boletín','bólido','bolígrafo','bomba','bonito','bonsái','bonzo','boquiabierto','borborigmo','borceguí','boricua','bosque','bostezar','botella','boya','boyante','brazalete','brebaje','brecha','brécol','bribón','brillantina','brinco','brisa','bromeliáceo','bronquio','bruto','buganvilla','buitre','bulto','buñuelo','burbuja','butaca','caballeresco','caballete','cabrahígo','cabuyería','cadavérico','caducidad','caducifolio','cafeína','cafetería','calabaza','calcañuelo','cálculo','calidez','caligrafía','calmado','cambio','camilla','caminar','cancionero','candela','canica','canjear','caparazón','capicúa','carambola','caramelo','carbón','caricatura','cariño','carnívoro','carpintero','carrete','cartera','cartílago','cartografía','carúncula','cascarrabias','casuística','catalizador','catástrofe','catatumbas','catedrático','cáustico','celestinesco','cenicienta','centímetro','centralización','certidumbre','cervicales','chaleco','chamuscar','chamusquina','chancleta','chándal','chaquetón','charlatán','chiflón','chigüín','Chihuahua','chilindrón','chiringuito','chivata','chivato','chocolatería','chorizo','chorrear','chungo','churro','cicatrizar','ciempiés','científico','ciervo','cimbrar','cimentar','cinematografía','cinturón','circulación','circunscribir','cítrico','citrícola','claridad','clásico','clerecía','clonación','coartada','cobertizo','cognitivo','colección','coliflor','común','concha','concreto','congestión','conjugar','conocer','conspirar','constipado','convertir','coordinador','coquetear','coraje','corrección','costa','cráter','creer','cripta','cristalería','cruzada','cuaderno','cuchara','cuchilla','cuentacuentos','cuento','cuerda','cuidar','culpabilidad','cultivar','cumplimentar','cúspide','dactiloscopia','dado','deber','debutar','deleznarse','demostración','departamento','deporte','derecho','desarrollo','desatornillador','desbarajuste','desbordamiento','descalcificación','descentralización','descompresión','desconsuelo','descripción','descubrimiento','desemballestar','desencajado','desgarro','deshidratación','deshilar','deshonra','deshuesar','deslizamiento','desmayarse','desnutrición','despacio','despegue','despejar','despertador','desplomarse','destino','destornillador','desvencijado','detalle','devolver','diabético','diablo','diabólico','diacrítico','dibujo','dictador','diente','difuminado','digresión','dinámico','director','disculpa','discusión','disfrutar','disparatado','disquisición','distinto','divergir','dobladillo','dorado','droguería','edredón','efectividad','égloga','egoísmo','ejecutar','ejecutivo','ejemplificación','ejercitar','elección','electorado','electrocardiograma','elegía','elegibilidad','elevalunas','embalsamar','embarazoso','embelesado','embotellado','embrague','embravecer','empampirolado','empañado','empeño','enajenamiento','encanto','encauzar','encéfalo','enchufar','enclaustrado','enclenque','encontrar','energético','enfurruñarse','engendrar','enjabonar','enladrillado','enmohecerse','enredar','ensalada','entender','entereza','entomólogo','entrada','entrenar','entrevista','epistaxis','equilibrista','equinoccio','ermitaño','errar','esbeltez','escabeche','escafoides','escama','escamochar','escápula','escayola','escenificación','escepticismo','escéptico','escisión','esclarecer','escoba','escribir','escuadrón','escudriñar','escuela','esdrújula','esencia','esfuerzo','esgrimir','eslavo','espalda','esperanza','esperpento','espinilla','esquizofrénico','estampado','estancia','estero','estilográfica','estimar','estómago','estrafalario','estrangular','estratagema','estreno','estribillo','estupefaciente','éter','ética','eufemismo','exabrupto','exageración','examinar','exasperante','exhalación','exhortación','éxodo','exordio','experimento','explayarse','exposición','expósito','expropiación','extasiado','extendido','exterior','exteriorizar','extracción','extracomunitario','extrínseco','fácil','facsímile','factótum','faja','falange','falda','falúa','familia','fantasía','faringitis','fascículo','fatal','fe','fémur','festival','fiambre','figura','filantropía','filantrópico','filarmónica','filatélico','filigrana','filípica','filipino','filistrín','filmoteca','filología','filosófico','fingir','fisura','fitopatología','flaco','flecha','forja','fortuito','forzar','fosforescente','fosilización','fotosíntesis','fuerza','fundir','futuro','futurólogo','gabardina','galardón','galaxia','gallina','gamuza','ganador','ganar','garabato','garrafa','gasterópodo','gaznápiro','gelatinoso','genealógico','género','geometría','geranio','geriatría','gimnasia','gleba','gliptografía','glomérulo','gloria','glotis','grabadora','grafólogo','grande','grueso','guachimán','guanábana','guarnición','Guatemala','guatemalteco','guinda','guirnalda','gusano','haba','habón','halterofilia','haraganería','harinado','hartar','haya','hebdómada','hebilla','hebraísta','hecatombe','hechiceresco','hechicero','hegemónico','helenización','helicóptero','hemistiquio','hepático','herético','hermético','hermosura','heroicidad','heteróclito','hexagonal','hialino','hibernación','híbrido','hilvanar','hincapié','hipérbaton','hispanohablante','historia','histrionismo','hito','hocico','hojaldre','homeopatía','homeostasis','honoríficamente','horchata','huelguista','húmedo','huracán','hurón','hurtadillas','husillero','icástico','iconoclasta','iconografía','idiosincrasia','ignición','igual','igualitarismo','iluminación','ilustrativo','imberbe','impaciencia','impepinable','importar','impreciso','imprevisible','impromptu','incandescente','incognoscible','incomprensivo','inconveniente','incorporación','incrustación','incursión','indicación','indómito','inductivo','inexorable','infeccioso','informar','inhábil','inhalador','ininteligible','ininterrumpidamente','injuria','inmaculado','inmunización','inmutable','inocuo','inquietante','inquilino','insalubre','inscripción','insectívoro','inserción','inserto','insidia','insigne','inspiración','instituto','intelectual','inteligente','interacción','intérprete','intervalo','intoxicado','intransigente','intrépido','introducción','introspección','intrusismo','inundación','inútil','investigación','invitación','invocación','inyección','ironía','irritación','istmo','itinerario','jabalí','jabato','jabonera','jácena','jactancioso ','jaculatoria','jalapeño','jarabe','jauría','jefatura','jergón','jirafa','jocosidad','jolgorio','jorobado','joven','juanete','jubón','juerguista','jugar','jurisprudencia','justificación','kilovatio','karate','kilo','kilogramo','koala','labiérnago','labriego','lácteo','laicización','laico','laísmo','lámina','languidecer','laosiano','laparoscopia','lapislázuli','largometraje','larguirucho','latido','lavavajillas','legañoso','legión','leguleyo','leotardos','leviatán','léxico','libertinaje','libidinoso','librería','limitación','lingüística','llanta','llanura','llave','locutorio','lúgubre','lugués','lumbago','luna','lusitano','luxación','macarrónico','machacón','machihembrar','madre','magnesio','malabarista','mañana','mandíbula','manejable','mapamundi','maravedinada','marcapasos','marchitar','marinero','mariposa','mausoleo','mecanismo','medievalismo','megalómano','mejorar','meñique','menospreciable','mentiroso','mesozoico','metalúrgico','metástasis','método','microscópico','misántropo','misión','modificación','mofarse','monógamo','monolingüe','monoteísmo','mortandad','mortero','movedizo','mover','mozárabe','muchedumbre','mucho','mucolítico','mudez','muérdago','muestrario','mullido','mundial','muñeca','murciélago','musaraña','museología','música','naranja','narcisismo','náufrago','náutica','navajero','náyade','necesario','néctar','Nefertiti','negligencia','nematelminto','neodarwinismo','neoexpresionism','neón','nerítico','nescientemente','neurastenia','nevera','nido','niebla','nimiedad','ningunear','niño','níquel','nitrógeno','nivelar','noche','nódulo','nómada','nombre','nomenclátor','nómina','normativa','nostálgico','novedoso','noviembre','novillada','nube','nudo','nuevo','nuez','número','oasis','oaxaqueño','obcecado','obduración','obedecer','obelisco','oblicuo','obliteración','obrero','obstruir','obtuso','occidentalizar','oceanografía','ocelote','octogenario','oculto','odeón','odioso','odontoide','oficio','ofuscar','oír','oligoelemento','omnívoro','oneroso','opinión','opresión','oráculo','orangután','órdago','ordinariez','orégano','orfandad','organigrama','organización','organogénesis','orgullo','orgulloso','orientativo','ornamentación','ornamento','orobanca','oropéndola','orzuelo','osteíctios','otear','otitis','otomán','ovalado','ovíparo','oxigenación','padre','pagar','página','palaciego','paleontología','palique','palmarés','palmípedo','paloduz','paloma','panadería','panadero','pánico','panóptico','pantalla','pañuelo','paquete','paracetamol','paráfrasis','paragüero','paraíso','paralelogramo','páramo','parangón','pararrayos','paredón','parénquima','parnasianismo','parótida','párpado','parquímetro','pársec','parsimonia','partenogénesis','partido','párvulo','pasador','pasajero','pasamontañas','pasantía','pasión','pastel','pasterización','patológico','patriótico','pectiniforme','pegajoso','peldaño','pelotazo','peonza','peor','pequinés','perdiz','perdonar','pérgola','perífrasis','peripecia','periplo','periquete','perlé','permeable','permisividad','permiso','pernicioso','pescador','pescozada','pestaña','pestilencia','petróleo','pez','picante','pictografía','pieza','pigmento','pimentón','pirata','piscolabis','placaje','placentero','plantígrado','plástico','plaza','pluma','plusvalía','poeta','políglota','polimetría','politécnico','político','pómulo','ponceño','portalámparas','poseer','práctica','pragmático','preeminencia','preestablecido','pregunta','premio','presente','pretérito','prevaricación','primero','principalmente','prismático','probable','problema','prolífico','pronombre','pronto','proporción','propósito','prospección','protagonista','provocador','proyecto','psicodélico','puchero','pueblerino','puerta','púlpito','pulsera','quebrado','querella','querer','quiebro','quinceañera','ración','ráfaga','raglán','rallador','rapidez','rápido','ratón','razón','real','rebeldía','recado','receptáculo','recibimiento','reciclado','reciente','recital','recompensa','reconstituyente','recreativo','redacción','redecilla','reembolso','reflejo','refrán','refresco','regadío','reivindicación','reivindicativo','reja','relación','reminiscencia','remordimiento','renacuajo','renovación','repelente','reservado','respeto','respuesta','resuelto','retórico','retransmitir','reverberación','revés','revista','revoltijo','reyes','rezongar','ribazo','ribonucleico','rifa','rígido','rimbombante','rinoplastia','riqueza','rizo','robot','rodapié','rodillera','romería','rondalla','ronquido','ropaje','rozadura','rúbrica','ruido','ruina','rústico','sabandija','saber ','sacacorchos ','sajo','salazón','salida','salpicar','salsera','samurái','sancta','sanctórum','sandez','sanguijuela','sarampión','sarpullido','sartén','satén','sátrapa','secano','secesión','secreto','seguro','selva','señor','septuagenario','serie','servidor','sextilla','Siberia','sierra','silogismo','simpático','sincronización','síntesis','sobrino','socio','socorrista','sofisticado','sol','soldado','solidaridad','sólido','solución','solvencia','somnoliento','sonámbulo','sonoro','sonrisa','soporífero','sorbete','soslayo','sótano','subálveo','subir','sublevación','subsahariano','subterráneo','suburbio','succión','sucesión','sueño','suizo','sulfhídrico','sultán','superstición','susceptible','suscripción','tábano','taburete','tacatá','tácito','tacón','Tahití','tailandés','tángana','tango','tapete','taquillón','tarambana','tarántula','tardío','tatuaje','taxista','tazón','tebeo','técnico','tejado','telégrafo','telepatía','temperatura','tentáculo','teogónico','teología','teoría','teotihuacano','tercero','tergiversación','termómetro','territorio','terrón','tesis','tesón','testificar','tetera','timón','tipografía','tiquismiquis','titán','titulación','titularización','título','topónimo','toquilla','tornado','tornillo','torrefacto','trabajo','trabalenguas','traducción','tráfago','tráfico','tragaluz','tráiler','traje','transacción','transferencia','transgénico','trapezoide','trascendental','trasluz','traspiés','trayectoria','trazo','tremendo','tríada','triquiñuela','triunfo','triunvirato','trocánter','trompo','trotskismo','turco','ubérrimo','ucraniano','ugandés','úlcera','último','umbrío','ungüento','unguiculado','único','uniforme','unigénito','urgente','Uruguay','uruguayo','usurpar','útero','útil','utopía','uva','vacacional','vaciado','vacilar','vaina','vallado','valle','vanagloriarse','vapor','varicela','varón','vectorial','vehemencia','veleidad','veleidoso','velocípedo','vencejo','Venecia','venenoso','Venezuela','venganza','ventrílocuo','Veracruz','verano','verborrea','vergüenza','verídico','verosimilitud','verso','vertebrado','vértigo','víbora','vihuela','violín','visera','visigótico','visión','visionario','viudo','vivaracho','víveres','vívido','vivienda','vivir','vociferar','volver','voz','vozarrón','yámbico','yáquil','yegua','yermo','yunque','zábila','zabordar','zacateca','zafarrancho','zafio','zaherir','zalamería','zalamero','zambomba','zanahoria','zancadilla','zanjar','zarigüeya','zarina','zarpa','zarzamora','zoantropía','zombi','zoología','zueco','zulo','zumbar','zumbido','zurcido','zurriagazo']
word = StringVar()
root = Tk()
# This is the section of code which creates the main window
root.geometry('550x300')
root.configure(background='#F0F8FF')
root.title('Spanish Spelling Bee')

# this is the function called when the button is clicked
def btnClickFunctionAdv():
    word.set(str(random.choice(AdvancedVocab)))


# this is the function called when the button is clicked
def btnClickFunctionBasic():
    word.set(str(random.choice(BasicVocab)))


# This is the section of code which creates a button
Button(root, text='Basic Vocab', bg='#FFFFFF', font=('arial', 20, 'normal'), command=btnClickFunctionBasic).place(x=25, y=62)

# This is the section of code which creates a button
Button(root, text='Adv Vocab', bg='#FFFFFF', font=('arial', 20, 'normal'), command=btnClickFunctionAdv).place(x=350, y=62)

# This is the section of code which creates the a label
Label(root, text=word, bg='#F0F8FF', font=('arial', 40, 'normal')).place(x=190, y=170)

root.mainloop()