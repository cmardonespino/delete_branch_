# Eliminar branch inactiva
El siguiente proyecto escrito en python 3+ se desarrolla para cubrir la necesidad de borrar de manera automatizada las branch inactivas durante un periodo de tiempo X.
# Requerimientos
* Generar un access token desde nuestras cuentas Github
* Tener instaladas las siguientes dependencias:
	* `requests`
	* `pygithub`


#HOWTO
Modificar las los parametros de la fuenta [variables.py](src/variables.py) de acuerdo a los datos del repositorio
Desde la shell ubicada en la raiz del proyecto, ejecutar el siguiente comando:
* `python delete_branch.py`

Las dependencias mencionadas fueron instaladas con el administrador de paquetes pip.