from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .models import *
from django import forms
from .resources import ProductResource

class AprovisionamientoResource(resources.ModelResource):
    class Meta:
        model = Aprovisionamiento
        fields = ('id', 'usuario', 'cedula', 'nombre', 'celula', 'lider')

    def before_import_row(self, row, **kwargs):
        row['usuario'] = row.pop('Usuario', None)
        row['cedula'] = row.pop('Cedula', None)
        row['nombre'] = row.pop('Nombre', None)
        row['celula'] = row.pop('Celula', None)
        row['lider'] = row.pop('Lider', None)

@admin.register(Aprovisionamiento)
class AprovisionamientoAdmin(ImportExportModelAdmin):
    resource_class = AprovisionamientoResource


class BacklogResource(resources.ModelResource):
    class Meta:
        model = Backlog
        fields = (
            'IdAprovisionamiento', 'ViabilidadOrigen', 'TipoOperacionPlan', 'CategoríaSM', 'Estado', 
            'IdServicio', 'GrupoAsignado', 'Mes', 'FechaCreación', 'ANS', 'TiempoOperacion', 
            'TiempoCliente', 'TiempoComercial', 'TiempoETB', 'TiempoTercero', 'TiempoTotal', 
            'TiempoReal', 'CumploONoCumple', 'FaseActual', 'NombreProducto', 'TipoSolicitud', 
            'CausalRetiro', 'AnchoBanda', 'MedioUltimaMilla', 'CuentaCliente', 'NIT', 
            'ProveedorUltimaMilla', 'Asignadoa', 'Modificadopor', 'DireccionPrincipal', 
            'SucursalInstalcion', 'CiudadInstalacion', 'FechaActulizacion', 'UltimaAnotacion', 
            'SegmentoResumen', 'UltimaTarea', 'AltasTramites', 'ValorRecurrente', 'DELTA', 
            'ONETIME', 'DELTAEQUIPOS', 'DELTAEQUIPOSLB', 'ProyeccionMeLB', 'FechaEntregaLB', 
            'EstadoLB', 'CODIGOTIPO', 'SUBCODIGOTIPO', 'GESTIONOGESTIO', 'ESTADOGENERAL', 
            'RESPONSABLE', 'ACCIONATOMAR', 'FechaPactadaCliente', 'FECHASEGUIMIENTOSTANDBY', 
            'ResponsableStandby', 'FechaEntregaCliente2', 'FechaFacturación', 'FechaFinalización', 'SemanaProyeccion', 
            'MasoMenos', 'plusminus', 'SemanaFact', 'Backlog', 'PrimerDíaMes', 'UltimoDíaMes', 
            'DíasFactura', 'ValorProrrateadoOperacion', 'TFacturacion', 'DíasFacturaIngresos', 
            'ValorProrrateadoIngresoMarzo', 'ValorProrrateadoIngresoAbril', 'TiempoMedioBolsa', 
            'ClasificaciónTipoCliente'
        )

    def before_import_row(self, row, **kwargs):
        row['IdAprovisionamiento'] = row.pop('Id Aprovisionamiento', None)
        row['ViabilidadOrigen'] = row.pop('Viabilidad Origen', None)
        row['TipoOperacionPlan'] = row.pop('Tipo Operacion Plan', None)
        row['CategoríaSM'] = row.pop('Categoría SM', None)
        row['Estado'] = row.pop('Estado', None)
        row['IdServicio'] = row.pop('Id Servicio', None)
        row['GrupoAsignado'] = row.pop('Grupo Asignado', None)
        row['Mes'] = row.pop('Mes', None)
        row['FechaCreación'] = row.pop('Fecha Creacion', None)
        row['ANS'] = row.pop('ANS', None)
        row['TiempoOperacion'] = row.pop('Tiempo Operacion', None)
        row['TiempoCliente'] = row.pop('Tiempo Cliente', None)
        row['TiempoComercial'] = row.pop('Tiempo Comercial', None)
        row['TiempoETB'] = row.pop('Tiempo ETB', None)
        row['TiempoTercero'] = row.pop('Tiempo Tercero', None)
        row['TiempoTotal'] = row.pop('Tiempo Total', None)
        row['TiempoReal'] = row.pop('Tiempo Real', None)
        row['CumploONoCumple'] = row.pop('Cumple / No Cumple', None)
        row['FaseActual'] = row.pop('Fase Actual', None)
        row['NombreProducto'] = row.pop('Nombre Producto', None)
        row['TipoSolicitud'] = row.pop('Tipo Solicitud', None)
        row['CausalRetiro'] = row.pop('Causal Retiro', None)
        row['AnchoBanda'] = row.pop('Ancho Banda', None)
        row['MedioUltimaMilla'] = row.pop('Medio Ultima Milla', None)
        row['CuentaCliente'] = row.pop('Cuenta Cliente', None)
        row['NIT'] = row.pop('NIT', None)
        row['ProveedorUltimaMilla'] = row.pop('Proveedor Ultima Milla', None)
        row['Asignadoa'] = row.pop('Asignado a', None)
        row['Modificadopor'] = row.pop('Modificado por', None)
        row['DireccionPrincipal'] = row.pop('Direccion Principal', None)
        row['SucursalInstalcion'] = row.pop('Sucursal Instalcion', None)
        row['CiudadInstalacion'] = row.pop('Ciudad Instalacion', None)
        row['FechaActulizacion'] = row.pop('Fecha Actulizacion', None)
        row['UltimaAnotacion'] = row.pop('Ultima Anotacion', None)
        row['SegmentoResumen'] = row.pop('Segmento Resumen', None)
        row['UltimaTarea'] = row.pop('Ultima Tarea', None)
        row['AltasTramites'] = row.pop('Altas Tramites', None)
        row['ValorRecurrente'] = row.pop('Valor Recurrente', None)
        row['DELTA'] = row.pop('DELTA', None)
        row['ONETIME'] = row.pop('ONE TIME', None)
        row['DELTAEQUIPOS'] = row.pop('DELTA + EQUIPOS', None)
        row['DELTAEQUIPOSLB'] = row.pop('DELTA EQUIPOS LB', None)
        row['ProyeccionMeLB'] = row.pop('Proyeccion Me LB', None)
        row['FechaEntregaLB'] = row.pop('Fecha Entrega LB', None)
        row['EstadoLB'] = row.pop('Estado LB', None)
        row['CODIGOTIPO'] = row.pop('CODIGO TIPO', None)
        row['SUBCODIGOTIPO'] = row.pop('SUB CODIGO TIPO', None)
        row['GESTIONOGESTIO'] = row.pop('GESTIO / NO GESTIO', None)
        row['ESTADOGENERAL'] = row.pop('ESTADO GENERAL', None)
        row['RESPONSABLE'] = row.pop('RESPONSABLE', None)
        row['ACCIONATOMAR'] = row.pop('ACCION A TOMAR', None)
        row['FechaPactadaCliente'] = row.pop('Fecha Pactada Cliente', None)
        row['FECHASEGUIMIENTOSTANDBY'] = row.pop('FECHA SEGUIMIENTO STANDBY', None)
        row['ResponsableStandby'] = row.pop('Responsable Standby', None)
        row['FechaEntregaCliente2'] = row.pop('Fecha Entrega Cliente2', None)
        row['FechaFacturación'] = row.pop('Fecha Facturacion', None)
        row['FechaFinalización'] = row.pop('Fecha Finalizacion', None)
        row['SemanaProyeccion'] = row.pop('Semana Proyeccion', None)
        row['MasoMenos'] = row.pop('+/-', None)
        row['plusminus'] = row.pop('plus minus', None)
        row['SemanaFact'] = row.pop('Semana Fact', None)
        row['Backlog'] = row.pop('Backlog', None)
        row['PrimerDíaMes'] = row.pop('Primer Día Mes', None)
        row['UltimoDíaMes'] = row.pop('Ultimo Día Mes', None)
        row['DíasFactura'] = row.pop('Días Factura', None)
        row['ValorProrrateadoOperacion'] = row.pop('Valor Prorrateado Operacion', None)
        row['TFacturacion'] = row.pop('T Facturacion', None)
        row['DíasFacturaIngresos'] = row.pop('Días Factura Ingresos', None)
        row['ValorProrrateadoIngresoMarzo'] = row.pop('Valor Prorrateado Ingreso Marzo', None)
        row['ValorProrrateadoIngresoAbril'] = row.pop('Valor Prorrateado Ingreso Abril', None)
        row['TiempoMedioBolsa'] = row.pop('Tiempo Medio Bolsa', None)


@admin.register(Backlog)
class BacklogAdmin(ImportExportModelAdmin):
    resource_class = BacklogResource
    


class AbiertasRetirosResource(resources.ModelResource):
    class meta:
        model = AbiertasRetiros
        fields = ('Id_Aprovisionamiento' 'Viabilidad_Origen' 'Asesor_Comercial' 'Tipo_Operacion_Plan' 'Categoría_SM' 'Estado' 'Id_Servicio' 'Grupo_Asignado' 'Mes' 'Fecha_Creación' 'Fecha_Esperada_06' 'Fecha_Inicio_Facturacion' 'ANS' 'Tiempo_Operacionv' 'Tiempo_Cliente' 'Tiempo_Comercial' 'Tiempo_ETB' 'Tiempo_Tercero' 'TTAbierto' 'Cumple_O_No_Cumple' 'Fase_Actual'
                'Nombre_Producto' 'Tipo_Solicitud' 'Causal_Retiro' 'Ancho_Banda' 'Medio_Ultima_Milla' 'Cuenta_Cliente' 'NIT' 'Proveedor_Ultima_Milla' 'Asignado_a' 'Modificado_por' 'Direccion_Principal' 'Sucursal_Instalcion' 'Ciudad_Instalacion' 'Ultima_Fecha_Anotacion' 'Ultima_Anotación_Resumen' 'Tipo_Suspensión' 'Segmento')

@admin.register(AbiertasRetiros)
class AbiertasRetirosAdmin(ImportExportModelAdmin):
    resource_class = AbiertasRetirosResource


class AbiertasResource(resources.ModelResource):
    class meta:
        model = Abiertas
        fields = ('Id_Aprovisionamiento' 'Viabilidad_Origen' 'Asesor_Comercial' 'Tipo_Operacion_Plan' 'Categoría_SM' 'Estado' 'Id_Servicio' 'Grupo_Asignado' 'Nombre_Mes' 'Fecha_Creación' 'ANS_Días' 'Tiempo_Operacion' 'Tiempo_Cliente' 'Tiempo_Comercial' 'Tiempo_ETB' 'Tiempo_Tercero' 'TTAbierto' 'Tiempo_Real' 'Cumple_O_No_Cumple' 'Fase_Actual' 'Nombre_Producto' 'Tipo_Solicitud'
                'Causal_Retiro' 'Ancho_Banda' 'Medio_Ultima_Milla' 'Cuenta_Cliente' 'NIT' 'Proveedor_Ultima_Milla' 'Asignado_a' 'Modificado_por' 'Direccion_Principal' 'Sucursal_Instalcion' 'Ciudad_Instalacion' 'Segmento' 'Fecha_Inicio_Contrato' 'Fecha_Fin_Contrato' 'Estado_Gestion_Oc' 'Fecha_Estimada_Entrega')

    def before_import_row(self, row, **kwargs):
        row['nombre_producto '] = row.pop('Nombre del Producto', None)
        
@admin.register(Abiertas)
class AbiertasAdmin(ImportExportModelAdmin):
    resource_class = AbiertasResource


class CerradasResource(resources.ModelResource):
    class meta:
        model = Cerradas
        fields = ('Id_Aprovisionamiento' 'Viabilidad_Origen' 'Asesor_Comercial' 'Tipo_Operacion_Plan' 'Categoría_SM' 'Estado' 'Id_Servicio' 'Grupo_Asignado' 'Nombre_Mes' 'Fecha_Creacion' 'ANS_Días' 'Tiempo_Operacion' 'Tiempo_Cliente' 'Tiempo_Comercial' 'Tiempo_ETB' 'Tiempo_Tercero' 'TTAbierto' 'Tiempo_Real' 'Cumple_O_No_Cumple' 'Fase_Actual' 'Nombre_Producto' 'Tipo_Solicitud' 'Causal_Retiro' 'Ancho_Banda'
                'Medio_Ultima_Milla' 'Cuenta_Cliente' 'NIT' 'Proveedor_Ultima_Milla' 'Asignado_a' 'Modificado_por' 'Direccion_Principal' 'Sucursal_Instalcion' 'Ciudad_Instalacion' 'Ultima_Fecha_Anotación' 'Ultima_Anotación_Resumen' 'Segmento' 'Fecha_Finalizacion' 'Causal_Finalizacion' 'Observaciones_Finalizacion' 'Fecha_Inicio_Contrato' 'Fecha_Fin_Contrato') 



@admin.register(Cerradas)
class CerradasAdmin(ImportExportModelAdmin):
    resource_class = CerradasResource


class FacturacionResource(resources.ModelResource):
    class meta:
        model = Facturacion
        fields = ('id_Aprovisionamiento' 'Viabilidad_Origen' 'Asesor_Comercial' 'Tipo_Operacion_Plan' 'Categoría_SM' 'Estado' 'Id_Servicio' 'Grupo_Asignado' 'Nombre_Mes' 'Fecha_Creacion' 'ANS_dias' 'Tiempo_Operacion' 'Tiempo_Cliente' 'Tiempo_Comercial' 'Tiempo_ETB' 'Tiempo_Tercero' 'TTAbierto' 'Tiempo_Real' 'Cumple_O_No_Cumple' 'Fase_Actual'
                'Nombre_Producto' 'Tipo_Solicitud' 'Causal_Retiro' 'Ancho_Banda' 'Medio_Ultima_Milla' 'Cuenta_Cliente' 'NIT' 'Proveedor_Ultima_Milla' 'Asignado_a' 'Modificado_por' 'Direccion_Principal' 'Sucursal_Instalcion' 'Ciudad_Instalacion' 'Adicional' 'Ultima_Actualizacion' 'Segmento' 'Fecha_Entrega_Cliente' 'Fecha_Inicio_Contrato'
                'Fecha_Facturacion' 'Fecha_Fin_Contrato')
        
@admin.register(Facturacion)
class FacturacionAdmin(ImportExportModelAdmin):
    resource_class = FacturacionResource


