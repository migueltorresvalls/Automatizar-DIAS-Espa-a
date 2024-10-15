import google.generativeai as genai 
import os

# Clase que se utiliza para realizar consultas a la IA

class Gemini:
    def __init__(self):
        # Hay que crearse una cuenta en Gemini Google y crearse una clave (https://ai.google.dev/gemini-api/docs/api-key?hl=es-419). A continuación, se añade la clave como variable de entorno bajo el nombre GEMINI_API_KEY.
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def lanzar_consulta(self, pdf):
        consulta = """
        Quiero que extraigas la siguiente información del pdf: tipo de resolución, nombre proyecto, tecnología, hibridación, tamaño, capacidad de acceso, SPV, sociedad, ubicacion, resultado, motivacion

        La fecha de publicación la quiero en formato dd/mm/aa

        El tipo de resolución puede ser: Solicitud de Autorización Administrativa Previa (AAP) / Autorización Administrativa de Construcción (AAC) / Evaluación de Impacto Ambiental (a la cual nos referimos como Declaración de Impacto Ambiental o DIA). Quiero que me contestes con DIA, AAP, AAC. Puede que sean AAC y AAP juntas, en cuyo caso contestame con ACC/APP. Si no lo encuentras, dejalo vacío. 

        Para el campo hibridación, determina se mezclan tecnologías diferentes en el proyecto. Por ejemplo, si se quiere añadir una planta fotovoltaica a una instalación eólica. Si hibrida de un proyecto, contesta con un SI, si no lo hace, contesta con un NO. 

        La tecnología del proyecto puede ser: fotovoltaica (FV), eólica (EO) o baterías (BESS). Solo contestame con uno de esos valores. Si no encuentras, dejalo vacío, NO pongas un 0. 

        El tamaño es la potencia nominal instalada en el proyecto en MWn. Si no encuentras el tamaño, pon un 0. 

        La capacidad es la capacidad de la subestación a la que se conecta en MW. Si no encuentras la capacidad, pon un 0.

        La SPV es la Special-purpose entity que firma el proyecto. Si no lo encuentras, dejalo vacío. 

        Para la sociedad, en base al contexto, intenta adivinar a que empresa pertenece. Si no aparece en el pdf, intenta buscando en periódicos u otras páginas web. Si no lo encuentras, dejalo vacío. 

        Para la ubicación, lo más importante es saber las coordenadas UTM, separadas por ;. Si no encuentras las coordenadas, busca el polígono o parcela. Si no apareciese, busca el término municial. Si no apareciese busca la provincia. Quiero que me respondas solo con un campo: coordenadas, polígono, parcela, término municipal o provinincia (siguiendo ese órden de prioridad). Por ejemplo, si has encontrado las coordenadas UTM y la provincia, solo quiero las coordenadas porque tienen mayor prioridad. Antes de cada valor, indicame si se trata de coordenadas (Co), polígono (Po), parcela (Pa), termino municipal (M) o provincia (P). El esquema para la ubicación sigue el siguiente ejemplo. ubicacion:C:41.33;34.99 si se trata de coordenada. ubicacion:P:Toledo, si se trata de provincia, y así sucesivamente. Si no encuentras ninguno, dejalo vacío. 

        Para el resultado, quiero saber si el resultado de la resolución ha sido favorable o desfavorable. Solo quiero uno de esos dos valores. Si no lo encuentras, dejalo vacío. 

        Para el campo motivos y solo si el resultado ha sido desfavorable, quiero saber cuales han sido los motivos. Si el resultado ha sido favorable, dejalo en blanco.  

        Quiero que tu respuesta siga la estructura de un csv separado por ':', donde el valor pedido es el primer elemento y el valor obtenido el segundo. Por ejemplo: tecnologia:FV. No quiero que haya un : despues de FV
                
        Puedes encontrar la información sobre el pdf a continuación: 

        """
        respuesta = self.model.generate_content(consulta + pdf)
        return respuesta.text