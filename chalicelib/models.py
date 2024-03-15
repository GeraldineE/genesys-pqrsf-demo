import typing
import pydantic


class PQRSF(pydantic.BaseModel):
	segmento: str
	descripcion: str
	solucion: typing.Optional[str] = None
	tipo_usuario: typing.Literal['Cliente', 'Marcas Aliadas', 'Otro']
	otro_usuario: typing.Optional[str] = None
	tipo_canal: typing.Literal[
		'Redes Sociales',
		'Llamada',
		'Correo',
		'Asesor comercial',
		'Página web',
		'WhatsApp',
		'Almacén',
		'Chatbot',
		'App',
		'Oficina de Sistecrédito',
		'Otro',
	]
	otro_canal: typing.Optional[str] = None
	tipo_producto: typing.Literal[
		'Sistecrédito',
		'SistePagos',
		'SistePay',
		'LuegoPago',
		'Sistetiendas',
		'Sistepass',
	]
	tipo_documento: typing.Literal['NIT', 'Cédula de ciudadanía', 'Cédula extranjería', 'PEP']
	numero_documento: str
	nombre_completo: str
	nombre_razon_social: str
	correo_electronico: pydantic.EmailStr
	numero_celular: str
	nombre_almacen: str
	departamento: str
	ciudad: str
	motivo: typing.Literal['No hay motivo']
	criticidad: typing.Literal['Alta', 'Media', 'Baja']
	raised_by: pydantic.EmailStr
	tipo_pqrsf: typing.Literal['Petición', 'Queja', 'Reclamo', 'Sugerencia', 'Felicitación']
	procedencia: str
	proceso_interno: typing.Literal[
		'Gestión Aliados', 'Gestión Legal', 'Soporte Clientes', 'Cliente Final'
	]
	agente_involucrado: typing.Optional[str] = None
	aliado_involucrado: typing.Optional[str] = None
	experiencia: typing.Optional[typing.Literal[1, 2, 3, 4, 5]] = None
