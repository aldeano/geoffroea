# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'controles_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=55)),
        ))
        db.send_create_signal(u'controles', ['Usuario'])

        # Adding M2M table for field groups on 'Usuario'
        m2m_table_name = db.shorten_name(u'controles_usuario_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'controles.usuario'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Usuario'
        m2m_table_name = db.shorten_name(u'controles_usuario_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'controles.usuario'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'permission_id'])

        # Adding model 'ControlesFronterizos'
        db.create_table(u'controles_controlesfronterizos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=8)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=8)),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('horario_inicio', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('horario_termino', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('comuna', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'controles', ['ControlesFronterizos'])

        # Adding M2M table for field inspectores on 'ControlesFronterizos'
        m2m_table_name = db.shorten_name(u'controles_controlesfronterizos_inspectores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('controlesfronterizos', models.ForeignKey(orm[u'controles.controlesfronterizos'], null=False)),
            ('usuario', models.ForeignKey(orm[u'controles.usuario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['controlesfronterizos_id', 'usuario_id'])

        # Adding model 'Dia_CCFF_Terrestre'
        db.create_table(u'controles_dia_ccff_terrestre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('inspector', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['controles.Usuario'], unique=True)),
            ('hombres_ingresados', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres_inspeccionados', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_ingresadas', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_inspeccionadas', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_si_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_no_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('n_declaran', self.gf('django.db.models.fields.IntegerField')()),
            ('n_adc', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('control_fronterizo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.ControlesFronterizos'])),
            ('bicicletas_ingresadas', self.gf('django.db.models.fields.IntegerField')()),
            ('bicicletas_inspeccionadas', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_part_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_part_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('moto_ingresada', self.gf('django.db.models.fields.IntegerField')()),
            ('moto_inspeccionada', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('tren_pas_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('tren_pas_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_dipl_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_dipl_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_hum_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('vehiculo_hum_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_atingente_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_atingente_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_no_atingente_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_no_atingente_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('tren_carga_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('tren_carga_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_ffaa_at_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_ffaa_at_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_ffaa_no_at_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('camion_ffaa_no_at_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('auto_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('auto_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('bus_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'controles', ['Dia_CCFF_Terrestre'])

        # Adding model 'Prod_Regulado'
        db.create_table(u'controles_prod_regulado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('kilogramos', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('pais_origen', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('medida_adoptada', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('numero_muestra', self.gf('django.db.models.fields.IntegerField')()),
            ('unidad_muestra', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'controles', ['Prod_Regulado'])

        # Adding model 'Desembarco_Barco'
        db.create_table(u'controles_desembarco_barco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'controles', ['Desembarco_Barco'])

        # Adding model 'Acta_Recepcion'
        db.create_table(u'controles_acta_recepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('puerto_inspeccion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nombre_nave', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('agencia', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_anterior', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_siguiente', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('arribo', self.gf('django.db.models.fields.DateTimeField')()),
            ('recepcion', self.gf('django.db.models.fields.DateTimeField')()),
            ('zarpe', self.gf('django.db.models.fields.DateTimeField')()),
            ('mujeres_desembarcan', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres_desembarcan', self.gf('django.db.models.fields.IntegerField')()),
            ('desembarcos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Desembarco_Barco'])),
            ('numero_sellos', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion_sellos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sitio_atraque', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_c_limantria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('solicitan_antecedentes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('basuras_tapadas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('basuras_fijas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('basuras_hermeticas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deficiencia_corregida', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('area_no_inspeccionada', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('animal_a_bordo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo_animal', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('numero_animal', self.gf('django.db.models.fields.IntegerField')()),
            ('pasajeros_ingresan', self.gf('django.db.models.fields.IntegerField')()),
            ('descensos', self.gf('django.db.models.fields.IntegerField')()),
            ('revision_listado_puertos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('periodo_revision', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cert_fitosanitario', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Acta_Recepcion'])

        # Adding M2M table for field productos_regulados on 'Acta_Recepcion'
        m2m_table_name = db.shorten_name(u'controles_acta_recepcion_productos_regulados')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acta_recepcion', models.ForeignKey(orm[u'controles.acta_recepcion'], null=False)),
            ('prod_regulado', models.ForeignKey(orm[u'controles.prod_regulado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['acta_recepcion_id', 'prod_regulado_id'])

        # Adding model 'Acta_PostRecepcion'
        db.create_table(u'controles_acta_postrecepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('puerto_inspeccion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nombre_nave', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('agencia', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_anterior', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_siguiente', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('arribo', self.gf('django.db.models.fields.DateTimeField')()),
            ('recepcion', self.gf('django.db.models.fields.DateTimeField')()),
            ('zarpe', self.gf('django.db.models.fields.DateTimeField')()),
            ('mujeres_desembarcan', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres_desembarcan', self.gf('django.db.models.fields.IntegerField')()),
            ('desembarcos', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Desembarco_Barco'])),
            ('numero_sellos', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion_sellos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sitio_atraque', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('puerto_c_limantria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('solicitan_antecedentes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('basuras_tapadas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('basuras_fijas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('basuras_hermeticas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('deficiencia_corregida', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('area_no_inspeccionada', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('animal_a_bordo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tipo_animal', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('numero_animal', self.gf('django.db.models.fields.IntegerField')()),
            ('monitoreo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prod_sellados_recepcion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mantiene_sellos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sellos_rotos', self.gf('django.db.models.fields.TextField')()),
            ('desembarco_basuras', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transbordo_basuras', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('supervision_sag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('motivo_adc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'controles', ['Acta_PostRecepcion'])

        # Adding M2M table for field productos_regulados on 'Acta_PostRecepcion'
        m2m_table_name = db.shorten_name(u'controles_acta_postrecepcion_productos_regulados')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acta_postrecepcion', models.ForeignKey(orm[u'controles.acta_postrecepcion'], null=False)),
            ('prod_regulado', models.ForeignKey(orm[u'controles.prod_regulado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['acta_postrecepcion_id', 'prod_regulado_id'])

        # Adding model 'Dia_CCFF_Maritimo'
        db.create_table(u'controles_dia_ccff_maritimo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('inspector', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['controles.Usuario'], unique=True)),
            ('hombres_ingresados', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres_inspeccionados', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_ingresadas', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_inspeccionadas', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_si_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_no_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('n_declaran', self.gf('django.db.models.fields.IntegerField')()),
            ('n_adc', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('control_fronterizo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.ControlesFronterizos'])),
            ('crucero_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('crucero_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('mercante_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('mercante_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('contenedor_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('contenedor_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('cisterna_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('cisterna_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('tanque_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('tanque_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('instruccion_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('instruccion_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('guerra_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('guerra_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('pas_carga_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('pas_carga_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('aviso_recalada_inicio', self.gf('django.db.models.fields.IntegerField')()),
            ('aviso_recalada_termino', self.gf('django.db.models.fields.IntegerField')()),
            ('acta_recepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Recepcion'])),
            ('post_recepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_PostRecepcion'])),
        ))
        db.send_create_signal(u'controles', ['Dia_CCFF_Maritimo'])

        # Adding model 'Acta_Inspeccion'
        db.create_table(u'controles_acta_inspeccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('compania_aerea', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('vuelo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('origen', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('hora_estimada', self.gf('django.db.models.fields.TimeField')()),
            ('tipo_vuelo', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('nombre_aeropuerto', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'controles', ['Acta_Inspeccion'])

        # Adding model 'Sol_Inspeccion'
        db.create_table(u'controles_sol_inspeccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('compania_aerea', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('vuelo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('origen', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ruta', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('hora_estimada', self.gf('django.db.models.fields.TimeField')()),
            ('tipo_vuelo', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('escala_uno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('escala_dos', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'controles', ['Sol_Inspeccion'])

        # Adding model 'Dia_CCFF_Aereo'
        db.create_table(u'controles_dia_ccff_aereo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('inspector', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['controles.Usuario'], unique=True)),
            ('hombres_ingresados', self.gf('django.db.models.fields.IntegerField')()),
            ('hombres_inspeccionados', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_ingresadas', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres_inspeccionadas', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_si_si_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('declaran_no_no_traen', self.gf('django.db.models.fields.IntegerField')()),
            ('n_declaran', self.gf('django.db.models.fields.IntegerField')()),
            ('n_adc', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_entrada_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_flora', self.gf('django.db.models.fields.IntegerField')()),
            ('cites_salida_fauna', self.gf('django.db.models.fields.IntegerField')()),
            ('control_fronterizo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.ControlesFronterizos'])),
            ('avioneta_ingresada', self.gf('django.db.models.fields.IntegerField')()),
            ('avioneta_inspeccionada', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('heli_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('heli_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_carga_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_carga_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_carga_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_carga_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_pas_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('avion_pas_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('avioneta_ffaa_ingresada', self.gf('django.db.models.fields.IntegerField')()),
            ('avioneta_ffaa_inspeccionada', self.gf('django.db.models.fields.IntegerField')()),
            ('heli_ffaa_ingresado', self.gf('django.db.models.fields.IntegerField')()),
            ('heli_ffaa_inspeccionado', self.gf('django.db.models.fields.IntegerField')()),
            ('solicitud_inspeccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Sol_Inspeccion'])),
            ('acta_inspeccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Inspeccion'])),
        ))
        db.send_create_signal(u'controles', ['Dia_CCFF_Aereo'])

        # Adding model 'Pasajero'
        db.create_table(u'controles_pasajero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('inspector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Usuario'])),
            ('tipo_doc', self.gf('django.db.models.fields.CharField')(max_length=19)),
            ('n_doc', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nombres_apellidos', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('declara', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('proceso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pais_origen', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=28)),
            ('ultimo_puerto', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('prox_puerto', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'controles', ['Pasajero'])

        # Adding model 'Prod_Interceptable'
        db.create_table(u'controles_prod_interceptable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('subtipo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'controles', ['Prod_Interceptable'])

        # Adding model 'Record_Intercepcion'
        db.create_table(u'controles_record_intercepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kilos', self.gf('django.db.models.fields.FloatField')()),
            ('folio_protocolo', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'controles', ['Record_Intercepcion'])

        # Adding model 'Intercepcion'
        db.create_table(u'controles_intercepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('kilos', self.gf('django.db.models.fields.FloatField')()),
            ('rip', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['controles.Record_Intercepcion'], unique=True)),
            ('medida_int', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('comentario_int', self.gf('django.db.models.fields.TextField')()),
            ('pasajero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Pasajero'])),
        ))
        db.send_create_signal(u'controles', ['Intercepcion'])

        # Adding M2M table for field intercepcion on 'Intercepcion'
        m2m_table_name = db.shorten_name(u'controles_intercepcion_intercepcion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intercepcion', models.ForeignKey(orm[u'controles.intercepcion'], null=False)),
            ('prod_interceptable', models.ForeignKey(orm[u'controles.prod_interceptable'], null=False))
        ))
        db.create_unique(m2m_table_name, ['intercepcion_id', 'prod_interceptable_id'])

        # Adding model 'Abandono'
        db.create_table(u'controles_abandono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('kilos', self.gf('django.db.models.fields.FloatField')()),
            ('rip', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['controles.Record_Intercepcion'], unique=True)),
            ('medida_int', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('comentario_int', self.gf('django.db.models.fields.TextField')()),
            ('dia', self.gf('django.db.models.fields.DateField')()),
            ('inspector', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['controles.Usuario'])),
            ('probable_origen', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=28)),
        ))
        db.send_create_signal(u'controles', ['Abandono'])

        # Adding M2M table for field intercepcion on 'Abandono'
        m2m_table_name = db.shorten_name(u'controles_abandono_intercepcion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('abandono', models.ForeignKey(orm[u'controles.abandono'], null=False)),
            ('prod_interceptable', models.ForeignKey(orm[u'controles.prod_interceptable'], null=False))
        ))
        db.create_unique(m2m_table_name, ['abandono_id', 'prod_interceptable_id'])

        # Adding model 'Orden_Tratamiento'
        db.create_table(u'controles_orden_tratamiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'controles', ['Orden_Tratamiento'])

        # Adding model 'Cores'
        db.create_table(u'controles_cores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'controles', ['Cores'])

        # Adding model 'Turno'
        db.create_table(u'controles_turno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jefe_turno', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['controles.Usuario'])),
            ('sgte_jefe_turno', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['controles.Usuario'])),
            ('dia_entrega', self.gf('django.db.models.fields.DateTimeField')()),
            ('llenado_furi', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_llenado', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('deteccion_prod_no_conf', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_deteccion', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('intercepcion_ampliada', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_intercepcion', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('proc_administrativo', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_proc_admin', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('funcionamiento_rx', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_func_rx', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('funcionamiento_canina', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_func_canina', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('funcionamiento_incin', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_func_incin', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('envio_reclamos', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_reclamos', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('prod_no_eliminados', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_no_eliminados', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('recepcion_correos', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_recepcion', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('envios_adc', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_adc', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('envio_cites', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_cites', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('envio_ac_incidentes', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_incidentes', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('deteccion_ingreso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('obs_ingreso', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'controles', ['Turno'])

        # Adding M2M table for field inspectores on 'Turno'
        m2m_table_name = db.shorten_name(u'controles_turno_inspectores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('turno', models.ForeignKey(orm[u'controles.turno'], null=False)),
            ('usuario', models.ForeignKey(orm[u'controles.usuario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['turno_id', 'usuario_id'])

        # Adding model 'Acta_Intercepcion'
        db.create_table(u'controles_acta_intercepcion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('intercepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Intercepcion'])),
            ('inspector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Usuario'])),
            ('firma', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Acta_Intercepcion'])

        # Adding model 'Acta_Retencion'
        db.create_table(u'controles_acta_retencion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('intercepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Intercepcion'])),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desde', self.gf('django.db.models.fields.DateField')()),
            ('hasta', self.gf('django.db.models.fields.DateField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipo_envase', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'controles', ['Acta_Retencion'])

        # Adding model 'Acta_Destruccion'
        db.create_table(u'controles_acta_destruccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('intercepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Intercepcion'])),
            ('inspector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Usuario'])),
            ('firma', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('acta_intercepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Intercepcion'])),
            ('acta_retencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Retencion'])),
            ('resolucion', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('desnaturalizacion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prod_desnaturalizacion', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'controles', ['Acta_Destruccion'])

        # Adding model 'Acta_Denuncia_Citacion'
        db.create_table(u'controles_acta_denuncia_citacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('infractor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='infractor_adc', to=orm['controles.Pasajero'])),
            ('hechos', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('acta_retencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Retencion'], blank=True)),
            ('oficina_citacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hora_citacion', self.gf('django.db.models.fields.DateTimeField')()),
            ('firma', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Acta_Denuncia_Citacion'])

        # Adding model 'Acta_Incidente'
        db.create_table(u'controles_acta_incidente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('pasajero', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pasajero_ai', to=orm['controles.Pasajero'])),
            ('incidente', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('firma', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'controles', ['Acta_Incidente'])

        # Adding model 'Especimen_Cites'
        db.create_table(u'controles_especimen_cites', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_comun', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nombre_cientifico', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('pais_procedencia', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('acta_intercepcion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controles.Acta_Intercepcion'])),
            ('estado_especimen', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'controles', ['Especimen_Cites'])

        # Adding model 'Acta_Devolucion_Cites'
        db.create_table(u'controles_acta_devolucion_cites', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('fecha_devolucion', self.gf('django.db.models.fields.DateField')()),
            ('especimen', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['controles.Especimen_Cites'])),
            ('tenedor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tenedor_adci', to=orm['controles.Pasajero'])),
            ('causal', self.gf('django.db.models.fields.TextField')()),
            ('receptor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cargo_receptor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('institucion_receptor', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'controles', ['Acta_Devolucion_Cites'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'controles_usuario')

        # Removing M2M table for field groups on 'Usuario'
        db.delete_table(db.shorten_name(u'controles_usuario_groups'))

        # Removing M2M table for field user_permissions on 'Usuario'
        db.delete_table(db.shorten_name(u'controles_usuario_user_permissions'))

        # Deleting model 'ControlesFronterizos'
        db.delete_table(u'controles_controlesfronterizos')

        # Removing M2M table for field inspectores on 'ControlesFronterizos'
        db.delete_table(db.shorten_name(u'controles_controlesfronterizos_inspectores'))

        # Deleting model 'Dia_CCFF_Terrestre'
        db.delete_table(u'controles_dia_ccff_terrestre')

        # Deleting model 'Prod_Regulado'
        db.delete_table(u'controles_prod_regulado')

        # Deleting model 'Desembarco_Barco'
        db.delete_table(u'controles_desembarco_barco')

        # Deleting model 'Acta_Recepcion'
        db.delete_table(u'controles_acta_recepcion')

        # Removing M2M table for field productos_regulados on 'Acta_Recepcion'
        db.delete_table(db.shorten_name(u'controles_acta_recepcion_productos_regulados'))

        # Deleting model 'Acta_PostRecepcion'
        db.delete_table(u'controles_acta_postrecepcion')

        # Removing M2M table for field productos_regulados on 'Acta_PostRecepcion'
        db.delete_table(db.shorten_name(u'controles_acta_postrecepcion_productos_regulados'))

        # Deleting model 'Dia_CCFF_Maritimo'
        db.delete_table(u'controles_dia_ccff_maritimo')

        # Deleting model 'Acta_Inspeccion'
        db.delete_table(u'controles_acta_inspeccion')

        # Deleting model 'Sol_Inspeccion'
        db.delete_table(u'controles_sol_inspeccion')

        # Deleting model 'Dia_CCFF_Aereo'
        db.delete_table(u'controles_dia_ccff_aereo')

        # Deleting model 'Pasajero'
        db.delete_table(u'controles_pasajero')

        # Deleting model 'Prod_Interceptable'
        db.delete_table(u'controles_prod_interceptable')

        # Deleting model 'Record_Intercepcion'
        db.delete_table(u'controles_record_intercepcion')

        # Deleting model 'Intercepcion'
        db.delete_table(u'controles_intercepcion')

        # Removing M2M table for field intercepcion on 'Intercepcion'
        db.delete_table(db.shorten_name(u'controles_intercepcion_intercepcion'))

        # Deleting model 'Abandono'
        db.delete_table(u'controles_abandono')

        # Removing M2M table for field intercepcion on 'Abandono'
        db.delete_table(db.shorten_name(u'controles_abandono_intercepcion'))

        # Deleting model 'Orden_Tratamiento'
        db.delete_table(u'controles_orden_tratamiento')

        # Deleting model 'Cores'
        db.delete_table(u'controles_cores')

        # Deleting model 'Turno'
        db.delete_table(u'controles_turno')

        # Removing M2M table for field inspectores on 'Turno'
        db.delete_table(db.shorten_name(u'controles_turno_inspectores'))

        # Deleting model 'Acta_Intercepcion'
        db.delete_table(u'controles_acta_intercepcion')

        # Deleting model 'Acta_Retencion'
        db.delete_table(u'controles_acta_retencion')

        # Deleting model 'Acta_Destruccion'
        db.delete_table(u'controles_acta_destruccion')

        # Deleting model 'Acta_Denuncia_Citacion'
        db.delete_table(u'controles_acta_denuncia_citacion')

        # Deleting model 'Acta_Incidente'
        db.delete_table(u'controles_acta_incidente')

        # Deleting model 'Especimen_Cites'
        db.delete_table(u'controles_especimen_cites')

        # Deleting model 'Acta_Devolucion_Cites'
        db.delete_table(u'controles_acta_devolucion_cites')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'controles.abandono': {
            'Meta': {'object_name': 'Abandono'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'comentario_int': ('django.db.models.fields.TextField', [], {}),
            'dia': ('django.db.models.fields.DateField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['controles.Usuario']"}),
            'intercepcion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['controles.Prod_Interceptable']", 'symmetrical': 'False'}),
            'kilos': ('django.db.models.fields.FloatField', [], {}),
            'medida_int': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'probable_origen': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'rip': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['controles.Record_Intercepcion']", 'unique': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '28'})
        },
        u'controles.acta_denuncia_citacion': {
            'Meta': {'object_name': 'Acta_Denuncia_Citacion'},
            'acta_retencion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Retencion']", 'blank': 'True'}),
            'firma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hechos': ('django.db.models.fields.TextField', [], {}),
            'hora_citacion': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infractor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'infractor_adc'", 'to': u"orm['controles.Pasajero']"}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'oficina_citacion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'controles.acta_destruccion': {
            'Meta': {'object_name': 'Acta_Destruccion'},
            'acta_intercepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Intercepcion']"}),
            'acta_retencion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Retencion']"}),
            'desnaturalizacion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'firma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Usuario']"}),
            'intercepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Intercepcion']"}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'prod_desnaturalizacion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'resolucion': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'controles.acta_devolucion_cites': {
            'Meta': {'object_name': 'Acta_Devolucion_Cites'},
            'cargo_receptor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'causal': ('django.db.models.fields.TextField', [], {}),
            'especimen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['controles.Especimen_Cites']"}),
            'fecha_devolucion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion_receptor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'receptor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tenedor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tenedor_adci'", 'to': u"orm['controles.Pasajero']"})
        },
        u'controles.acta_incidente': {
            'Meta': {'object_name': 'Acta_Incidente'},
            'firma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidente': ('django.db.models.fields.TextField', [], {}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'pasajero': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pasajero_ai'", 'to': u"orm['controles.Pasajero']"})
        },
        u'controles.acta_inspeccion': {
            'Meta': {'object_name': 'Acta_Inspeccion'},
            'compania_aerea': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora_estimada': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre_aeropuerto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'origen': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_vuelo': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'vuelo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'controles.acta_intercepcion': {
            'Meta': {'object_name': 'Acta_Intercepcion'},
            'firma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Usuario']"}),
            'intercepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Intercepcion']"}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'controles.acta_postrecepcion': {
            'Meta': {'object_name': 'Acta_PostRecepcion'},
            'adc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'agencia': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'animal_a_bordo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'area_no_inspeccionada': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'arribo': ('django.db.models.fields.DateTimeField', [], {}),
            'basuras_fijas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'basuras_hermeticas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'basuras_tapadas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deficiencia_corregida': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desembarco_basuras': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desembarcos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Desembarco_Barco']"}),
            'hombres_desembarcan': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantiene_sellos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monitoreo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'motivo_adc': ('django.db.models.fields.TextField', [], {}),
            'mujeres_desembarcan': ('django.db.models.fields.IntegerField', [], {}),
            'nombre_nave': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'numero_animal': ('django.db.models.fields.IntegerField', [], {}),
            'numero_sellos': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'prod_sellados_recepcion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'productos_regulados': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['controles.Prod_Regulado']", 'symmetrical': 'False'}),
            'puerto_anterior': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'puerto_c_limantria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'puerto_inspeccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'puerto_siguiente': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'recepcion': ('django.db.models.fields.DateTimeField', [], {}),
            'sellos_rotos': ('django.db.models.fields.TextField', [], {}),
            'sitio_atraque': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'solicitan_antecedentes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'supervision_sag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_animal': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'transbordo_basuras': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ubicacion_sellos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zarpe': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'controles.acta_recepcion': {
            'Meta': {'object_name': 'Acta_Recepcion'},
            'agencia': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'animal_a_bordo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'area_no_inspeccionada': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'arribo': ('django.db.models.fields.DateTimeField', [], {}),
            'basuras_fijas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'basuras_hermeticas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'basuras_tapadas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cert_fitosanitario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deficiencia_corregida': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descensos': ('django.db.models.fields.IntegerField', [], {}),
            'desembarcos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Desembarco_Barco']"}),
            'hombres_desembarcan': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres_desembarcan': ('django.db.models.fields.IntegerField', [], {}),
            'nombre_nave': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'numero_animal': ('django.db.models.fields.IntegerField', [], {}),
            'numero_sellos': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'pasajeros_ingresan': ('django.db.models.fields.IntegerField', [], {}),
            'periodo_revision': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'productos_regulados': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['controles.Prod_Regulado']", 'symmetrical': 'False'}),
            'puerto_anterior': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'puerto_c_limantria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'puerto_inspeccion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'puerto_siguiente': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'recepcion': ('django.db.models.fields.DateTimeField', [], {}),
            'revision_listado_puertos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sitio_atraque': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'solicitan_antecedentes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_animal': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ubicacion_sellos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zarpe': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'controles.acta_retencion': {
            'Meta': {'object_name': 'Acta_Retencion'},
            'desde': ('django.db.models.fields.DateField', [], {}),
            'hasta': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Intercepcion']"}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'tipo_envase': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'controles.controlesfronterizos': {
            'Meta': {'object_name': 'ControlesFronterizos'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'comuna': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'horario_inicio': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'horario_termino': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspectores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['controles.Usuario']", 'null': 'True', 'symmetrical': 'False'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '8'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '8'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'controles.cores': {
            'Meta': {'object_name': 'Cores'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'controles.desembarco_barco': {
            'Meta': {'object_name': 'Desembarco_Barco'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'controles.dia_ccff_aereo': {
            'Meta': {'object_name': 'Dia_CCFF_Aereo'},
            'acta_inspeccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Inspeccion']"}),
            'avion_carga_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_carga_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_carga_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_carga_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_pas_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'avion_pas_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'avioneta_ffaa_ingresada': ('django.db.models.fields.IntegerField', [], {}),
            'avioneta_ffaa_inspeccionada': ('django.db.models.fields.IntegerField', [], {}),
            'avioneta_ingresada': ('django.db.models.fields.IntegerField', [], {}),
            'avioneta_inspeccionada': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_flora': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_flora': ('django.db.models.fields.IntegerField', [], {}),
            'control_fronterizo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.ControlesFronterizos']"}),
            'declaran_no_no_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_no_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_si_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'heli_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'heli_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'heli_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'heli_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'hombres_ingresados': ('django.db.models.fields.IntegerField', [], {}),
            'hombres_inspeccionados': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['controles.Usuario']", 'unique': 'True'}),
            'mujeres_ingresadas': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres_inspeccionadas': ('django.db.models.fields.IntegerField', [], {}),
            'n_adc': ('django.db.models.fields.IntegerField', [], {}),
            'n_declaran': ('django.db.models.fields.IntegerField', [], {}),
            'solicitud_inspeccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Sol_Inspeccion']"})
        },
        u'controles.dia_ccff_maritimo': {
            'Meta': {'object_name': 'Dia_CCFF_Maritimo'},
            'acta_recepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Recepcion']"}),
            'aviso_recalada_inicio': ('django.db.models.fields.IntegerField', [], {}),
            'aviso_recalada_termino': ('django.db.models.fields.IntegerField', [], {}),
            'cisterna_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'cisterna_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_flora': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_flora': ('django.db.models.fields.IntegerField', [], {}),
            'contenedor_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'contenedor_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'control_fronterizo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.ControlesFronterizos']"}),
            'crucero_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'crucero_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_no_no_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_no_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_si_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'guerra_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'guerra_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'hombres_ingresados': ('django.db.models.fields.IntegerField', [], {}),
            'hombres_inspeccionados': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['controles.Usuario']", 'unique': 'True'}),
            'instruccion_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'instruccion_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'mercante_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'mercante_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres_ingresadas': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres_inspeccionadas': ('django.db.models.fields.IntegerField', [], {}),
            'n_adc': ('django.db.models.fields.IntegerField', [], {}),
            'n_declaran': ('django.db.models.fields.IntegerField', [], {}),
            'pas_carga_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'pas_carga_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'post_recepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_PostRecepcion']"}),
            'tanque_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'tanque_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {})
        },
        u'controles.dia_ccff_terrestre': {
            'Meta': {'object_name': 'Dia_CCFF_Terrestre'},
            'auto_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'auto_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'bicicletas_ingresadas': ('django.db.models.fields.IntegerField', [], {}),
            'bicicletas_inspeccionadas': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ffaa_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ffaa_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'bus_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'bus_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_atingente_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_atingente_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_ffaa_at_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_ffaa_at_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_ffaa_no_at_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_ffaa_no_at_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_no_atingente_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'camion_no_atingente_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_entrada_flora': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_fauna': ('django.db.models.fields.IntegerField', [], {}),
            'cites_salida_flora': ('django.db.models.fields.IntegerField', [], {}),
            'control_fronterizo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.ControlesFronterizos']"}),
            'declaran_no_no_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_no_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'declaran_si_si_traen': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hombres_ingresados': ('django.db.models.fields.IntegerField', [], {}),
            'hombres_inspeccionados': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['controles.Usuario']", 'unique': 'True'}),
            'moto_ingresada': ('django.db.models.fields.IntegerField', [], {}),
            'moto_inspeccionada': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres_ingresadas': ('django.db.models.fields.IntegerField', [], {}),
            'mujeres_inspeccionadas': ('django.db.models.fields.IntegerField', [], {}),
            'n_adc': ('django.db.models.fields.IntegerField', [], {}),
            'n_declaran': ('django.db.models.fields.IntegerField', [], {}),
            'tren_carga_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'tren_carga_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'tren_pas_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'tren_pas_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_dipl_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_dipl_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_hum_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_hum_inspeccionado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_part_ingresado': ('django.db.models.fields.IntegerField', [], {}),
            'vehiculo_part_inspeccionado': ('django.db.models.fields.IntegerField', [], {})
        },
        u'controles.especimen_cites': {
            'Meta': {'object_name': 'Especimen_Cites'},
            'acta_intercepcion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Acta_Intercepcion']"}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'estado_especimen': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_comun': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pais_procedencia': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'controles.intercepcion': {
            'Meta': {'object_name': 'Intercepcion'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'comentario_int': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercepcion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['controles.Prod_Interceptable']", 'symmetrical': 'False'}),
            'kilos': ('django.db.models.fields.FloatField', [], {}),
            'medida_int': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'pasajero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Pasajero']"}),
            'rip': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['controles.Record_Intercepcion']", 'unique': 'True'})
        },
        u'controles.orden_tratamiento': {
            'Meta': {'object_name': 'Orden_Tratamiento'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'controles.pasajero': {
            'Meta': {'object_name': 'Pasajero'},
            'declara': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controles.Usuario']"}),
            'n_doc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nombres_apellidos': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'pais_origen': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'proceso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prox_puerto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo_doc': ('django.db.models.fields.CharField', [], {'max_length': '19'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '28'}),
            'ultimo_puerto': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'controles.prod_interceptable': {
            'Meta': {'object_name': 'Prod_Interceptable'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subtipo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'controles.prod_regulado': {
            'Meta': {'object_name': 'Prod_Regulado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilogramos': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'medida_adoptada': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'numero_muestra': ('django.db.models.fields.IntegerField', [], {}),
            'pais_origen': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'producto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'unidad_muestra': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'controles.record_intercepcion': {
            'Meta': {'object_name': 'Record_Intercepcion'},
            'folio_protocolo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kilos': ('django.db.models.fields.FloatField', [], {})
        },
        u'controles.sol_inspeccion': {
            'Meta': {'object_name': 'Sol_Inspeccion'},
            'compania_aerea': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'escala_dos': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'escala_uno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora_estimada': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'origen': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ruta': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_vuelo': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'vuelo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'controles.turno': {
            'Meta': {'object_name': 'Turno'},
            'deteccion_ingreso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'deteccion_prod_no_conf': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'dia_entrega': ('django.db.models.fields.DateTimeField', [], {}),
            'envio_ac_incidentes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'envio_cites': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'envio_reclamos': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'envios_adc': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'funcionamiento_canina': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'funcionamiento_incin': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'funcionamiento_rx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspectores': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['controles.Usuario']"}),
            'intercepcion_ampliada': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'jefe_turno': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['controles.Usuario']"}),
            'llenado_furi': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'obs_adc': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_cites': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_deteccion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_func_canina': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_func_incin': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_func_rx': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_incidentes': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_ingreso': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_intercepcion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_llenado': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_no_eliminados': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_proc_admin': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_recepcion': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'obs_reclamos': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'proc_administrativo': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'prod_no_eliminados': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'recepcion_correos': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'sgte_jefe_turno': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['controles.Usuario']"})
        },
        u'controles.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['controles']