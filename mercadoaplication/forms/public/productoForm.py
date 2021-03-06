"""
    AUTHOR:         luis mora
    CREATION DATE:  11/06/2021
    DESCRIPTION:    Form de la tabla producto del esquema public

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        DATE    ||  MODIFIED_BY ||  DESCRIPTION
    --------------------------------------------------------
                ||              ||  
                ||              ||  
"""
#importar modelos
from mercadoaplication.models.producto import Producto

from django import forms

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields = ('nombre', 'precioventa', 'existencia')
		widgets = {

				  'nombre': forms.TextInput(attrs=   {'id':'nombre',
				  	                                'maxlength':'30',
					                                'required':'true',
					                                'class':'input-field',
					                                'oninput':'toUpperCase(this)'}),
				  'precioventa': forms.FloatField(attrs=   {'id':'comisionporcentaje',
				   	                                                'step': '0.01'}),
				  'existencia': forms.NumberInput(attrs=   {'id':'existencia',})
		}
